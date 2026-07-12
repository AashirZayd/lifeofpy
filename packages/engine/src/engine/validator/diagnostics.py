from enum import Enum
from typing import Optional, List
from pydantic import BaseModel

class Severity(str, Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"

class Diagnostic(BaseModel):
    severity: Severity
    code: str
    title: str
    description: str
    suggestion: Optional[str] = None
    file: Optional[str] = None
    line: Optional[int] = None
    doc_link: Optional[str] = None

class DiagnosticsReport:
    def __init__(self):
        self.diagnostics: List[Diagnostic] = []

    def add(self, diagnostic: Diagnostic):
        self.diagnostics.append(diagnostic)

    def add_error(self, code: str, title: str, description: str, **kwargs):
        self.add(Diagnostic(severity=Severity.ERROR, code=code, title=title, description=description, **kwargs))

    def add_warning(self, code: str, title: str, description: str, **kwargs):
        self.add(Diagnostic(severity=Severity.WARNING, code=code, title=title, description=description, **kwargs))

    def add_info(self, code: str, title: str, description: str, **kwargs):
        self.add(Diagnostic(severity=Severity.INFO, code=code, title=title, description=description, **kwargs))

    @property
    def has_errors(self) -> bool:
        return any(d.severity == Severity.ERROR for d in self.diagnostics)

    def get_errors(self) -> List[Diagnostic]:
        return [d for d in self.diagnostics if d.severity == Severity.ERROR]
