from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest

VALID_LICENSES = {"MIT", "Apache-2.0", "GPL-3.0", "BSD-3-Clause", "Proprietary"}


class LicenseRule(ValidationRuleProtocol):
    @property
    def name(self) -> str:
        return "LicenseRule"

    def validate(self, target: ValidatorManifest, report: DiagnosticsReport) -> None:
        if target.license not in VALID_LICENSES:
            report.add_warning(
                code="VAL-LIC-001",
                title="Unrecognized License",
                description=f"The license '{target.license}' is not in the standard SPDX list.",
                suggestion="Use a standard SPDX identifier like 'MIT' or 'Apache-2.0'.",
            )
