from typing import List, Dict
from engine.validator.models import ValidatorManifest

class IndexGenerator:
    @staticmethod
    def generate(manifests: List[ValidatorManifest]) -> Dict[str, dict]:
        framework_index = {}
        category_index = {}
        tag_index = {}
        author_index = {}
        search_index = []

        for m in manifests:
            search_index.append({
                "id": m.slug,
                "name": m.name,
                "description": m.description,
                "author": m.author,
                "tags": m.tags,
                "category": m.category,
                "frameworks": m.supportedFrameworks
            })

            for f in m.supportedFrameworks:
                if f not in framework_index:
                    framework_index[f] = []
                framework_index[f].append(m.slug)

            if m.category not in category_index:
                category_index[m.category] = []
            category_index[m.category].append(m.slug)

            if m.author not in author_index:
                author_index[m.author] = []
            author_index[m.author].append(m.slug)

            for t in m.tags:
                if t not in tag_index:
                    tag_index[t] = []
                tag_index[t].append(m.slug)

        return {
            "component-index.json": {"components": [m.slug for m in manifests]},
            "framework-index.json": framework_index,
            "category-index.json": category_index,
            "tag-index.json": tag_index,
            "author-index.json": author_index,
            "search-index.json": {"entries": search_index}
        }
