from returns.result import Success, Failure
from campaign_crud.domain.stat_block import StatBlock
from campaign_crud.domain.errors import StatBlockError



def test_create_valid_stat_block():
    result = StatBlock.create("Giant Spider", 14, 26)
    assert isinstance(result, Success)
    assert result.unwrap().name == "Giant Spider"

def test_create_state_block_invalid_name():
    result = StatBlock.create("", 14, 26)
    assert isinstance(result, Failure)
    assert isinstance(result.failure(), StatBlockError)
    assert result.failure().message == "StatBlock requires a name"


def test_create_state_block_invalid_ac():
    result = StatBlock.create("Giant Spider", -1, 26)
    assert isinstance(result, Failure)
    assert isinstance(result.failure(), StatBlockError)
    assert result.failure().message == "AC and HP must be positive"

def test_create_state_block_invalid_hp():
    result = StatBlock.create("Giant Spider", 14, -1)
    assert isinstance(result, Failure)
    assert isinstance(result.failure(), StatBlockError)
    assert result.failure().message == "AC and HP must be positive"
