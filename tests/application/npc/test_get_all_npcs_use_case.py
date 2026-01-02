from campaign_crud.application.npc.get_all_npcs import GetAllNPCsUseCase
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.npc import NPC
from tests.doubles.in_memory_npc_repository import InMemoryNPCRepository

def test_get_all_npcs_empty():
    respository = InMemoryNPCRepository()
    use_case = GetAllNPCsUseCase(respository)

    result = use_case.execute()
    npcs = result.unwrap()
    assert npcs == []

def test_Get_all_npcs_returns_all():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    repository = InMemoryNPCRepository()

    npc1 = NPC.create("Attercop", block).unwrap()
    npc2 = NPC.create("Shelob", block).unwrap()

    repository.save(npc1)
    repository.save(npc2)

    use_case = GetAllNPCsUseCase(repository)
    result = use_case.execute()

    npcs = result.unwrap()
    assert len(npcs) == 2
    assert npc1 in npcs
    assert npc2 in npcs