// SPDX-License-Identifier: MIT
// Platinum devTeam.
pragma solidity 0.8.6;

import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";

contract Marnotaur is ERC20 {

    uint256 constant public MAX_SUPPLY = 150_000_000e18;

    constructor(address initialKeeper)
    ERC20("Marnotaur Governance v1", "TAUR")
    { 
        _mint(initialKeeper, MAX_SUPPLY);
    }
}