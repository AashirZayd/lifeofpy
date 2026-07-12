import importlib
import pkgutil
from typing import Dict, Type
from .frameworks.base import FrameworkAdapter

def discover_frameworks() -> Dict[str, Type[FrameworkAdapter]]:
    """Dynamically loads all framework adapters in the frameworks/ directory."""
    import engine.frameworks as frameworks_pkg
    adapters = {}
    
    for _, module_name, _ in pkgutil.iter_modules(frameworks_pkg.__path__):
        if module_name == "base":
            continue
            
        module = importlib.import_module(f"engine.frameworks.{module_name}")
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, FrameworkAdapter) and attr is not FrameworkAdapter:
                instance = attr()
                adapters[instance.id] = attr
                
    return adapters
