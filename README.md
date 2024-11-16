### Decentralized Password Blacklist System

#### Introduction
This decentralized password blacklist aims to help organizations keep track of compromised or weak passwords without sharing private information. This solution leverages blockchain technology to maintain a decentralized record of password hashes, ensuring that organizations can securely contribute to a common blacklist and verify the safety of passwords.

#### Features
- **Password Hashing**: Passwords are hashed using SHA-256 before being added to the blockchain.
- **Blockchain-Based Record**: Uses a smart contract to store the password hashes, ensuring immutability and security.
- **Privacy Preservation**: Organizations can add passwords and verify against the blacklist without sharing any actual passwords.
- **Decentralized Ledger**: Multiple organizations can contribute to and access the blacklist without a central authority.

#### Usage Instructions
1. **Setup Dependencies**: Install the required Python packages using `pip`.
    ```sh
    pip install web3 solcx
    ```
2. **Install Ganache**: Use Ganache to run a local Ethereum blockchain for testing purposes.
3. **Run the Script**: Start the script to interact with the decentralized blacklist.
    ```sh
    python decentralized_password_blacklist.py
    ```
4. **Options Available**:
   - **Add a Password to the Blacklist**: Hash the password and store it in the blockchain.
   - **Check if a Password is Compromised**: Check the hashed password against the existing blacklist.

#### Prerequisites
- **Python 3.6 or above**: Ensure you have Python installed in your system.
- **Ganache**: Run a local blockchain environment with Ganache.
- **Solidity Compiler (solcx)**: Used to compile the Solidity smart contract.

#### How It Works
1. **Smart Contract Deployment**: The smart contract is written in Solidity and deployed to the local Ethereum blockchain using the Web3 library.
2. **Password Hashing**: Passwords are hashed using SHA-256 before being submitted to the blockchain, ensuring that no plaintext passwords are shared.
3. **Check Passwords**: Organizations can check if a password has been compromised without accessing the actual passwords of other organizations.

#### Implementation Steps
1. **Clone Repository**: Clone this repository from GitHub.
2. **Install Dependencies**: Use the command `pip install -r requirements.txt` to install all necessary dependencies.
3. **Run Ganache**: Run Ganache and ensure it's listening on `http://127.0.0.1:8545`.
4. **Run the Tool**: Run the Python script using `python decentralized_password_blacklist.py` to interact with the blacklist.

#### Contributing
If you find bugs or have suggestions for improvements, feel free to contribute by opening an issue or making a pull request.

#### License
This project is open-source and licensed under the MIT License.

#### Disclaimer
This project is intended for educational purposes only. Users are responsible for ensuring they comply with applicable laws and regulations before using or modifying the decentralized password blacklist system.
