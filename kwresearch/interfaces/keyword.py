import time
from typing import List

from pydantic import BaseModel


class Keyword(BaseModel):
    keyword: str
    difficulty: float
    volume: int
    organic_ctr: float
    priority: float

    def __str__(self):
        return self.keyword

class RelatedKeywords(BaseModel):
    keyword: str
    location: str
    device: str
    engine: str
    related_keywords: List[Keyword]

    created_at: int = int(time.time())

    def __str__(self):
        return self.keyword
    
    def __iter__(self):
        return iter(self.related_keywords)