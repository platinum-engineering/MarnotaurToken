import pytest

@pytest.fixture(scope="module")
def token20(accounts, Marnotaur):
    erc20 = accounts[0].deploy(Marnotaur, accounts[0])
    yield erc20 


