from returns.result import Result, Failure
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.errors import NPCError, RepositoryError
from campaign_crud.ports.npc_repository import NPCRepository

class CreateNPCUseCase:
    def __init__(self, npc_repository: NPCRepository):
        self.npc_repository = npc_repository

    def execute(self, name: str, stat_block: StatBlock) -> Result[NPC, NPCError | RepositoryError]:
        """Create and persist an NPC"""
        npc_result = NPC.create(name, stat_block)

        if isinstance(npc_result, Failure):
            return npc_result

        npc = npc_result.unwrap()

        return self.npc_repository.save(npc)