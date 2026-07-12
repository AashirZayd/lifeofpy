from .base import ValidationRuleProtocol
from .diagnostics import DiagnosticsReport
from .models import ValidatorManifest

SUPPORTED_FRAMEWORKS = {"tkinter", "customtkinter", "pyside6", "pyqt6"}

class FrameworkRule(ValidationRuleProtocol):
    @property
    def name(self) -> str:
        return "FrameworkRule"

    def validate(self, target: ValidatorManifest, report: DiagnosticsReport) -> None:
        if not target.supportedFrameworks:
            report.add_error(
                code="VAL-FWK-001",
                title="No Supported Frameworks",
                description="The component must support at least one framework.",
                suggestion="Add 'customtkinter' to supportedFrameworks."
            )
            return

        for fwk in target.supportedFrameworks:
            if fwk not in SUPPORTED_FRAMEWORKS:
                report.add_error(
                    code="VAL-FWK-002",
                    title="Unsupported Framework",
                    description=f"Framework '{fwk}' is not supported.",
                    suggestion=f"Must be one of: {', '.join(SUPPORTED_FRAMEWORKS)}"
                )
