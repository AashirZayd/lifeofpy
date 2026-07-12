import hashlib
import json
from datetime import datetime, timezone
from typing import List

from core.registry.models import Checksum, RegistryMetadata

from engine.validator.models import ValidatorManifest


class MetadataGenerator:
    @staticmethod
    def generate(manifests: List[ValidatorManifest], version: str = "1.0.0") -> RegistryMetadata:
        frameworks = set()
        categories = set()

        for m in manifests:
            frameworks.update(m.supportedFrameworks)
            categories.add(m.category)

        raw_data = json.dumps([m.model_dump() for m in manifests], sort_keys=True).encode("utf-8")
        sha = hashlib.sha256(raw_data).hexdigest()

        return RegistryMetadata(
            registryVersion=version,
            schemaVersion="1.0.0",
            engineVersion="0.1.0",
            generatedAt=datetime.now(timezone.utc),
            componentCount=len(manifests),
            frameworkCount=len(frameworks),
            categoryCount=len(categories),
            checksum=Checksum(sha256=sha),
        )
