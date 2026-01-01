from returns.result import Result, Failure, Success

from .errors import NPCError

from .stat_block import StatBlock

class NPC:
    def __init__(self, name: str, stat_block: StatBlock):
        self.name = name
        self.stat_block = stat_block

    @classmethod
    def create(cls, name: str, stat_block: StatBlock) -> Result["NPC", str]:
        if not name or not name.strip():
            return Failure(NPCError("NPC requires a name"))
        if not stat_block:
            return Failure(NPCError("NPC requires a stat block"))
        return Success(NPC(name, stat_block))

    @property
    def armor_class(self):
        return self.stat_block.ac

    @property
    def hit_points(self):
        return self.stat_block.hp