from campaign_crud.domain.npc import NPC
from campaign_crud.domain.stat_block import StatBlock

def test_npc_has_id_after_creation():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    npc = NPC.create("Giant Spider", block).unwrap()
    assert npc.id is not None

def test_id_is_unique():
    block = StatBlock.create("Giant Spider", 14, 26).unwrap()
    npc1 = NPC.create("Giant Spider", block).unwrap()
    npc2 = NPC.create("Giant Spider", block).unwrap()
    assert npc1.id != npc2.id