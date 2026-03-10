// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract SimpleStorage {
    mapping (string => uint256 ) public base_balance;
    function addBalance(string memory _address, uint256 _balance) public {
        base_balance[_address] = _balance;
    }
}