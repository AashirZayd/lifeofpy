# LifeOfPy Manifest Validator

The Manifest Validator is the canonical validation engine for every component in the LifeOfPy ecosystem.

## Architecture
The system employs a strict, compiler-like architecture:
1. **Pydantic Schemas (`models.py`)**: Responsible for base type checking and required field validation.
2. **Rule Engine (`rules.py`)**: Orchestrates individual, decoupled `ValidationRuleProtocol` implementations (SemVer, Licenses, Dependencies, Frameworks).
3. **Diagnostics (`diagnostics.py`)**: Emits structured errors, warnings, and informational messages rather than raw Python exceptions, providing compiler-style `DiagnosticsReport` objects.

## Usage
The service relies on the core FileSystem and Logging abstractions:

```python
from engine.validator.service import ManifestValidationService
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger

logger = DefaultLogger()
fs = FileSystemService(logger)
validator = ManifestValidationService(logger, fs)

# Validate a full component directory
report = validator.validate_component("/path/to/button-modern")

if report.has_errors:
    for diag in report.get_errors():
        print(f"[{diag.code}] {diag.title}: {diag.description}")
        if diag.suggestion:
            print(f"  -> Suggestion: {diag.suggestion}")
```
