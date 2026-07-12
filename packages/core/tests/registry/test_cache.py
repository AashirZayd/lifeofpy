import pytest
import time
from core.registry.cache import RegistryCache
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger


@pytest.fixture
def cache(tmp_path):
    logger = DefaultLogger()
    fs = FileSystemService(logger)
    cache_dir = tmp_path / "cache"
    return RegistryCache(fs, logger, cache_dir, ttl=1)


def test_cache_set_and_get(cache):
    cache.set("key1", {"data": "test"})
    assert cache.get("key1") == {"data": "test"}


def test_cache_miss(cache):
    assert cache.get("missing_key") is None


def test_cache_expiry(cache):
    cache.set("key2", "value")
    time.sleep(1.1)
    assert cache.get("key2") is None
