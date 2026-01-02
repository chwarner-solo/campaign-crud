from abc import ABC, abstractmethod
from returns.result import Result
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.npc_id import NPCID
from campaign_crud.domain.errors import RepositoryError

class NPCRepository(ABC):
    """Port: abstracts persistance for NPCs"""

    @abstractmethod
    def save(self, npc: NPC) -> Result[NPC, RepositoryError]:
        """Save an NPC and return it"""

    def get(self, npc_id: NPCID) -> Result[NPC, RepositoryError]:
        """Get an NPC by id"""
        pass

    def get(self) -> Result[list[NPC], RepositoryError]:
        """Get all NPCs"""
        pass