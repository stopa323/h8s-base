from pydantic import BaseModel, Field


class PancakeTypeCreate(BaseModel):
    name: str = Field(...,
                      title="Juicy Pancake type")
    description: str = Field("No description so far...",
                             title="Catchy description",
                             max_length=500)

    class Config:
        orm_mode = True

        schema_extra = {
            "description": "Object for creating Pancake type",
            "example": {
                "name": "BananaPancake",
                "description": "World-class, 5-star, Gordon Ramsay-approved, "
                               "Banana pancake."}}


class PancakeType(PancakeTypeCreate):
    id: str = Field(...,
                    title="Unique pancake type Id")

    class Config:
        orm_mode = True

        schema_extra = {
            "description": "Serialized Pancake type database object",
            "example": {
                "id": "00000000-0000-0000-0000-000000000001",
                "name": "BananaPancake",
                "description": "World-class, 5-star, Gordon Ramsay-approved, "
                               "Banana pancake."}}


