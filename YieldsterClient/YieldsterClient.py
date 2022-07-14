import json
import math

from web3 import Web3

from JavaApiRun import Run
from config import Config


class YieldsterClient:
    yieldster_vault_abi = json.loads(
        '[{ "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": false, "internalType": "string", "name": "message", "type": "string" }], "name": "CallStatus", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": false, "internalType": "address", "name": "masterCopy", "type": "address" }], "name": "ChangedMasterCopy", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": false, "internalType": "address", "name": "account", "type": "address" }], "name": "Paused", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": false, "internalType": "address", "name": "feeAddress", "type": "address" }, { "indexed": false, "internalType": "string", "name": "message", "type": "string" } ], "name": "Response", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "anonymous": false, "inputs": [{ "indexed": false, "internalType": "address", "name": "account", "type": "address" }], "name": "Unpaused", "type": "event" }, { "inputs": [], "name": "APContract", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "name": "assetList", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "account", "type": "address" }], "name": "balanceOf", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_masterCopy", "type": "address" }], "name": "changeMasterCopy", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "decimals", "outputs": [{ "internalType": "uint8", "name": "", "type": "uint8" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "subtractedValue", "type": "uint256" } ], "name": "decreaseAllowance", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "emergencyConditions", "outputs": [{ "internalType": "uint8", "name": "", "type": "uint8" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "emergencyVault", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "eth", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "name": "etherDepositors", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_address", "type": "address" }], "name": "getEtherDepositor", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_tokenAddress", "type": "address" }], "name": "getTokenBalance", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "getVaultNAV", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "addedValue", "type": "uint256" } ], "name": "increaseAllowance", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "name", "outputs": [{ "internalType": "string", "name": "", "type": "string" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "operator", "type": "address" }, { "internalType": "address", "name": "from", "type": "address" }, { "internalType": "uint256[]", "name": "ids", "type": "uint256[]" }, { "internalType": "uint256[]", "name": "values", "type": "uint256[]" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "onERC1155BatchReceived", "outputs": [{ "internalType": "bytes4", "name": "", "type": "bytes4" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "paused", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "strategyBeneficiary", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "strategyPercentage", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "bytes4", "name": "interfaceId", "type": "bytes4" }], "name": "supportsInterface", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "symbol", "outputs": [{ "internalType": "string", "name": "", "type": "string" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "threshold", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "tokenValueInUSD", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "totalSupply", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "from", "type": "address" }, { "internalType": "address", "name": "to", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [{ "internalType": "bool", "name": "", "type": "bool" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "vaultAdmin", "outputs": [{ "internalType": "address", "name": "", "type": "address" }], "stateMutability": "view", "type": "function" }, { "stateMutability": "payable", "type": "receive" }, { "inputs": [{ "internalType": "address", "name": "_mastercopy", "type": "address" }], "name": "upgradeMasterCopy", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_APContract", "type": "address" }], "name": "setAPS", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "toggleEmergencyBreak", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "enableEmergencyExit", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "registerVaultWithAPS", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_APContract", "type": "address" }, { "internalType": "address", "name": "_vaultAdmin", "type": "address" }, { "internalType": "address", "name": "_emergencyVault", "type": "address" } ], "name": "setup", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_owner", "type": "address" }], "name": "transferOwnership", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "uint256[]", "name": "_whiteListGroups", "type": "uint256[]" }], "name": "addWhiteListGroups", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "uint256[]", "name": "_whiteListGroups", "type": "uint256[]" }], "name": "removeWhiteListGroups", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "string", "name": "_tokenName", "type": "string" }, { "internalType": "string", "name": "_symbol", "type": "string" } ], "name": "setTokenDetails", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "uint256", "name": "_slippage", "type": "uint256" }], "name": "setVaultSlippage", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address[]", "name": "_enabledDepositAsset", "type": "address[]" }, { "internalType": "address[]", "name": "_enabledWithdrawalAsset", "type": "address[]" }, { "internalType": "address[]", "name": "_disabledDepositAsset", "type": "address[]" }, { "internalType": "address[]", "name": "_disabledWithdrawalAsset", "type": "address[]" } ], "name": "setVaultAssets", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_vaultAdmin", "type": "address" }], "name": "changeVaultAdmin", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_smartStrategyAddress", "type": "address" }, { "internalType": "uint256", "name": "_type", "type": "uint256" } ], "name": "setVaultSmartStrategy", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "uint256", "name": "_threshold", "type": "uint256" }], "name": "setThreshold", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_tokenAddress", "type": "address" }, { "internalType": "uint256", "name": "_amount", "type": "uint256" } ], "name": "deposit", "outputs": [], "stateMutability": "payable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_tokenAddress", "type": "address" }, { "internalType": "uint256", "name": "_shares", "type": "uint256" } ], "name": "withdraw", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_beneficiary", "type": "address" }, { "internalType": "uint256", "name": "_percentage", "type": "uint256" } ], "name": "setBeneficiaryAndPercentage", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_poolAddress", "type": "address" }, { "internalType": "bytes", "name": "_instruction", "type": "bytes" }, { "internalType": "uint256[]", "name": "_amount", "type": "uint256[]" }, { "internalType": "address[]", "name": "_fromToken", "type": "address[]" }, { "internalType": "address[]", "name": "_returnToken", "type": "address[]" } ], "name": "protocolInteraction", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getAssetList", "outputs": [{ "internalType": "address[]", "name": "", "type": "address[]" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_fromToken", "type": "address" }, { "internalType": "address", "name": "_toToken", "type": "address" }, { "internalType": "uint256", "name": "_amount", "type": "uint256" }, { "internalType": "uint256", "name": "_slippageSwap", "type": "uint256" } ], "name": "exchangeToken", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_tokenAddress", "type": "address" }], "name": "managementFeeCleanUp", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "", "type": "address" }, { "internalType": "address", "name": "", "type": "address" }, { "internalType": "uint256", "name": "id", "type": "uint256" }, { "internalType": "uint256", "name": "", "type": "uint256" }, { "internalType": "bytes", "name": "data", "type": "bytes" } ], "name": "onERC1155Received", "outputs": [{ "internalType": "bytes4", "name": "", "type": "bytes4" }], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "toPause", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "unPause", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "name": "getVaultSlippage", "outputs": [{ "internalType": "uint256", "name": "", "type": "uint256" }], "stateMutability": "view", "type": "function" }, { "inputs": [{ "internalType": "address", "name": "_emergencyVault", "type": "address" }], "name": "changeEmergencyVault", "outputs": [], "stateMutability": "nonpayable", "type": "function" } ]')
    ierc20_abi = json.loads(
        '[ { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "owner", "type": "address" }, { "indexed": true, "internalType": "address", "name": "spender", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Approval", "type": "event" }, { "anonymous": false, "inputs": [ { "indexed": true, "internalType": "address", "name": "from", "type": "address" }, { "indexed": true, "internalType": "address", "name": "to", "type": "address" }, { "indexed": false, "internalType": "uint256", "name": "value", "type": "uint256" } ], "name": "Transfer", "type": "event" }, { "inputs": [], "name": "totalSupply", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "account", "type": "address" } ], "name": "balanceOf", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "recipient", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transfer", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "owner", "type": "address" }, { "internalType": "address", "name": "spender", "type": "address" } ], "name": "allowance", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "spender", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "approve", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "internalType": "address", "name": "sender", "type": "address" }, { "internalType": "address", "name": "recipient", "type": "address" }, { "internalType": "uint256", "name": "amount", "type": "uint256" } ], "name": "transferFrom", "outputs": [ { "internalType": "bool", "name": "", "type": "bool" } ], "stateMutability": "nonpayable", "type": "function" } ]')

    def getNAV(self, vault_address):
        run = Run()
        return run.get_vault_nav(vault_address=vault_address)

    def getNAVHistorical(self, vault_address, timestamp, is_date):
        run = Run()
        return run.get_vault_nav(vault_address=vault_address, time_stamp=timestamp, is_date=is_date)

    def getVaultTokenPrice(self, token_address):
        run = Run()
        return run.get_token_price(token_address=token_address, is_vault_token="true")

    def getVaultTokenPriceHistorical(self, token_address, timestamp, is_date):
        run = Run()
        return run.get_token_price(token_address=token_address, is_vault_token="true", time_stamp=timestamp,
                                   is_date=is_date)

    def getAssetTokenPrice(self, token_address):
        run = Run()
        return run.get_token_price(token_address=token_address, is_vault_token="false")

    def getAssetTokenPriceHistorical(self, token_address, timestamp, is_date):
        run = Run()
        return run.get_token_price(token_address=token_address, is_vault_token="false", time_stamp=timestamp,
                                   is_date=is_date)

    def getTokenBalance(self, vault_address, token_address):
        run = Run()
        return run.get_token_balance(vault_address=vault_address, token_address=token_address)

    def getTokenBalanceHistorical(self, vault_address, token_address, timestamp, is_date):
        run = Run()
        return run.get_token_balance(vault_address=vault_address, token_address=token_address, time_stamp=timestamp,
                                     is_date=is_date)

    def getVaultAssets(self, vault_address):
        run = Run()
        return run.get_vault_assets(vault_address=vault_address)

    def getTokenDecimal(self, token_address):
        run = Run()
        return run.get_token_decimal(token_address)

    def getCurrentBlockNumber(self):
        web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER, request_kwargs={'timeout': 60}))
        return web3.eth.blockNumber

    def deposit(self, vault_address, token_address, amount):
        web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER, request_kwargs={'timeout': 60}))
        private_key = Config.PRIVATE_KEY
        account = web3.eth.account.privateKeyToAccount(private_key)
        assert private_key is not None, "Private key is not present in config.yml"
        assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

        vault_contract = web3.eth.contract(address=web3.toChecksumAddress(vault_address),
                                           abi=self.yieldster_vault_abi)
        token_contract = web3.eth.contract(address=web3.toChecksumAddress(token_address),
                                           abi=self.ierc20_abi)

        allowance_transaction = token_contract.functions.approve(
            web3.toChecksumAddress(vault_address),
            amount).buildTransaction({'nonce': web3.eth.getTransactionCount(
            web3.toChecksumAddress(account.address))})
        signed_allowance_transaction = web3.eth.account.signTransaction(allowance_transaction, private_key)
        web3.eth.sendRawTransaction(signed_allowance_transaction.rawTransaction)

        deposit_transaction = vault_contract.functions.deposit(
            web3.toChecksumAddress(token_address),
            amount).buildTransaction({'nonce': web3.eth.getTransactionCount(
            web3.toChecksumAddress(account.address))})
        signed_deposit_transaction = web3.eth.account.signTransaction(deposit_transaction, private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_deposit_transaction.rawTransaction)
        if web3.eth.getTransactionReceipt(web3.toHex(tx_hash)) is None:
            return {
                "transactionHash": web3.toHex(tx_hash),
                "status": 0
            }
        else:
            return {
                "transactionHash": web3.toHex(tx_hash),
                "status": web3.eth.getTransactionReceipt(web3.toHex(tx_hash)).status
            }

    def withdraw(self, vault_address, token_address, amount):
        try:
            web3 = Web3(Web3.HTTPProvider(Config.WEB3_PROVIDER, request_kwargs={'timeout': 60}))
            private_key = Config.PRIVATE_KEY
            account = web3.eth.account.privateKeyToAccount(private_key)
            assert private_key is not None, "Private key is not present in config.yml"
            assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

            vault_contract = web3.eth.contract(address=web3.toChecksumAddress(vault_address),
                                               abi=self.yieldster_vault_abi)
            token_contract = web3.eth.contract(address=web3.toChecksumAddress(token_address),
                                               abi=self.ierc20_abi)

            token_balance_in_vault = self.getTokenBalance(vault_address, token_address)
            token_balance_in_vault = token_balance_in_vault['data']['TokenBalance']
            token_price = self.getAssetTokenPrice(token_address)
            token_price = token_price['data']['TokenPrice']
            token_decimal = self.getTokenDecimal(token_address)
            token_amount = token_price * token_balance_in_vault / math.pow(10, token_decimal['data'])

            if token_amount > amount:
                withdraw_transaction = vault_contract.functions.withdraw(
                    web3.toChecksumAddress(token_address),
                    amount).buildTransaction({'nonce': web3.eth.getTransactionCount(
                    web3.toChecksumAddress(account.address))})
                signed_withdraw_transaction = web3.eth.account.signTransaction(withdraw_transaction, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_withdraw_transaction.rawTransaction)
                if web3.eth.getTransactionReceipt(web3.toHex(tx_hash)) is None:
                    return {
                        "transactionHash": web3.toHex(tx_hash),
                        "status": 0
                    }
                else:
                    return {
                        "transactionHash": web3.toHex(tx_hash),
                        "status": web3.eth.getTransactionReceipt(web3.toHex(tx_hash)).status
                    }
            else:
                amount_to_swap = amount - token_amount
                run = Run()
                encoded_withdraw = vault_contract.encodeABI("withdraw", [token_address, amount])
                estimated_gas = run.get_estimated_gas(vault_address, token_address, encoded_withdraw, account.address)
                withdraw_transaction = vault_contract.functions.withdraw(
                    web3.toChecksumAddress(token_address),
                    amount).buildTransaction({'nonce': web3.eth.getTransactionCount(
                    web3.toChecksumAddress(account.address)), 'value': int(float(estimated_gas['data']))})
                signed_withdraw_transaction = web3.eth.account.signTransaction(withdraw_transaction, private_key)
                print(signed_withdraw_transaction)
                response = run.execute_withdraw(account.address, int(float(estimated_gas['data'])), token_address,
                                                amount,
                                                signed_withdraw_transaction, vault_address)
                print(response)
                pass
        except Exception as e:
            print("Exception while executing withdraw: ", e)
