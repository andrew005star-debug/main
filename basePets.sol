// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract SimpleStorage {

    struct Pets {
    string master_name;
    string Pets_name;
    }

    Pets[] public base_Pets;

    function addPet(string memory _master_name, string memory _Pets_name) public {
        base_Pets.push(Pets(_master_name, _Pets_name));
    }
}