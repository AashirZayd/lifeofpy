import json
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Config:
    registryVersion: str
    experimentalFeatures: bool
    defaultFramework: str
    
def load_config(path: str | Path = "lifeofpy.json") -> Config:
    path = Path(path)
    if not path.exists():
        return Config("v1", False, "customtkinter")
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    return Config(
        registryVersion=data.get("registryVersion", "v1"),
        experimentalFeatures=data.get("experimentalFeatures", False),
        defaultFramework=data.get("defaultFramework", "customtkinter")
    )
