from pathlib import Path
from typing import Dict, Any, List
import json
from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol
from engine.validator.models import ValidatorManifest
from .errors import WriterError

class RegistryWriter:
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs

    def write(self, output_dir: Path, artifacts: Dict[str, Any], component_map: Dict[Path, ValidatorManifest]) -> None:
        self.logger.info(f"Writing registry to {output_dir}")
        
        with self.fs.transaction() as tx:
            self.fs.create_directory(output_dir, parents=True)
            
            for filename, data in artifacts.items():
                file_path = output_dir / filename
                content = json.dumps(data, indent=2, sort_keys=True, default=str)
                self.fs.write_text_atomic(file_path, content)
                
            target_comps = output_dir / "components"
            self.fs.create_directory(target_comps)
            
            for src_dir, manifest in component_map.items():
                dst_dir = target_comps / manifest.slug
                self.fs.copy(src_dir, dst_dir)
