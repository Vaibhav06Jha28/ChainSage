// vulnerable_contract.sol
// ⚠️ This contract contains a classic Reentrancy vulnerability.
// Do NOT deploy on mainnet without fixing it.

pragma solidity ^0.8.0;

contract Reentrancy {
    mapping(address => uint) public balances;

    // Deposit ETH into the contract
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Withdraw user balance — vulnerable to reentrancy!
    function withdraw(uint amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // 🔴 Vulnerable call: External call made before state change
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Transfer failed");

        // State update AFTER external call — the vulnerability
        balances[msg.sender] -= amount;
    }
}
