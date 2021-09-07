// SPDX-License-Identifier: MIT
// Platinum devTeam.
pragma solidity 0.8.6;

import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/token/ERC20/ERC20.sol";
import "OpenZeppelin/openzeppelin-contracts@4.2.0/contracts/access/Ownable.sol";

contract sMarnotaur is ERC20, Ownable {

    uint256 constant public INITIAL_SUPPLY = 212_766e18;

    constructor()
    ERC20("Synthetic Marnotaur", "sTAUR")
    { 
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);   
    }
}