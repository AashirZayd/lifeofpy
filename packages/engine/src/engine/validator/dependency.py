from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest

class DependencyRule(ValidationRuleProtocol):
    @property
    def name(self) -> str:
        return "DependencyRule"

    def validate(self, target: ValidatorManifest, report: DiagnosticsReport) -> None:
        if len(target.componentDependencies) != len(set(target.componentDependencies)):
            report.add_error(
                code="VAL-DEP-001",
                title="Duplicate Component Dependencies",
                description="The componentDependencies list contains duplicate entries."
            )
            
        if len(target.pythonDependencies) != len(set(target.pythonDependencies)):
            report.add_error(
                code="VAL-DEP-002",
                title="Duplicate Python Dependencies",
                description="The pythonDependencies list contains duplicate entries."
            )
            
        if target.slug in target.componentDependencies:
            report.add_error(
                code="VAL-DEP-003",
                title="Self-Referencing Dependency",
                description="A component cannot depend on itself."
            )
