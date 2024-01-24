import abc

from attr import define


@define
class AsyncAPISpecGenerator(abc.ABC):
    """ Generate asyncapi spec definition from our core container. """

    @abc.abstractmethod
    def as_dict(self) -> dict:
        ...

