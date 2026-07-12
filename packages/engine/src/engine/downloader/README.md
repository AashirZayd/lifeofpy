# LifeOfPy Downloader Engine

The Downloader Engine is responsible for securely and deterministically transferring registry payloads to a local staging environment. It operates asynchronously (via queue and scheduler abstractions) and prevents corrupt or unverified data from bleeding into the user's project space.

## Architecture Pipeline
1. **Queueing & Scheduling (`queue.py`, `scheduler.py`)**: Accepts download requests and resolves them asynchronously in a deterministic queue structure.
2. **Transfer Layer (`transfer.py`)**: Uses the injected `RegistryProviderProtocol` to handle actual HTTP/Socket requests. It is perfectly decoupled from whether the source is GitHub, a corporate mirror, or an offline folder.
3. **Verification (`verification.py`)**: Cryptographically guarantees that downloaded assets match exactly what the dependency graph resolved via SHA-256. 
4. **Staging (`staging.py`)**: Deposits files into temporary OS directories. If verification fails, the staging area is immediately scrubbed and the failure is logged.

## Public API

```python
from engine.downloader.service import DownloaderService
from core.registry.github import GitHubProvider
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger

logger = DefaultLogger()
fs = FileSystemService(logger)
provider = GitHubProvider(logger, fs)

downloader = DownloaderService(provider, fs, logger)

# Subscribe to beautiful CLI progress events
downloader.subscribe_progress(lambda evt: print(evt.status))

# Execute a single download (automatically stages and verifies)
result = downloader.download("button-modern", "1.0.0", expected_checksum="sha256:...")
```
