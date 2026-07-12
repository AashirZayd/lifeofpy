import pytest
from pathlib import Path
from core.filesystem.service import FileSystemService
from core.logging.logger import DefaultLogger
from core.exceptions.filesystem import PathNotFoundError, AtomicWriteError, BackupError, RollbackError

@pytest.fixture
def fs():
    logger = DefaultLogger(verbose=True)
    return FileSystemService(logger)

def test_atomic_write_and_read(fs, tmp_path):
    test_file = tmp_path / "test.txt"
    fs.write_text_atomic(test_file, "hello world")
    
    assert fs.exists(test_file)
    assert fs.read_text(test_file) == "hello world"
    assert fs.read_bytes(test_file) == b"hello world"

def test_read_missing(fs, tmp_path):
    with pytest.raises(PathNotFoundError):
        fs.read_text(tmp_path / "missing.txt")

def test_copy_and_delete(fs, tmp_path):
    src = tmp_path / "src.txt"
    dst = tmp_path / "dst.txt"
    fs.write_text_atomic(src, "test")
    
    fs.copy(src, dst)
    assert fs.read_text(dst) == "test"
    
    fs.delete(src)
    assert not fs.exists(src)

def test_transaction_commit(fs, tmp_path):
    f1 = tmp_path / "f1.txt"
    
    with fs.transaction() as tx:
        fs.write_text_atomic(f1, "tx data")
        fs.create_directory(tmp_path / "new_dir")
        
    assert fs.exists(f1)
    assert fs.exists(tmp_path / "new_dir")

def test_transaction_rollback(fs, tmp_path):
    f1 = tmp_path / "f1.txt"
    fs.write_text_atomic(f1, "original")
    
    with pytest.raises(ValueError):
        with fs.transaction() as tx:
            fs.write_text_atomic(f1, "modified")
            fs.create_directory(tmp_path / "rolled_back_dir")
            assert fs.read_text(f1) == "modified"
            raise ValueError("Intentional failure")
            
    # Should rollback to original state
    assert fs.read_text(f1) == "original"
    assert not fs.exists(tmp_path / "rolled_back_dir")

def test_move(fs, tmp_path):
    src = tmp_path / "src_move.txt"
    dst = tmp_path / "dst_move.txt"
    fs.write_text_atomic(src, "moving")
    fs.move(src, dst)
    assert fs.exists(dst)
    assert not fs.exists(src)

def test_is_symlink(fs, tmp_path):
    import os
    src = tmp_path / "src.txt"
    fs.write_text_atomic(src, "symlink target")
    link = tmp_path / "link.txt"
    try:
        os.symlink(src, link)
        assert fs.is_symlink(link)
    except OSError:
        pass # Windows may require admin rights for symlinks

def test_directory_operations(fs, tmp_path):
    dir_path = tmp_path / "test_dir"
    fs.create_directory(dir_path)
    assert fs.exists(dir_path)
    
    fs.write_text_atomic(dir_path / "f.txt", "content")
    
    import core.exceptions.filesystem as exc
    with pytest.raises(exc.FilesystemError):
        fs.delete_directory(dir_path, recursive=False)
        
    fs.delete_directory(dir_path, recursive=True)
    assert not fs.exists(dir_path)
