require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

module.exports = {
  solidity: "0.8.18",  // Make sure the version matches the one in your Solidity file
  networks: {
    hardhat: {},  // Local development network
    goerli: {  // Replace with the test network you're using
      url: process.env.GOERLI_URL,  // Your Alchemy or Infura API URL
      accounts: [process.env.PRIVATE_KEY]  // Your private key
    }
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY  // API key for verifying contracts
  }
};
