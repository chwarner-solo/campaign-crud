from dataclasses import dataclass

from campaign_crud.domain.npc import NPC

@dataclass()
class NPCResponse:
    id: str
    name: str
    ac: int
    hp: int

    @classmethod
    def from_npc(cls, npc: NPC):
        return cls(
            id=str(npc.id),
            name=npc.name,
            ac=npc.stat_block.ac,
            hp=npc.stat_block.hp,
        )

@dataclass()
class ErrorResponse:
    error:str