from typing import List, Dict, Set
from engine.validator.models import ValidatorManifest
from .errors import ResolutionError

class DependencyResolver:
    def resolve(self, manifests: List[ValidatorManifest]) -> List[ValidatorManifest]:
        manifest_map = {m.slug: m for m in manifests}
        visited: Set[str] = set()
        path: Set[str] = set()
        resolved: List[ValidatorManifest] = []

        def visit(slug: str):
            if slug in path:
                raise ResolutionError(f"Circular dependency detected involving '{slug}'")
            if slug in visited:
                return
            
            if slug not in manifest_map:
                raise ResolutionError(f"Missing dependency: '{slug}'")

            path.add(slug)
            manifest = manifest_map[slug]
            for dep in sorted(manifest.componentDependencies):
                visit(dep)
                
            path.remove(slug)
            visited.add(slug)
            resolved.append(manifest)

        for slug in sorted(manifest_map.keys()):
            if slug not in visited:
                visit(slug)

        return resolved
