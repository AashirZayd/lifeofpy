import json
from pathlib import Path
from typing import Any, Dict, List


class SearchIndexer:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.components: List[Dict[str, Any]] = []

    def add_component(self, manifest_data: dict):
        self.components.append(manifest_data)

    def build_indexes(self):
        # Generate main search index
        search_index = [
            {
                "id": c.get("id"),
                "name": c.get("name"),
                "description": c.get("description"),
                "author": c.get("author"),
                "tags": c.get("tags", []),
                "category": c.get("category"),
                "frameworks": c.get("supported_frameworks", []),
            }
            for c in self.components
        ]

        with open(self.output_dir / "search-index.json", "w", encoding="utf-8") as f:
            json.dump(search_index, f, indent=2)

        # Generate categories index
        categories = {}
        for c in self.components:
            cat = c.get("category")
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(c.get("id"))

        with open(self.output_dir / "category-index.json", "w", encoding="utf-8") as f:
            json.dump(categories, f, indent=2)
