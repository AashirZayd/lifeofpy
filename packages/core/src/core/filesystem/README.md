# LifeOfPy Core Filesystem API

The `core.filesystem` module enforces safety, atomicity, and testability across all file operations in the LifeOfPy ecosystem.

## Why is direct OS access prohibited?
Calling `open()`, `shutil`, or `pathlib` directly leads to partially corrupted states during failed installations. The `FileSystemService` ensures that operations like copying or writing are 100% reversible via the `transaction()` context manager.

## Usage

```python
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger

logger = DefaultLogger()
fs = FileSystemService(logger)

# Atomic Write
fs.write_text_atomic("/path/to/manifest.json", '{"id": "button-01"}')

# Transaction with Automatic Rollback
try:
    with fs.transaction() as tx:
        fs.copy("/src/button-01", "/dst/components/ui")
        fs.delete("/dst/components/ui/old-button")
        # Any exception raised here automatically restores the deleted button and removes the copied directory.
except Exception as e:
    logger.error(f"Failed to install component: {e}")
```
