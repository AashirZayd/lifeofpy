from core.exceptions.base import LifeOfPyError

class DependencyGraphError(LifeOfPyError):
    pass

class ResolutionError(DependencyGraphError):
    pass

class CycleDetectedError(DependencyGraphError):
    pass

class ConflictDetectedError(DependencyGraphError):
    pass

class PlanningError(DependencyGraphError):
    pass
