from pathlib import Path
from typing import Any, Dict

from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport


class FolderStructureRule(ValidationRuleProtocol):
    @property
    def name(self) -> str:
        return "FolderStructureRule"

    def validate(self, target: Dict[str, Any], report: DiagnosticsReport) -> None:
        dir_path: Path = target.get("dir_path")
        if not dir_path or not dir_path.is_dir():
            report.add_error(
                code="VAL-STR-001",
                title="Invalid Directory",
                description=f"The path {dir_path} is not a valid directory.",
            )
            return

        required_files = ["manifest.json", "component.py", "README.md"]
        for file in required_files:
            if not (dir_path / file).exists():
                report.add_error(
                    code="VAL-STR-002",
                    title="Missing Required File",
                    description=f"The canonical file '{file}' is missing from the component directory.",
                    suggestion=f"Create {file} in {dir_path.name}/",
                )
