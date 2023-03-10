from sqlmodel import Field, SQLModel


class Hero(SQLModel, table=True):
    __tablename__ = "hero"
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
