# LifeOfPy Registry Provider

The Registry Provider is the definitive abstraction for retrieving component manifests and source files from the LifeOfPy Registry.

## Key Features
* **Backend Agnostic**: Fully decouples the `lifeofpy` CLI from GitHub.
* **Pluggable Architecture**: Seamlessly switch between `GitHubProvider`, `LocalProvider` (for offline dev/CI), and `MirrorProvider` (for failover redundancy).
* **Robust Networking**: Features an independent HTTP client with timeouts, retries, and error handling.
* **Caching Layer**: Configurable file-based caching for registry manifests to reduce network latency.

## Usage
The factory handles configuration resolution and dependency injection automatically:

```python
from core.registry.factory import RegistryFactory
from core.logging.logger import DefaultLogger
from core.filesystem.service import FileSystemService

logger = DefaultLogger()
fs = FileSystemService(logger)
factory = RegistryFactory(logger, fs)

provider = factory.create_provider({"registry_url": "https://raw.githubusercontent.com/.../v1/"})

if provider.component_exists("button-modern"):
    manifest = provider.get_manifest("button-modern")
    print(manifest.pythonDependencies)
```
