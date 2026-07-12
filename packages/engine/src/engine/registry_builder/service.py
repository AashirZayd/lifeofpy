from pathlib import Path
from typing import Dict, List

from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from engine.validator.models import ValidatorManifest

from .base import RegistryBuilderProtocol
from .checksums import ChecksumGenerator
from .indexer import IndexGenerator
from .pipeline import RegistryPipeline
from .statistics import StatisticsGenerator


class RegistryBuilderService(RegistryBuilderProtocol):
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs
        self.pipeline = RegistryPipeline(logger, fs)

    def build_registry(self, source_dir: Path | str, output_dir: Path | str) -> Path:
        return self.pipeline.build(Path(source_dir), Path(output_dir))

    def build_indexes(self, manifests: List[ValidatorManifest]) -> Dict[str, dict]:
        return IndexGenerator.generate(manifests)

    def build_statistics(self, manifests: List[ValidatorManifest]) -> dict:
        return StatisticsGenerator.generate(manifests)

    def build_checksums(self, output_dir: Path | str) -> dict:
        gen = ChecksumGenerator(self.logger, self.fs)
        return gen.generate_for_directory(Path(output_dir))

    def verify_registry(self, registry_dir: Path | str) -> bool:
        d = Path(registry_dir)
        return self.fs.exists(d / "registry.json") and self.fs.exists(d / "checksums.json")

    def clean_registry(self, registry_dir: Path | str) -> None:
        self.fs.delete_directory(Path(registry_dir), recursive=True)
