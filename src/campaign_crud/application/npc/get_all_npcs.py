from returns.result import Result
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.errors import RepositoryError
from campaign_crud.ports.npc_repository import NPCRepository

class GetAllNPCsUseCase:
    def __init__(self, repository: NPCRepository):
        self.repository = repository

    def execute(self) -> Result[list[NPC], RepositoryError]:
        """Get all NPCs"""
        return self.repository.get_all()