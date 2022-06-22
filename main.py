from YieldsterClient.YieldsterClient import YieldsterClient


def get_vault_nav():
    yieldster_client = YieldsterClient()
    nav = yieldster_client.getNAV("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718")
    print(nav)


def get_vault_nav_historical():
    yieldster_client = YieldsterClient()
    nav = yieldster_client.getNAVHistorical("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718", 1655771105, "false")
    print(nav)


def get_token_balance():
    yieldster_client = YieldsterClient()
    token_balance = yieldster_client.getTokenBalance("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718",
                                                     "0x6B175474E89094C44Da98b954EedeAC495271d0F")
    print(token_balance)


def get_token_balance_historical():
    yieldster_client = YieldsterClient()
    token_balance = yieldster_client.getTokenBalanceHistorical("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718",
                                                               "0x6B175474E89094C44Da98b954EedeAC495271d0F", 1655771105,
                                                               "false")
    print(token_balance)


def get_vault_token_price():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getVaultTokenPrice("0x6d00dff1bf1b74f7bd366bc8b726f812934e3718")
    print(token_price)


def get_vault_token_price_historical():
    yieldster_client = YieldsterClient()
    token_price = yieldster_client.getVaultTokenPriceHistorical("0x02FB737B01dd3Dfc4eF006969b4211487afdd06a",
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


# Driver function
if __name__ == '__main__':
    # get_vault_nav()
    # get_vault_nav_historical()
    # get_vault_assets()

    get_token_balance()

    # get_vault_token_price()

    # get_asset_token_price()
    # get_asset_token_price_historical()
    # get_vault_token_price()
    # get_vault_token_price_historical()
    get_token_balance_historical()
