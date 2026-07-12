from typing import List

from engine.validator.models import ValidatorManifest


class StatisticsGenerator:
    @staticmethod
    def generate(manifests: List[ValidatorManifest]) -> dict:
        total = len(manifests)
        fw_counts = {}
        cat_counts = {}
        total_deps = 0

        for m in manifests:
            cat_counts[m.category] = cat_counts.get(m.category, 0) + 1
            for f in m.supportedFrameworks:
                fw_counts[f] = fw_counts.get(f, 0) + 1
            total_deps += len(m.componentDependencies)

        return {
            "totalComponents": total,
            "componentsPerFramework": fw_counts,
            "componentsPerCategory": cat_counts,
            "averageDependencies": round(total_deps / total, 2) if total > 0 else 0,
            "packCount": 0,
            "themeCount": 0,
        }
