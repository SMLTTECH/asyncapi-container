from pydantic import BaseModel

from asyncapi_container.asyncapi.spec.v3.info import Info


class AsyncAPIV3Root(BaseModel):
    asyncapi: str = "3.0.0"
    info: Info = Info()
    # introduce types in the future
    channels: dict
    components: dict
    operations: dict
