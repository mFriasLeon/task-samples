"""Naralabs task: Managing sample.

To avoid repeating code in routers files and functions, it a good idea 
use decorators because allow you to factor out common functionality and apply 
it to multiple functions or classes. 
In exceptions file will use decorators to avoid repeating HTTPExceptions in each API function.
"""


#from email.mime import message
from functools import wraps
from fastapi import HTTPException
import constants.messages as messages

def raise_exception_404(function):
    """Decorators function to raise exception 404

    Args:
        function: GET api function

    Raises:
        HTTPException: exception 404 

    """

    @wraps(function)
    async def wrapper(*args, **kwargs):
        result = await function(*args, **kwargs)
        if result:
            return result
        else:
            raise HTTPException(status_code = 404, detail = messages.NOT_FOUND)

    return wrapper

def raise_exception_400(function):
    """Decorators function to raise exception 400

    Args:
        function: POST api function

    Raises:
        HTTPException: exception 400

    Returns:
        dictionary: return dictionary message
    """

    @wraps(function)
    async def wrapper(*args, **kwargs):
        success = await function(*args, **kwargs)
        if success:
            return {"message": messages.CREATED}
        else:
            raise HTTPException(status_code = 400, detail = messages.FAIL)

    return wrapper
