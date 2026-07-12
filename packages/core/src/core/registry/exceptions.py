from ..exceptions.base import LifeOfPyError


class RegistryProviderError(LifeOfPyError):
    pass


class RegistryUnavailableError(RegistryProviderError):
    pass


class RegistryTimeoutError(RegistryProviderError):
    pass


class RegistryNotFoundError(RegistryProviderError):
    pass


class ComponentNotFoundError(RegistryProviderError):
    pass


class ManifestNotFoundError(RegistryProviderError):
    pass


class PackNotFoundError(RegistryProviderError):
    pass


class CacheError(RegistryProviderError):
    pass


class NetworkError(RegistryProviderError):
    pass


class ProviderConfigurationError(RegistryProviderError):
    pass
