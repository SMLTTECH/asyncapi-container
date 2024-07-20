from typing import Dict, List

from pydantic import BaseModel, Field

from asyncapi_container.asyncapi.spec.v3.info import Info
from asyncapi_container.custom_types import RoutingMap, TopicName



class SimpleSpecV3(BaseModel):
    """
    Simplified version of AsyncAPI specification mapper.
    Doesn't require to understand and use the whole asyncapi specification
    allowing focus only on producers and consumers.
    """

    info: Info = Info(title="My Project", version="0.0.1", description="")
    sends: RoutingMap  = Field(default={}, description="What your service can send. Acting as producer.")
    receives: RoutingMap = Field(default={}, description="What your service can receive. Acting as consumer.")

    class Config:
        arbitrary_types_allowed = True
