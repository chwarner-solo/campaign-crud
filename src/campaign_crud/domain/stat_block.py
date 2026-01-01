from returns.result import Result, Success, Failure

from .errors import StatBlockError

class StatBlock:
    def __init__(self, name: str, ac: int, hp: int):
        self.name = name
        self.ac = ac
        self.hp = hp


    @classmethod
    def create(cls, name: str, ac: int, hp: int) -> Result["StatBlock", StatBlockError]:
        if not name or not name.strip():
            return Failure(StatBlockError("StatBlock requires a name"))
        if ac <= 0 or hp <= 0:
            return Failure(StatBlockError("AC and HP must be positive"))
        return Success(StatBlock(name, ac, hp))
