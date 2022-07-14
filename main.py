from YieldsterClient.YieldsterClient import YieldsterClient


def get_vault_nav():
    yieldster_client = YieldsterClient()
    nav = yieldster_client.getNAV("0xb20Cf65651B4Eef714fD25b1BfF52EcC8E4D902B")
    print(nav)


def get_vault_nav_historical():
    yieldster_client = YieldsterClient()
    nav = yieldster_client.getNAVHistorical("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718", 1655771105, "false")
    print(nav)


def get_token_balance():
    yieldster_client = YieldsterClient()
    token_balance = yieldster_client.getTokenBalance("0xb20Cf65651B4Eef714fD25b1BfF52EcC8E4D902B",
                                                     "0x6B175474E89094C44Da98b954EedeAC495271d0F")
    print(token_balance)


def get_token_balance_historical():
    yieldster_client = YieldsterClient()
    token_balance = yieldster_client.getTokenBalanceHistorical("0xb20Cf65651B4Eef714fD25b1BfF52EcC8E4D902B",
                                                               "0x6B175474E89094C44Da98b954EedeAC495271d0F", 1655771105,
                                                               "false")
    print(token_balance)


def get_vault_token_price():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getVaultTokenPrice("0xb20Cf65651B4Eef714fD25b1BfF52EcC8E4D902B")
    print(token_price)


def get_vault_token_price_historical():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getVaultTokenPriceHistorical("0xb20Cf65651B4Eef714fD25b1BfF52EcC8E4D902B",
                                                                1655771105,
                                                                "false")
    print(token_price)


def get_asset_token_price():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getAssetTokenPrice("0x6B175474E89094C44Da98b954EedeAC495271d0F")
    print(token_price)


def get_asset_token_price_historical():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getAssetTokenPriceHistorical("0x6B175474E89094C44Da98b954EedeAC495271d0F",
                                                                1655771105,
                                                                "false")
    print(token_price)


def get_vault_assets():
    yieldster_client = YieldsterClient()
    vault_assets = yieldster_client.getVaultAssets("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718")
    print(vault_assets)


def get_current_block_number():
    yieldster_client = YieldsterClient()
    yieldster_client.getCurrentBlockNumber()


def deposit():
    yieldster_client = YieldsterClient()
    response = yieldster_client.deposit("0x77b2CE13b4813976EEc236112377e4375a811aAC",
                                        "0xdac17f958d2ee523a2206206994597c13d831ec7",
                                        7000000)
    print(response)


def withdraw():
    yieldster_client = YieldsterClient()
    response = yieldster_client.withdraw("0x77b2CE13b4813976EEc236112377e4375a811aAC",
                                         "0xdAC17F958D2ee523a2206206994597C13D831ec7",
                                         5000000000000000000)
    print(response)


# Driver function
if __name__ == '__main__':
    # get_vault_nav()
    # get_vault_nav_historical()
    # get_vault_assets()
    # get_token_balance()
    # get_vault_token_price()
    # get_asset_token_price()
    # get_asset_token_price_historical()
    # get_vault_token_price()
    # get_vault_token_price_historical()
    # get_token_balance_historical()

    # get_current_block_number()
    # deposit()
    withdraw()
