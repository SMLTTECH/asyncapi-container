from pydantic import BaseModel, Field

from asyncapi_container.asyncapi.spec.v3.info import Info
from asyncapi_container.asyncapi.spec.v3.tag import Tag
from asyncapi_container.custom_types import RoutingMap


class TopicV3(BaseModel):
    """
    Simplified version of AsyncAPI channel used as topic.
    """

    address: str | None = Field(
        default=None,
        title="My Project",
        version="0.0.1",
        description='An optional string representation of this channel\'s address. '
                    'The address is typically the "topic name", "routing key", '
                    '"event type", or "path". When null or absent, '
                    'it MUST be interpreted as unknown. '
                    'This is useful when the address is generated dynamically at runtime or can\'t '
                    'be known upfront. It MAY contain Channel Address Expressions. '
                    'Query parameters and fragments SHALL NOT be used, instead use bindings to define them.'
    )
    title: str = Field(
        default="",
        description="A human-friendly title for the channel.",
    )
    summary: str = Field(
        default="",
        description="A short summary of the channel.",
    )
    description: str = Field(
        default="",
        description="An optional description of this channel. "
                    "CommonMark syntax can be used for rich text representation."
    )
    tags: list[Tag] | None = Field(
       default=None,
       description="A list of tags for logical grouping of channels.",
    )

    def __hash__(self):
        # Pydantic models with list attributes can't ba hashable.
        # Let's change them to tuples on the fly to make hashable
        values = self.__dict__.values()
        hashable_values = []
        for value in values:
            if isinstance(value, list):
                hashable_value = tuple(value)
                hashable_values.append(hashable_value)

        return hash((type(self),) + tuple(hashable_values))

    class Config:
        arbitrary_types_allowed = True
