import pytest
import json
from pathlib import Path
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger
from engine.registry_builder.service import RegistryBuilderService
from engine.registry_builder.errors import ResolutionError, ValidationError

@pytest.fixture
def logger():
    return DefaultLogger()

@pytest.fixture
def fs(logger):
    return FileSystemService(logger)

@pytest.fixture
def builder(logger, fs):
    return RegistryBuilderService(logger, fs)

def test_build_empty_registry(builder, fs, tmp_path):
    src = tmp_path / "src"
    out = tmp_path / "registry" / "v1"
    fs.create_directory(src)
    
    builder.build_registry(src, out)
    assert fs.exists(out / "registry.json")
    assert fs.exists(out / "checksums.json")
    assert fs.exists(out / "metadata.json")
    assert fs.exists(out / "search-index.json")

def test_circular_dependency(builder, fs, tmp_path):
    src = tmp_path / "src"
    out = tmp_path / "registry" / "v1"
    
    comp_a = src / "a"
    comp_b = src / "b"
    fs.create_directory(comp_a, parents=True)
    fs.create_directory(comp_b, parents=True)
    
    fs.write_text_atomic(comp_a / "component.py", "")
    fs.write_text_atomic(comp_a / "README.md", "")
    fs.write_text_atomic(comp_a / "manifest.json", '{"id": "a", "slug": "a", "name": "A", "description": "A", "version": "1.0.0", "author": "me", "license": "MIT", "category": "Cat", "supportedFrameworks": ["customtkinter"], "componentDependencies": ["b"]}')
    
    fs.write_text_atomic(comp_b / "component.py", "")
    fs.write_text_atomic(comp_b / "README.md", "")
    fs.write_text_atomic(comp_b / "manifest.json", '{"id": "b", "slug": "b", "name": "B", "description": "B", "version": "1.0.0", "author": "me", "license": "MIT", "category": "Cat", "supportedFrameworks": ["customtkinter"], "componentDependencies": ["a"]}')
    
    with pytest.raises(ResolutionError) as exc:
        builder.build_registry(src, out)
    assert "Circular dependency" in str(exc.value)

def test_successful_build(builder, fs, tmp_path):
    src = tmp_path / "src"
    out = tmp_path / "registry" / "v1"
    
    comp_a = src / "btn"
    fs.create_directory(comp_a, parents=True)
    fs.write_text_atomic(comp_a / "component.py", "")
    fs.write_text_atomic(comp_a / "README.md", "")
    fs.write_text_atomic(comp_a / "manifest.json", '{"id": "btn", "slug": "btn", "name": "Btn", "description": "Btn", "version": "1.0.0", "author": "me", "license": "MIT", "category": "Buttons", "supportedFrameworks": ["customtkinter"]}')
    
    builder.build_registry(src, out)
    
    assert fs.exists(out / "components" / "btn" / "component.py")
    
    idx = json.loads(fs.read_text(out / "search-index.json"))
    assert len(idx["entries"]) == 1
    assert idx["entries"][0]["id"] == "btn"
    
    stats = json.loads(fs.read_text(out / "statistics.json"))
    assert stats["totalComponents"] == 1
    
    checksums = json.loads(fs.read_text(out / "checksums.json"))
    assert "registry.json" in checksums
