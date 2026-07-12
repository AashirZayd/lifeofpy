import json
from pathlib import Path
from typing import Any, Dict

from core.filesystem.base import FileSystemProtocol
from core.logging.logger import LoggerProtocol

from engine.validator.service import ManifestValidationService

from .checksums import ChecksumGenerator
from .collector import ComponentCollector
from .indexer import IndexGenerator
from .metadata import MetadataGenerator
from .resolver import DependencyResolver
from .sorter import DeterministicSorter
from .statistics import StatisticsGenerator
from .writer import RegistryWriter


class RegistryPipeline:
    def __init__(self, logger: LoggerProtocol, fs: FileSystemProtocol):
        self.logger = logger
        self.fs = fs
        self.validator = ManifestValidationService(logger, fs)

        self.collector = ComponentCollector(logger, fs, self.validator)
        self.resolver = DependencyResolver()
        self.sorter = DeterministicSorter()
        self.indexer = IndexGenerator()
        self.metadata_gen = MetadataGenerator()
        self.stats_gen = StatisticsGenerator()
        self.writer = RegistryWriter(logger, fs)
        self.checksums_gen = ChecksumGenerator(logger, fs)

    def build(self, source_dir: Path, output_dir: Path) -> Path:
        self.logger.info("Starting Registry Build Pipeline")

        comp_map = self.collector.discover(source_dir)
        manifests = list(comp_map.values())

        if not manifests:
            self.logger.warning("No components discovered. Registry will be empty.")

        self.logger.info("Resolving dependencies...")
        resolved_manifests = self.resolver.resolve(manifests)

        self.logger.info("Sorting components...")
        sorted_manifests = self.sorter.sort_manifests(resolved_manifests)

        self.logger.info("Generating artifacts...")
        artifacts: Dict[str, Any] = {}

        indexes = self.indexer.generate(sorted_manifests)
        artifacts.update(indexes)

        stats = self.stats_gen.generate(sorted_manifests)
        artifacts["statistics.json"] = stats

        metadata = self.metadata_gen.generate(sorted_manifests)
        artifacts["metadata.json"] = metadata.model_dump()

        artifacts["registry.json"] = {
            "version": "1.0.0",
            "metadata": metadata.model_dump(),
            "components": [m.model_dump() for m in sorted_manifests],
        }

        self.writer.write(output_dir, artifacts, comp_map)

        self.logger.info("Generating checksums...")
        checksums = self.checksums_gen.generate_for_directory(output_dir)
        self.fs.write_text_atomic(output_dir / "checksums.json", json.dumps(checksums, indent=2, sort_keys=True))

        self.logger.info(f"Registry build complete at {output_dir}")
        return output_dir
