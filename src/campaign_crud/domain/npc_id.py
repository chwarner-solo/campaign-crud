import uuid
from dataclasses import dataclass

@dataclass(frozen=True)
class NPCID:
    """NPC identifier"""
    value: uuid.UUID

    @classmethod
    def new(cls):
        """Generate a new NPCID"""
        return cls(uuid.uuid4())

    def __str__(self):
        return str(self.value)
