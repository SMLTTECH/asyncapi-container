import abc

from attr import define

from asyncapi_container.asyncapi.spec.v3.root import AsyncAPIV3Root


@define
class AsyncAPISpecGenerator(abc.ABC):
    """ Generate asyncapi spec definition from our core container. """

    @abc.abstractmethod
    def parse_spec_container(self) -> AsyncAPIV3Root:
        ...

    @abc.abstractmethod
    def as_dict(self) -> dict:
        ...

    @abc.abstractmethod
    def as_json(self) -> dict:
        ...
