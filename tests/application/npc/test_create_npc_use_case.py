from campaign_crud.application.npc.create_npc import CreateNPCUseCase
from campaign_crud.domain.stat_block import StatBlock
from tests.doubles.in_memory_npc_repository import InMemoryNPCRepository

def test_create_npc_use_case_success():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    repository = InMemoryNPCRepository()
    use_case = CreateNPCUseCase(repository)

    result = use_case.execute("Attercop", stat_block=block)

    npc = result.unwrap()
    assert npc.name == "Attercop"
    assert npc.id is not None
    assert repository.get(npc.id).unwrap() == npc