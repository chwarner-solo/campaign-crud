from campaign_crud.application.npc.get_npc import GetNPCUseCase
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.npc import NPC
from tests.doubles.in_memory_npc_repository import InMemoryNPCRepository

def test_get_npc_by_id_success():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    repository = InMemoryNPCRepository()

    created_npc = NPC.create("Attercop", block).unwrap()
    repository.save(created_npc)

    use_case = GetNPCUseCase(repository)
    result = use_case.execute(created_npc.id)

    npc = result.unwrap()
    assert npc.name == "Attercop"
    assert npc.id == created_npc.id

def test_get_npc_not_found():
    repository = InMemoryNPCRepository()
    use_case = GetNPCUseCase(repository)

    from campaign_crud.domain.npc_id import NPCID
    result = use_case.execute(NPCID.new())

    npc = result.unwrap()
    assert npc is None