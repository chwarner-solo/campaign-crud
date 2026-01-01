from campaign_crud.domain.npc_id import NPCID
import uuid


def test_create_npc_id_From_uuid():
    test_uuid = uuid.uuid4()
    npc_id = NPCID(test_uuid)
    assert npc_id.value == test_uuid

def test_npc_id_generates_new_uuid():
    npc_id = NPCID.new()
    assert isinstance(npc_id.value, uuid.UUID)

def test_npc_id_string_representation():
    test_uuid = uuid.uuid4()
    npc_id = NPCID(test_uuid)
    assert str(npc_id) == str(test_uuid)

def test_npc_id_equality():
    test_uuid = uuid.uuid4()
    id1 = NPCID(test_uuid)
    id2 = NPCID(test_uuid)
    assert id1 == id2

def test_npc_id_inequality():
    id1 = NPCID.new()
    id2 = NPCID.new()
    assert id1 != id2

def test_npc_id_hashable():
    npc_id = NPCID.new()
    id_set = {npc_id}
    assert npc_id in id_set