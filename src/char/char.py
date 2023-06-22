import asyncio
import os
import random
from uuid import UUID, uuid4
from typing import Literal, Optional, Type, cast
from pydantic import BaseModel


class Char(BaseModel):
    id: UUID
    full_name: str
    bio: str


    def __init__(
        self,
        full_name: str,
        bio: str,
        id: Optional[str | UUID] = None,
        ):
        if id is None:
            id = uuid4()

