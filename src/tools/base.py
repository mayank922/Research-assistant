from abc import ABC, abstractmethod

"""
Every Tool calling function must implement execute function
"""

class Tool(ABC):
    
    @abstractmethod
    def execute(self, **kwargs) -> dict:
        """
        Execute the tool with the given arguments.
        Must be implemented by every tool subclass.
        Returns a dict with the tool results.
        """
        pass