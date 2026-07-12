import re

from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest

SEMVER_REGEX = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)


class SemVerRule(ValidationRuleProtocol):
    @property
    def name(self) -> str:
        return "SemVerRule"

    def validate(self, target: ValidatorManifest, report: DiagnosticsReport) -> None:
        if not SEMVER_REGEX.match(target.version):
            report.add_error(
                code="VAL-SEMVER-001",
                title="Invalid Semantic Version",
                description=f"The version '{target.version}' does not strictly follow SemVer 2.0.0 rules.",
                suggestion="Format as MAJOR.MINOR.PATCH (e.g., 1.0.0)",
            )
