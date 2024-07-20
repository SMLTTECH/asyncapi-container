from pydantic import BaseModel, Field

from asyncapi_container.asyncapi.spec.v3.external_docs import ExternalDocs


class Tag(BaseModel):
    """ Allows adding meta data to a single tag."""
    name: str = Field(..., description="The name of the tag.")
    description: str = Field(
        default="",
        description="A short description for the tag. "
                    "CommonMark syntax can be used for rich text representation."
    )
    external_docs: ExternalDocs = Field(
        default=ExternalDocs(url=""),
        alias="externalDocs",
        description="Additional external documentation for this tag.",
    )

    class Config:
        frozen = True

