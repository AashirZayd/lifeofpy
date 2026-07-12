from typing import Any, List

from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest


class RuleEngine:
    def __init__(self):
        self.rules: List[ValidationRuleProtocol] = []

    def register(self, rule: ValidationRuleProtocol):
        self.rules.append(rule)

    def execute_manifest_rules(self, manifest: ValidatorManifest, report: DiagnosticsReport):
        for rule in self.rules:
            if hasattr(rule, "validate"):
                try:
                    if rule.name != "FolderStructureRule":
                        rule.validate(manifest, report)
                except Exception as e:
                    report.add_error(
                        code="VAL-SYS-001",
                        title="Rule Execution Failed",
                        description=f"Rule {rule.name} failed to execute: {e}",
                    )

    def execute_structure_rules(self, dir_path: Any, report: DiagnosticsReport):
        for rule in self.rules:
            if rule.name == "FolderStructureRule":
                rule.validate({"dir_path": dir_path}, report)
