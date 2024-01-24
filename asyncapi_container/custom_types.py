from typing import Dict, List, Type

from pydantic import BaseModel

TopicName = str
RoutingMap = Dict[TopicName, List[Type[BaseModel]]]
