from returns.result import Result, Success
from campaign_crud.ports.npc_repository import NPCRepository
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.npc_id import NPCID
from campaign_crud.domain.errors import DomainError

class InMemoryNPCRepository(NPCRepository):
    def __init__(self):
        self.npcs: dict[NPCID, NPC] = {}

    def save(self, npc: NPC) -> Result[NPC, DomainError]:
        self.npcs[npc.id] = npc
        return Success(npc)

    def get(self, npc_id: NPCID) -> Result[NPC, DomainError]:
        return Success(self.npcs[npc_id])
