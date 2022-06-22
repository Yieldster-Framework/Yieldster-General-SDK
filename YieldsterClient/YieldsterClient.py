from JavaApiRun import Run


class YieldsterClient:

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
