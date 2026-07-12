from typing import List
from engine.validator.models import ValidatorManifest

class DeterministicSorter:
    @staticmethod
    def sort_manifests(manifests: List[ValidatorManifest]) -> List[ValidatorManifest]:
        return sorted(manifests, key=lambda m: (
            ",".join(sorted(m.supportedFrameworks)),
            m.category,
            m.slug
        ))
