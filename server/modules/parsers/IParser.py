from abc import ABC, abstractmethod

class IParser(ABC):
    """Interface for parser classes."""

    @abstractmethod
    def parse(self) -> str:
        """Parse the file located at the given file path.

        Args:
            file_path (str): The path to the file to be parsed.

        Returns:
            str: The parsed content of the file.
        """
        pass
