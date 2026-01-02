from returns.result import Result
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.npc_id import NPCID
from campaign_crud.domain.errors import RepositoryError
from campaign_crud.ports.npc_repository import NPCRepository

class GetNPCUseCase:
    def __init__(self, repository: NPCRepository):
        self.repository = repository

    def execute(self, npc_id: NPCID) -> Result[NPC | None, RepositoryError]:
        """Get an NPC by ID"""
        return self.repository.get(npc_id)
