from pydantic import BaseModel, Field, ConfigDict


class Base(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        use_enum_values=True,
        validate_assignment=True,
        strict=True,
        validate_default=True,
    )

class Pet(Base):
    # "code": 0,
    # "type": "string",
    # "message": "string"
    id: int
    name: str
    status: str
