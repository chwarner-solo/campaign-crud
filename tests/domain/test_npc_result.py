from returns.result import Success, Failure
from campaign_crud.domain.npc import NPC
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.errors import NPCError

def test_create_valid_npc():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    result = NPC.create("Giant Spider", block)
    assert isinstance(result, Success)
    assert result.unwrap().name == "Giant Spider"

def test_create_npc_invalid_name():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    result = NPC.create("", block)
    assert isinstance(result, Failure)
    assert isinstance(result.failure(), NPCError)
    assert result.failure().message == "NPC requires a name"




