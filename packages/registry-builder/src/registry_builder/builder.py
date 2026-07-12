import json
import shutil
from pathlib import Path

from checksum_generator.hasher import generate_file_sha256
from engine.logger import setup_logger
from engine.resolver import DependencyResolver
from manifest_validator.validator import ManifestValidationError, validate_component_manifest
from search_indexer.indexer import SearchIndexer

logger = setup_logger("registry-builder")


def build_registry(source_dir: Path, output_dir: Path):
    logger.info(f"Starting registry build from {source_dir} to {output_dir}")

    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)

    components_out_dir = output_dir / "components"
    components_out_dir.mkdir()

    indexer = SearchIndexer(output_dir)
    resolver = DependencyResolver()

    valid_manifests = {}

    for component_dir in source_dir.iterdir():
        if not component_dir.is_dir():
            continue

        manifest_path = component_dir / "manifest.json"
        if not manifest_path.exists():
            logger.warning(f"Skipping {component_dir.name}, missing manifest.json")
            continue

        try:
            manifest = validate_component_manifest(manifest_path)

            # Generate checksums for files
            checksums = {}
            for file_path in component_dir.rglob("*"):
                if file_path.is_file():
                    rel_path = file_path.relative_to(component_dir).as_posix()
                    checksums[rel_path] = generate_file_sha256(file_path)

            manifest_dict = manifest.model_dump(mode="json")
            manifest_dict["_checksums"] = checksums

            valid_manifests[manifest.id] = manifest_dict
            resolver.add_node(manifest.id, manifest.dependencies)
            indexer.add_component(manifest_dict)

            # Copy to output
            with open(components_out_dir / f"{manifest.id}.json", "w", encoding="utf-8") as f:
                json.dump(manifest_dict, f, indent=2)

            logger.info(f"Validated and indexed {manifest.id}")

        except ManifestValidationError as e:
            logger.error(f"Validation failed for {component_dir.name}:\n{e}")
            raise  # Fail CI

    # Resolve DAG to ensure no circular dependencies
    for cid in valid_manifests.keys():
        logger.info(f"Checking dependency graph for {cid}")
        resolver.resolve(cid)

    # Generate static indexes
    indexer.build_indexes()

    # Generate main registry.json
    with open(output_dir / "registry.json", "w", encoding="utf-8") as f:
        json.dump({"version": "v1", "components": list(valid_manifests.values())}, f, indent=2)

    logger.info("Registry build complete.")
