import pytest
from pathlib import Path
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger
from engine.validator.service import ManifestValidationService
from engine.validator.diagnostics import Severity

@pytest.fixture
def logger():
    return DefaultLogger()

@pytest.fixture
def fs(logger):
    return FileSystemService(logger)

@pytest.fixture
def validator(logger, fs):
    return ManifestValidationService(logger, fs)

def test_valid_manifest(validator):
    data = {
        "id": "button-modern",
        "slug": "button-modern",
        "name": "Modern Button",
        "description": "A beautiful button",
        "version": "1.0.0",
        "author": "LifeOfPy",
        "license": "MIT",
        "category": "Buttons",
        "supportedFrameworks": ["customtkinter"]
    }
    report = validator.validate_manifest(data)
    assert not report.has_errors

def test_invalid_schema(validator):
    data = {
        "id": "button-modern"
    }
    report = validator.validate_manifest(data)
    assert report.has_errors
    assert any(d.code == "VAL-SCH-001" for d in report.diagnostics)

def test_semver_rule(validator):
    data = {
        "id": "btn",
        "slug": "btn",
        "name": "btn",
        "description": "desc",
        "version": "v1.0",
        "author": "me",
        "license": "MIT",
        "category": "Cat",
        "supportedFrameworks": ["customtkinter"]
    }
    report = validator.validate_manifest(data)
    assert report.has_errors
    assert any(d.code == "VAL-SEMVER-001" for d in report.diagnostics)

def test_framework_rule(validator):
    data = {
        "id": "btn",
        "slug": "btn",
        "name": "btn",
        "description": "desc",
        "version": "1.0.0",
        "author": "me",
        "license": "MIT",
        "category": "Cat",
        "supportedFrameworks": ["invalid_fwk"]
    }
    report = validator.validate_manifest(data)
    assert report.has_errors
    assert any(d.code == "VAL-FWK-002" for d in report.diagnostics)

def test_license_rule(validator):
    data = {
        "id": "btn",
        "slug": "btn",
        "name": "btn",
        "description": "desc",
        "version": "1.0.0",
        "author": "me",
        "license": "WTFPL",
        "category": "Cat",
        "supportedFrameworks": ["customtkinter"]
    }
    report = validator.validate_manifest(data)
    assert not report.has_errors
    assert any(d.severity == Severity.WARNING and d.code == "VAL-LIC-001" for d in report.diagnostics)

def test_dependency_rule(validator):
    data = {
        "id": "btn",
        "slug": "btn",
        "name": "btn",
        "description": "desc",
        "version": "1.0.0",
        "author": "me",
        "license": "MIT",
        "category": "Cat",
        "supportedFrameworks": ["customtkinter"],
        "componentDependencies": ["dep1", "dep1"]
    }
    report = validator.validate_manifest(data)
    assert report.has_errors
    assert any(d.code == "VAL-DEP-001" for d in report.diagnostics)
    
def test_component_structure(validator, fs, tmp_path):
    comp_dir = tmp_path / "button-modern"
    fs.create_directory(comp_dir)
    
    report = validator.validate_component(comp_dir)
    assert report.has_errors
    assert any(d.code == "VAL-STR-002" for d in report.diagnostics)
    
    fs.write_text_atomic(comp_dir / "component.py", "# code")
    fs.write_text_atomic(comp_dir / "README.md", "# readme")
    fs.write_text_atomic(comp_dir / "manifest.json", "{invalid json")
    
    report = validator.validate_component(comp_dir)
    assert report.has_errors
    assert any(d.code == "VAL-IO-001" for d in report.diagnostics)
    
    fs.write_text_atomic(comp_dir / "manifest.json", '{"id": "btn", "slug": "btn", "name": "btn", "description": "desc", "version": "1.0.0", "author": "me", "license": "MIT", "category": "Cat", "supportedFrameworks": ["customtkinter"]}')
    report = validator.validate_component(comp_dir)
    assert not report.has_errors

def test_validate_registry(validator, fs, tmp_path):
    reg_dir = tmp_path / "registry"
    fs.create_directory(reg_dir)
    
    report = validator.validate_registry(reg_dir)
    assert report.has_errors
    assert any(d.code == "VAL-REG-001" for d in report.diagnostics)
    
    comp_dir = reg_dir / "components" / "btn"
    fs.create_directory(comp_dir, parents=True)
    fs.write_text_atomic(comp_dir / "component.py", "")
    fs.write_text_atomic(comp_dir / "README.md", "")
    fs.write_text_atomic(comp_dir / "manifest.json", '{"id": "btn", "slug": "btn", "name": "btn", "description": "desc", "version": "1.0.0", "author": "me", "license": "MIT", "category": "Cat", "supportedFrameworks": ["customtkinter"]}')
    
    report = validator.validate_registry(reg_dir)
    assert not report.has_errors
