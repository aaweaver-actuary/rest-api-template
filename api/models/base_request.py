from abc import ABC, abstractmethod
from pydantic import BaseModel

class BaseRequest(ABC, BaseModel):
    """Parent class for all Requests. All concrete Request models should subclass this class.""" 
