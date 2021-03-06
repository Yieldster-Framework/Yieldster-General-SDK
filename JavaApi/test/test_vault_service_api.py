"""
    Yieldster SDK API

    Swagger documentation for Yieldster 2.0 SDK API's  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import JavaApi.openapi_client
from JavaApi.openapi_client.api.vault_service_api import VAULTSERVICEApi  # noqa: E501


class TestVAULTSERVICEApi(unittest.TestCase):
    """VAULTSERVICEApi unit test stubs"""

    def setUp(self):
        self.api = VAULTSERVICEApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_staked_pools(self):
        """Test case for add_staked_pools

        API to add staked pools of a vault  # noqa: E501
        """
        pass

    def test_featured_status(self):
        """Test case for featured_status

        API to update featured Vault by Id   # noqa: E501
        """
        pass

    def test_get_advisor_setting_by_vault_id(self):
        """Test case for get_advisor_setting_by_vault_id

        API to get VAULT_ADVISOR_SETTINGS   # noqa: E501
        """
        pass

    def test_get_all_my_vaults(self):
        """Test case for get_all_my_vaults

        API to get MY_VAULTS by pagination  # noqa: E501
        """
        pass

    def test_get_all_vaults(self):
        """Test case for get_all_vaults

        API to get all vault details  # noqa: E501
        """
        pass

    def test_get_all_vaults_by_pagination(self):
        """Test case for get_all_vaults_by_pagination

        API to get ALL_VAULTS By Paginating  # noqa: E501
        """
        pass

    def test_get_apr(self):
        """Test case for get_apr

        API to get APR   # noqa: E501
        """
        pass

    def test_get_asset_by_vault_id(self):
        """Test case for get_asset_by_vault_id

        API to get asset details of a vault  # noqa: E501
        """
        pass

    def test_get_dashboard_graph(self):
        """Test case for get_dashboard_graph

        """
        pass

    def test_get_details_by_search(self):
        """Test case for get_details_by_search

        API to get asset, protocol and vault details by SEARCHING  # noqa: E501
        """
        pass

    def test_get_details_for_auto_complete(self):
        """Test case for get_details_for_auto_complete

        API to achieve AUTO_COMPLETE on the basis of protocols, assets and vaults  # noqa: E501
        """
        pass

    def test_get_featured_vault_details_by_pagination(self):
        """Test case for get_featured_vault_details_by_pagination

        API to get FEATURED_VAULTS by pagination  # noqa: E501
        """
        pass

    def test_get_invested_protocol_by_vault_id(self):
        """Test case for get_invested_protocol_by_vault_id

        API to get invested protocol of a vault  # noqa: E501
        """
        pass

    def test_get_protocols_by_vault_id(self):
        """Test case for get_protocols_by_vault_id

        API to get supported protocols of a vault  # noqa: E501
        """
        pass

    def test_get_staked_pools(self):
        """Test case for get_staked_pools

        API to get staked pools of a vault  # noqa: E501
        """
        pass

    def test_get_vault_by_address(self):
        """Test case for get_vault_by_address

        API to get VaultByAddress  # noqa: E501
        """
        pass

    def test_get_vault_by_base_currency(self):
        """Test case for get_vault_by_base_currency

        API to get VAULT_BY_BASE_CURRENCY  # noqa: E501
        """
        pass

    def test_get_vault_by_financial_details1(self):
        """Test case for get_vault_by_financial_details1

        API to get Investment Details like TOTAL_BALANCE and TOTAL_RETURN for NAV BAR  # noqa: E501
        """
        pass

    def test_get_vault_by_id(self):
        """Test case for get_vault_by_id

        API to get vault details by ID   # noqa: E501
        """
        pass

    def test_get_vault_by_id1(self):
        """Test case for get_vault_by_id1

        API to get vault token details of user and Token Nav   # noqa: E501
        """
        pass

    def test_get_vault_details_by_filtering_with_pagination(self):
        """Test case for get_vault_details_by_filtering_with_pagination

        API to get VAULT_BY_FILTERING  # noqa: E501
        """
        pass

    def test_get_vault_image(self):
        """Test case for get_vault_image

        API to get VAULT_ICON  # noqa: E501
        """
        pass

    def test_get_vault_sorted(self):
        """Test case for get_vault_sorted

        API to get SORTED_VAULTS  # noqa: E501
        """
        pass

    def test_get_vault_transaction_by_vault_address_and_pending_or_reverted(self):
        """Test case for get_vault_transaction_by_vault_address_and_pending_or_reverted

        API to filter vault transaction by txStatus (PENDING/REVERTED)   # noqa: E501
        """
        pass

    def test_profit_management_fee(self):
        """Test case for profit_management_fee

        API to update PROFIT MANAGEMENT FEE   # noqa: E501
        """
        pass

    def test_user_investment_details(self):
        """Test case for user_investment_details

        """
        pass


if __name__ == '__main__':
    unittest.main()
