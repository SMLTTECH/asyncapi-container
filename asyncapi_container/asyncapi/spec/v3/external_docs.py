from pydantic import BaseModel, Field


class ExternalDocs(BaseModel):
    """ Allows referencing an external resource for extended documentation. """
    description: str = Field(
        default="",
        description="A short description of the target documentation. "
                    "CommonMark syntax can be used for rich text representation."
    )
    url: str = Field(
        ...,
        description="REQUIRED. "
                    "The URL for the target documentation. This MUST be in the form of an absolute URL."
    )

    class Config:
        frozen = True
