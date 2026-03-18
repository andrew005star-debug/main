// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;
import {SimpleStorage} from "./SimpleStorage.sol";

contract Squared is SimpleStorage {
    function store(uint256 _newFavNumber) public override {
    myFavoriteNumber = _newFavNumber * _newFavNumber;
    }
}