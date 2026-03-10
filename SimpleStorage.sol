// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;
contract SimpleStorage {

    uint256 public favoriteNumber; // storage variable: it's stored in a section of the blockchain called "Storage"
    uint256[] list_of_favorite_numbers;

    struct Person {
    uint256 my_favorite_number;
    string name;
    }

    Person[] public list_of_people; // this is a dynamic array

    function store(uint256 _favoriteNumber) public {
        // the variable favorite number is updated with the value that is contained into the parameter `_favoriteNumber`
        favoriteNumber = _favoriteNumber;
    }
    
    function retrieve() public view returns(uint256) {
    return favoriteNumber;
    }

    function add_person(string memory _name, uint256 _favorite_number) public {
    list_of_people.push(Person(_favorite_number, _name));
    }

    Person public my_friend = Person(7, 'Pat');
/* equals to
Person public my_friend = Person({
    favorite_number:7,
    name:'Pat'});
*/
}