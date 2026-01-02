from uuid import UUID

from fastapi import APIRouter, HTTPException, Depends
from returns.result import Success, Failure

from campaign_crud.application.npc.create_npc import CreateNPCUseCase
from campaign_crud.application.npc.get_npc import GetNPCUseCase
from campaign_crud.application.npc.get_all_npcs import GetAllNPCsUseCase
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.npc_id import NPCID
from .dependencies import get_create_npc_use_case, get_get_npc_use_case, get_get_all_npcs_use_case
from .npc_dto import NPCResponse

router = APIRouter(prefix="/npcs", tags=["npcs"])

@router.post("/")
def create_npc(name: str, create_use_case: CreateNPCUseCase = Depends(get_create_npc_use_case)):
    block = StatBlock.create(name, 14, 26).unwrap()
    result = create_use_case.execute(name, stat_block=block)

    match result:
        case Success(npc):
            return NPCResponse.from_npc(npc)
        case Failure(error):
            raise HTTPException(status_code=400, detail=error.message)

@router.get("/")
def get_all_npcs(get_all_npcs_use_case: GetAllNPCsUseCase = Depends(get_get_all_npcs_use_case)):
    result = get_all_npcs_use_case.execute()

    match result:
        case Success(npcs):
            return [NPCResponse.from_npc(npc) for npc in npcs]
        case Failure(error):
            raise HTTPException(status_code=500, detail=error.message)

@router.get("/{npc_id}")
def get_npc(npc_id: str, get_use_case: GetNPCUseCase = Depends(get_get_npc_use_case)):
    result = get_use_case.execute(NPCID(UUID(npc_id)))

    match result:
        case Success(npc):
            if npc is None:
                raise HTTPException(status_code=404, detail="NPC not found")
            return NPCResponse.from_npc(npc)
        case Failure(error):
            raise HTTPException(status_code=500, detail=error.message)
