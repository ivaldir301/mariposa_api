from pydantic import RootModel
from typing import Any, Dict

class DynamicModel(RootModel):
    root: Dict[str, Any]

