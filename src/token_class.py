from enum import Enum
from dataclasses import dataclass


class ValidTokens(Enum):
    SPACE_TOKEN = 0
    CHAR_TOKEN = 1
    FUNC_TOKEN = 3
    KWD_TOKEN = 4


@dataclass
class Token:
    string: str
    token_type: ValidTokens 