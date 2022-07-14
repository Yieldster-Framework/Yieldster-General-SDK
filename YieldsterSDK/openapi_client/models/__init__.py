# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from YieldsterSDK.openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from YieldsterSDK.openapi_client.model.access_list_object import AccessListObject
from YieldsterSDK.openapi_client.model.advisor_key import AdvisorKey
from YieldsterSDK.openapi_client.model.asset import Asset
from YieldsterSDK.openapi_client.model.binary import Binary
from YieldsterSDK.openapi_client.model.currency import Currency
from YieldsterSDK.openapi_client.model.deposit_strategy import DepositStrategy
from YieldsterSDK.openapi_client.model.error import Error
from YieldsterSDK.openapi_client.model.eth_transaction import EthTransaction
from YieldsterSDK.openapi_client.model.faq import Faq
from YieldsterSDK.openapi_client.model.fee_model import FeeModel
from YieldsterSDK.openapi_client.model.fee_strategy import FeeStrategy
from YieldsterSDK.openapi_client.model.pending_vault import PendingVault
from YieldsterSDK.openapi_client.model.pending_vault_transaction import PendingVaultTransaction
from YieldsterSDK.openapi_client.model.protocol import Protocol
from YieldsterSDK.openapi_client.model.response import Response
from YieldsterSDK.openapi_client.model.sdk_response import SDKResponse
from YieldsterSDK.openapi_client.model.security_configuration import SecurityConfiguration
from YieldsterSDK.openapi_client.model.swagger_resource import SwaggerResource
from YieldsterSDK.openapi_client.model.transaction import Transaction
from YieldsterSDK.openapi_client.model.ui_response import UIResponse
from YieldsterSDK.openapi_client.model.ui_configuration import UiConfiguration
from YieldsterSDK.openapi_client.model.user import User
from YieldsterSDK.openapi_client.model.vault import Vault
from YieldsterSDK.openapi_client.model.vault_display_model import VaultDisplayModel
from YieldsterSDK.openapi_client.model.vault_transactions import VaultTransactions
from YieldsterSDK.openapi_client.model.white_list import WhiteList
from YieldsterSDK.openapi_client.model.withdrawal_strategy import WithdrawalStrategy
