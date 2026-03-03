# src/config/settings.py
"""Central config loader — every module reads from config.yaml through here."""
from pathlib import Path
from typing import Any, Dict
import yaml

BASE_DIR = Path(__file__).parent.parent.parent          # project root
DEFAULT_CONFIG_PATH = BASE_DIR / "config.yaml"

_cache: Dict[str, Any] = {}


def load_config(yaml_path: Path = DEFAULT_CONFIG_PATH) -> Dict[str, Any]:
    """Load and cache the YAML config (one disk read per path)."""
    key = str(yaml_path)
    if key not in _cache:
        if yaml_path.exists():
            with open(yaml_path) as f:
                _cache[key] = yaml.safe_load(f) or {}
        else:
            _cache[key] = {}
    return _cache[key]


def resolve_path(raw: Any, base: Path = BASE_DIR) -> Path:
    """Turn a config value into an absolute Path (relative paths resolve
    against the project root)."""
    p = Path(raw)
    return p if p.is_absolute() else base / p
