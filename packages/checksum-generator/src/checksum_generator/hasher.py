import hashlib
from pathlib import Path

def generate_file_sha256(file_path: str | Path) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
        
    sha256_hash = hashlib.sha256()
    with open(path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
            
    return sha256_hash.hexdigest()

def generate_string_sha256(content: str) -> str:
    return hashlib.sha256(content.encode('utf-8')).hexdigest()
