import json
from pathlib import Path
from typing import Union
from pydantic import ValidationError
from .models import ComponentManifest, PackManifest

class ManifestValidationError(Exception):
    pass

def validate_component_manifest(data: Union[dict, str, Path]) -> ComponentManifest:
    try:
        if isinstance(data, Path):
            with open(data, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif isinstance(data, str):
            data = json.loads(data)
        
        return ComponentManifest(**data)
    except ValidationError as e:
        raise ManifestValidationError(f"Invalid Component Manifest:\n{e.json(indent=2)}")
    except json.JSONDecodeError as e:
        raise ManifestValidationError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise ManifestValidationError(f"Unexpected error validating manifest: {e}")

def validate_pack_manifest(data: Union[dict, str, Path]) -> PackManifest:
    try:
        if isinstance(data, Path):
            with open(data, 'r', encoding='utf-8') as f:
                data = json.load(f)
        elif isinstance(data, str):
            data = json.loads(data)
        
        return PackManifest(**data)
    except ValidationError as e:
        raise ManifestValidationError(f"Invalid Pack Manifest:\n{e.json(indent=2)}")
    except Exception as e:
        raise ManifestValidationError(f"Unexpected error validating pack manifest: {e}")
