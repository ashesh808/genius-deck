from abc import ABC, abstractmethod

class IDataMapper(ABC):
    """
    An abstract base class (interface) for data mappers.
    """

    @abstractmethod
    def model_to_entity(self, model_instance):
        """
        Convert a model instance to an entity object.
        """
        pass

    @abstractmethod
    def entity_to_model(self, entity, existing=None):
        """
        Convert an entity object to a model instance.
        """
        pass