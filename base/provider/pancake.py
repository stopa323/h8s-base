from typing import List

from base.db import pancake


def list_pancakes() -> List[pancake.PancakeType]:
    db_objects = pancake.PancakeType.objects
    return list(db_objects)
