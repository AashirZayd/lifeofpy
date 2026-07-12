from pathlib import Path
from ..exceptions.filesystem import InvalidPathError

def normalize_path(path: Path | str) -> Path:
    """Normalizes a path, resolving symlinks and making it absolute safely."""
    try:
        p = Path(path).resolve()
        return p
    except Exception as e:
        raise InvalidPathError(f"Failed to normalize path {path}: {e}")

def validate_safe_path(base: Path | str, target: Path | str) -> Path:
    """Ensures a target path resolves within the base directory to prevent path traversal."""
    base_path = normalize_path(base)
    target_path = normalize_path(Path(base) / target)
    
    if not str(target_path).startswith(str(base_path)):
        raise InvalidPathError(f"Path traversal detected: {target} escapes {base}")
    return target_path
