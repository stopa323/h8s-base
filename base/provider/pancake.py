from typing import List

from base.db import pancake as db
from base.schema import pancake as api


def list_pancakes() -> List[db.PancakeTypeObj]:
    db_objects = db.PancakeTypeObj.objects
    return list(db_objects)


def create_pancake_type(pancake_type: api.PancakeType) -> db.PancakeTypeObj:
    pancake_db = db.PancakeTypeObj(**pancake_type.dict())
    pancake_db.save()
    return pancake_db
