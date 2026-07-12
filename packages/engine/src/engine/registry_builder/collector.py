from pathlib import Path
from typing import Dict
import json
from engine.validator.models import ValidatorManifest
from engine.validator.service import ManifestValidationService
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol
from .errors import DiscoveryError, ValidationError

class ComponentCollector:
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol, validator: ManifestValidationService):
        self.logger = logger
        self.fs = fs
        self.validator = validator

    def discover(self, source_dir: Path) -> Dict[Path, ValidatorManifest]:
        self.logger.info(f"Discovering components in {source_dir}")
        if not self.fs.exists(source_dir):
            raise DiscoveryError(f"Source directory not found: {source_dir}")

        manifests = {}
        paths = sorted([p for p in source_dir.rglob("manifest.json") if ".git" not in str(p) and ".tmp" not in str(p)])
        
        for path in paths:
            comp_dir = path.parent
            self.logger.debug(f"Found manifest at {path}")
            
            report = self.validator.validate_component(comp_dir)
            if report.has_errors:
                self.logger.error(f"Validation failed for {comp_dir}")
                for d in report.get_errors():
                    self.logger.error(f"[{d.code}] {d.description}")
                raise ValidationError(f"Validation failed for component at {comp_dir}")

            content = self.fs.read_text(path)
            data = json.loads(content)
            manifests[comp_dir] = ValidatorManifest.model_validate(data)

        self.logger.info(f"Discovered {len(manifests)} valid components")
        return manifests
