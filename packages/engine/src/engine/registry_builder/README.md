# LifeOfPy Registry Builder

The Registry Builder takes a raw directory containing unvalidated component source code and deterministically transforms it into a production-ready, versioned registry format (e.g. `registry/v1/`).

## Architecture Pipeline
The builder strictly adheres to a staged processing pipeline (`pipeline.py`):
1. **Discovery**: Finds all `manifest.json` files recursively.
2. **Validation**: Passes every found component through the `Manifest Validation Engine`. If a single component fails, the build halts.
3. **Resolution**: Generates a dependency graph and detects circular dependencies.
4. **Sorting**: Enforces deterministic ordering.
5. **Generation**: Creates metadata, checksums, statistics, and isolated search indices (by framework, category, author, tag).
6. **Writer**: Employs the `FileSystemService` to write the finalized registry atomically to disk, ensuring partial failures result in a clean rollback.

## Public API

```python
from engine.registry_builder.service import RegistryBuilderService
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger

logger = DefaultLogger()
fs = FileSystemService(logger)
builder = RegistryBuilderService(logger, fs)

# Transforms raw source into /registry/v1/
builder.build_registry("/path/to/raw/components", "/path/to/registry/v1")
```
