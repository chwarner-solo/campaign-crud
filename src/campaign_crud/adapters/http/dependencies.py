from fastapi import Depends

from campaign_crud.application.npc.create_npc import CreateNPCUseCase
from campaign_crud.application.npc.get_npc import GetNPCUseCase
from campaign_crud.application.npc.get_all_npcs import GetAllNPCsUseCase
from tests.doubles.in_memory_npc_repository import InMemoryNPCRepository

_repository = InMemoryNPCRepository()

def get_repository():
    return _repository

def get_create_npc_use_case(repo=Depends(get_repository)) -> CreateNPCUseCase:
    return CreateNPCUseCase(repo)

def get_get_npc_use_case(repo=Depends(get_repository)) -> GetNPCUseCase:
    return GetNPCUseCase(repo)

def get_get_all_npcs_use_case(repo=Depends(get_repository)) -> GetAllNPCsUseCase:
    return GetAllNPCsUseCase(repo)