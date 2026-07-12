from core.exceptions.base import LifeOfPyError


class RegistryBuilderError(LifeOfPyError):
    pass


class DiscoveryError(RegistryBuilderError):
    pass


class ValidationError(RegistryBuilderError):
    pass


class ResolutionError(RegistryBuilderError):
    pass


class GenerationError(RegistryBuilderError):
    pass


class ChecksumError(RegistryBuilderError):
    pass


class WriterError(RegistryBuilderError):
    pass
