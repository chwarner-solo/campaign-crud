from enum import Enum
from dataclasses import dataclass


@dataclass()
class DomainError:
    """Base domain error"""
    message: str

@dataclass()
class StatBlockError(DomainError):
    """StatBlock validation error"""
    pass

@dataclass()
class NPCError(DomainError):
    """NPC validation error"""
    pass

@dataclass()
class RepositoryError(DomainError):
    """Wraps persistance layer errors"""
    pass