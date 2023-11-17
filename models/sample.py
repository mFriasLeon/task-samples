"""Naralabs task: Managing samples.

In FastAPI, a model is a data structure that represents the data 
that is being sent or received over the API.

"""

from pydantic import BaseModel
from typing import Optional

class SampleRequest(BaseModel):
    """Class to model Sample
    """
    monitored_id : int
    sample_name : str
    diagnosis: str
    date: str
    tissue_size : int


class SampleResponse(BaseModel):
    """Class to model Sample
    """
    id: str
    monitored_id : int
    sample_name : str
    diagnosis: str
    date: str
    tissue_size : int

