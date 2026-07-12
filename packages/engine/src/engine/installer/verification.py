from pathlib import Path
from core.filesystem.base import FileSystemProtocol
from engine.validator.service import ManifestValidationService
from .errors import VerificationError

class InstallationVerifier:
    def __init__(self, fs: FileSystemProtocol, validator: ManifestValidationService):
        self.fs = fs
        self.validator = validator

    def verify_staged_component(self, staged_dir: Path) -> bool:
        if not self.fs.exists(staged_dir):
            raise VerificationError(f"Staged component directory missing: {staged_dir}")

        report = self.validator.validate_component(staged_dir)
        if report.has_errors:
            error_msgs = ", ".join([d.description for d in report.get_errors()])
            raise VerificationError(f"Component validation failed during staging: {error_msgs}")

        return True
        
    def verify_installation(self, project_dir: Path, component_slug: str) -> bool:
        target = project_dir / "components" / component_slug
        if not self.fs.exists(target):
            raise VerificationError(f"Component {component_slug} is missing from project.")
        return True
