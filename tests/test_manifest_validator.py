import pytest
from manifest_validator.validator import validate_component_manifest, ManifestValidationError

def test_valid_manifest():
    data = {
        "id": "test-id",
        "name": "Test",
        "description": "Test desc",
        "version": "1.0.0",
        "author": "aashir",
        "license": "MIT",
        "supported_frameworks": ["customtkinter"],
        "category": "Tests"
    }
    manifest = validate_component_manifest(data)
    assert manifest.id == "test-id"
    
def test_invalid_manifest():
    with pytest.raises(ManifestValidationError):
        validate_component_manifest({})
