from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, PositiveFloat, PositiveInt


class MatchFormat(str, Enum):
    TEST = "TEST"
    ODI = "ODI"
    T20 = "T20"


class Metadata(BaseModel):
    match_url: str
    batting: str
    bowling: str
    format: MatchFormat
    inning: PositiveInt


class CommentaryItem(BaseModel):
    ball: PositiveFloat
    event: str
    text: str
    additional_text: Optional[str] = None


class OverData(BaseModel):
    over_number: PositiveInt
    commentary: List[CommentaryItem]


class RawCommentaryData(BaseModel):
    metadata: Optional[Metadata] = None
    over_data: Optional[OverData] = None
