from pydantic import BaseModel


class Info(BaseModel):
    """Asyncapi Included information about your project."""

    title: str = "My Project"
    version: str = "0.0.1"
    description: str = ""

