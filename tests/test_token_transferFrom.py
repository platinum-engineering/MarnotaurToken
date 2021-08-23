import pytest
import logging
from brownie import Wei, reverts
LOGGER = logging.getLogger(__name__)



def test_marnotour_main_props(accounts, token20):
    assert token20.balanceOf(accounts[0]) == token20.MAX_SUPPLY()
    assert token20.name() == "Marnotaur"
    assert token20.symbol() == "TAUR"


def test_marnotour_transferFrom(accounts, token20):
    token20.transfer(accounts[1], 1, {"from": accounts[0]})
    with reverts("ERC20: transfer amount exceeds allowance"):
        token20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[2]})
    token20.approve(accounts[0], 1, {"from": accounts[1]})    
    token20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[0]})
    assert token20.balanceOf(accounts[1]) == 0
    assert token20.balanceOf(accounts[2]) == 1

    #minter
    token20.transfer(accounts[1], 1, {"from": accounts[0]})
    token20.approve(accounts[2], 1, {"from": accounts[1]})
    token20.transferFrom(accounts[1], accounts[2], 1, {"from": accounts[2]})
    assert token20.balanceOf(accounts[1]) == 0
    assert token20.balanceOf(accounts[2]) == 2

    token20.approve(accounts[3], 1, {"from": accounts[1]})
    with reverts("ERC20: transfer amount exceeds balance"):
        token20.transferFrom(accounts[1], accounts[3], 1, {"from": accounts[3]})


