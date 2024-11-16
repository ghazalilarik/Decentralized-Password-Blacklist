import hashlib
import json
from hashlib import sha256
import os
from web3 import Web3

# Setup Web3 connection (local Ganache or private Ethereum network)
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Smart Contract Source Code (Solidity)
contract_source_code = '''
pragma solidity ^0.8.0;

contract PasswordBlacklist {
    mapping(bytes32 => bool) private compromisedPasswords;

    function addPassword(bytes32 passwordHash) public {
        compromisedPasswords[passwordHash] = true;
    }

    function isPasswordCompromised(bytes32 passwordHash) public view returns (bool) {
        return compromisedPasswords[passwordHash];
    }
}
'''

# Compile and deploy contract (using local Web3 connection)
import solcx
solcx.install_solc("0.8.0")
compiled_sol = solcx.compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:PasswordBlacklist']

# Deploy contract
web3.eth.default_account = web3.eth.accounts[0]
PasswordBlacklist = web3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])
tx_hash = PasswordBlacklist.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
contract_address = tx_receipt.contractAddress
password_blacklist_contract = web3.eth.contract(address=contract_address, abi=contract_interface['abi'])

# Function to hash the password using SHA-256
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Add password to decentralized blacklist
def add_password_to_blacklist(password):
    password_hash = hash_password(password)
    tx_hash = password_blacklist_contract.functions.addPassword(web3.toBytes(hexstr=password_hash)).transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Password hash {password_hash} added to blacklist.")

# Check if password is compromised
def is_password_compromised(password):
    password_hash = hash_password(password)
    is_compromised = password_blacklist_contract.functions.isPasswordCompromised(web3.toBytes(hexstr=password_hash)).call()
    return is_compromised

if __name__ == "__main__":
    print("Decentralized Password Blacklist System")

    while True:
        print("\nOptions:")
        print("1. Add a password to the blacklist")
        print("2. Check if a password is compromised")
        print("3. Exit")
        
        option = input("Enter your choice: ")
        if option == '1':
            password = input("Enter the password to blacklist: ")
            add_password_to_blacklist(password)
        elif option == '2':
            password = input("Enter the password to check: ")
            is_compromised = is_password_compromised(password)
            if is_compromised:
                print("This password is compromised!")
            else:
                print("This password is safe.")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")
