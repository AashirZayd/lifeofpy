from pathlib import Path
import json
from pydantic import ValidationError as PydanticValidationError
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from .base import ManifestValidationEngineProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest
from .rules import RuleEngine
from .semver import SemVerRule
from .licenses import LicenseRule
from .framework import FrameworkRule
from .dependency import DependencyRule
from .structure import FolderStructureRule

class ManifestValidationService(ManifestValidationEngineProtocol):
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs
        self.engine = RuleEngine()
        
        self.engine.register(SemVerRule())
        self.engine.register(LicenseRule())
        self.engine.register(FrameworkRule())
        self.engine.register(DependencyRule())
        self.engine.register(FolderStructureRule())

    def validate_manifest(self, manifest_data: dict) -> DiagnosticsReport:
        report = DiagnosticsReport()
        self.logger.debug("Validating manifest data")
        
        try:
            manifest = ValidatorManifest.model_validate(manifest_data)
        except PydanticValidationError as e:
            report.add_error(
                code="VAL-SCH-001",
                title="Schema Validation Failed",
                description=str(e),
                suggestion="Ensure all required fields are present and correctly typed."
            )
            return report
            
        self.engine.execute_manifest_rules(manifest, report)
        return report

    def validate_component(self, component_dir: Path | str) -> DiagnosticsReport:
        report = DiagnosticsReport()
        dir_path = Path(component_dir)
        self.logger.info(f"Validating component directory: {dir_path}")
        
        self.engine.execute_structure_rules(dir_path, report)
        
        if report.has_errors:
            return report
            
        manifest_path = dir_path / "manifest.json"
        try:
            content = self.fs.read_text(manifest_path)
            data = json.loads(content)
        except Exception as e:
            report.add_error(
                code="VAL-IO-001",
                title="Failed to Read Manifest",
                description=f"Could not read manifest.json: {e}"
            )
            return report
            
        manifest_report = self.validate_manifest(data)
        report.diagnostics.extend(manifest_report.diagnostics)
        
        return report

    def validate_directory(self, target_dir: Path | str) -> DiagnosticsReport:
        return self.validate_component(target_dir)

    def validate_registry(self, registry_dir: Path | str) -> DiagnosticsReport:
        report = DiagnosticsReport()
        r_dir = Path(registry_dir)
        components_dir = r_dir / "components"
        
        if not self.fs.exists(components_dir):
            report.add_error(
                code="VAL-REG-001",
                title="Invalid Registry Structure",
                description="Missing 'components/' directory in registry root."
            )
            return report
            
        for comp_dir in components_dir.iterdir():
            if comp_dir.is_dir():
                comp_report = self.validate_component(comp_dir)
                report.diagnostics.extend(comp_report.diagnostics)
                
        return report

    def validate_dependencies(self, manifest: ValidatorManifest) -> DiagnosticsReport:
        report = DiagnosticsReport()
        rule = DependencyRule()
        rule.validate(manifest, report)
        return report
