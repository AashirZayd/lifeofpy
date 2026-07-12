from core.exceptions.base import LifeOfPyError


class ValidationError(LifeOfPyError):
    pass


class ManifestValidationError(ValidationError):
    pass


class DependencyValidationError(ValidationError):
    pass


class FrameworkValidationError(ValidationError):
    pass


class LicenseValidationError(ValidationError):
    pass


class StructureValidationError(ValidationError):
    pass


class ChecksumValidationError(ValidationError):
    pass


class SchemaValidationError(ValidationError):
    pass
