from pathlib import Path

from ultralytics import YOLO
from typing import Dict


# Project root (one level above the `app` package), so model paths resolve
# correctly no matter which directory the server is launched from.
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Prefix for YOLO model file paths
YOLO_MODEL_PREFIX = PROJECT_ROOT / "models" / "yolo11"

MODEL_PATHS = {
    "n": f"{YOLO_MODEL_PREFIX}n.pt",
    "s": f"{YOLO_MODEL_PREFIX}s.pt",
    "m": f"{YOLO_MODEL_PREFIX}m.pt",
}


def load_models() -> Dict[str, YOLO]:
    """
    Load YOLO models from disk and return them in a dictionary.

    Returns:
        dict[str, YOLO]: Dictionary of models keyed by type ("n", "s", "m")
    """
    models = {}
    for model_type, path in MODEL_PATHS.items():
        models[model_type] = YOLO(path)
    return models
