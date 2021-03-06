"""
    Yieldster SDK API

    Swagger documentation for Yieldster 2.0 SDK API's  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from JavaApi.openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from JavaApi.openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from JavaApi.openapi_client.model.binary import Binary
    globals()['Binary'] = Binary


class Vault(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('vault_type',): {
            'PUBLIC': "PUBLIC",
            'PRIVATE': "PRIVATE",
        },
    }

    validations = {
        ('supported_assets',): {
        },
        ('supported_protocols',): {
        },
        ('staked_pools',): {
        },
        ('fee_strategy_list',): {
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'vault_address': (str,),  # noqa: E501
            'vault_name': (str,),  # noqa: E501
            'advisor_email': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'logo_img': (Binary,),  # noqa: E501
            'base_currency': (str,),  # noqa: E501
            'organization_data': (str,),  # noqa: E501
            'supported_assets': ([str],),  # noqa: E501
            'vault_type': (str,),  # noqa: E501
            'supported_protocols': ([str],),  # noqa: E501
            'reward_token_name': (str,),  # noqa: E501
            'reward_token_symbol': (str,),  # noqa: E501
            'vault_admin': (str,),  # noqa: E501
            'optimal_cash_balance': (int,),  # noqa: E501
            'investment_limit': (int,),  # noqa: E501
            'advisor_id': (str,),  # noqa: E501
            'staked_pools': ([str],),  # noqa: E501
            'advisor_end_point': (str,),  # noqa: E501
            'vault_advisor_setting': ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)},),  # noqa: E501
            'invested_protocol': (str,),  # noqa: E501
            'mangement_fee': (float,),  # noqa: E501
            'deposit_strategy': (str,),  # noqa: E501
            'withdrawal_strategy': (str,),  # noqa: E501
            'emergency_vault_address': (str,),  # noqa: E501
            'beneficiary_address': (str,),  # noqa: E501
            'fee_strategy_list': ([str],),  # noqa: E501
            'last_advisor_execution_date': (datetime,),  # noqa: E501
            'locked': (bool,),  # noqa: E501
            'visible': (bool,),  # noqa: E501
            'featured_vault': (bool,),  # noqa: E501
            'emergency_break_set': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'vault_address': 'vaultAddress',  # noqa: E501
        'vault_name': 'vaultName',  # noqa: E501
        'advisor_email': 'advisorEmail',  # noqa: E501
        'id': 'id',  # noqa: E501
        'description': 'description',  # noqa: E501
        'logo_img': 'logoImg',  # noqa: E501
        'base_currency': 'baseCurrency',  # noqa: E501
        'organization_data': 'organizationData',  # noqa: E501
        'supported_assets': 'supportedAssets',  # noqa: E501
        'vault_type': 'vaultType',  # noqa: E501
        'supported_protocols': 'supportedProtocols',  # noqa: E501
        'reward_token_name': 'rewardTokenName',  # noqa: E501
        'reward_token_symbol': 'rewardTokenSymbol',  # noqa: E501
        'vault_admin': 'vaultAdmin',  # noqa: E501
        'optimal_cash_balance': 'optimalCashBalance',  # noqa: E501
        'investment_limit': 'investmentLimit',  # noqa: E501
        'advisor_id': 'advisorId',  # noqa: E501
        'staked_pools': 'stakedPools',  # noqa: E501
        'advisor_end_point': 'advisorEndPoint',  # noqa: E501
        'vault_advisor_setting': 'vaultAdvisorSetting',  # noqa: E501
        'invested_protocol': 'investedProtocol',  # noqa: E501
        'mangement_fee': 'mangementFee',  # noqa: E501
        'deposit_strategy': 'depositStrategy',  # noqa: E501
        'withdrawal_strategy': 'withdrawalStrategy',  # noqa: E501
        'emergency_vault_address': 'emergencyVaultAddress',  # noqa: E501
        'beneficiary_address': 'beneficiaryAddress',  # noqa: E501
        'fee_strategy_list': 'feeStrategyList',  # noqa: E501
        'last_advisor_execution_date': 'lastAdvisorExecutionDate',  # noqa: E501
        'locked': 'locked',  # noqa: E501
        'visible': 'visible',  # noqa: E501
        'featured_vault': 'featuredVault',  # noqa: E501
        'emergency_break_set': 'emergencyBreakSet',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, vault_address, vault_name, advisor_email, *args, **kwargs):  # noqa: E501
        """Vault - a model defined in OpenAPI

        Args:
            vault_address (str):
            vault_name (str):
            advisor_email (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            logo_img (Binary): [optional]  # noqa: E501
            base_currency (str): [optional]  # noqa: E501
            organization_data (str): [optional]  # noqa: E501
            supported_assets ([str]): [optional]  # noqa: E501
            vault_type (str): [optional]  # noqa: E501
            supported_protocols ([str]): [optional]  # noqa: E501
            reward_token_name (str): [optional]  # noqa: E501
            reward_token_symbol (str): [optional]  # noqa: E501
            vault_admin (str): [optional]  # noqa: E501
            optimal_cash_balance (int): [optional]  # noqa: E501
            investment_limit (int): [optional]  # noqa: E501
            advisor_id (str): [optional]  # noqa: E501
            staked_pools ([str]): [optional]  # noqa: E501
            advisor_end_point (str): [optional]  # noqa: E501
            vault_advisor_setting ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            invested_protocol (str): [optional]  # noqa: E501
            mangement_fee (float): [optional]  # noqa: E501
            deposit_strategy (str): [optional]  # noqa: E501
            withdrawal_strategy (str): [optional]  # noqa: E501
            emergency_vault_address (str): [optional]  # noqa: E501
            beneficiary_address (str): [optional]  # noqa: E501
            fee_strategy_list ([str]): [optional]  # noqa: E501
            last_advisor_execution_date (datetime): [optional]  # noqa: E501
            locked (bool): [optional]  # noqa: E501
            visible (bool): [optional]  # noqa: E501
            featured_vault (bool): [optional]  # noqa: E501
            emergency_break_set (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.vault_address = vault_address
        self.vault_name = vault_name
        self.advisor_email = advisor_email
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, vault_address, vault_name, advisor_email, *args, **kwargs):  # noqa: E501
        """Vault - a model defined in OpenAPI

        Args:
            vault_address (str):
            vault_name (str):
            advisor_email (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): [optional]  # noqa: E501
            description (str): [optional]  # noqa: E501
            logo_img (Binary): [optional]  # noqa: E501
            base_currency (str): [optional]  # noqa: E501
            organization_data (str): [optional]  # noqa: E501
            supported_assets ([str]): [optional]  # noqa: E501
            vault_type (str): [optional]  # noqa: E501
            supported_protocols ([str]): [optional]  # noqa: E501
            reward_token_name (str): [optional]  # noqa: E501
            reward_token_symbol (str): [optional]  # noqa: E501
            vault_admin (str): [optional]  # noqa: E501
            optimal_cash_balance (int): [optional]  # noqa: E501
            investment_limit (int): [optional]  # noqa: E501
            advisor_id (str): [optional]  # noqa: E501
            staked_pools ([str]): [optional]  # noqa: E501
            advisor_end_point (str): [optional]  # noqa: E501
            vault_advisor_setting ({str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}): [optional]  # noqa: E501
            invested_protocol (str): [optional]  # noqa: E501
            mangement_fee (float): [optional]  # noqa: E501
            deposit_strategy (str): [optional]  # noqa: E501
            withdrawal_strategy (str): [optional]  # noqa: E501
            emergency_vault_address (str): [optional]  # noqa: E501
            beneficiary_address (str): [optional]  # noqa: E501
            fee_strategy_list ([str]): [optional]  # noqa: E501
            last_advisor_execution_date (datetime): [optional]  # noqa: E501
            locked (bool): [optional]  # noqa: E501
            visible (bool): [optional]  # noqa: E501
            featured_vault (bool): [optional]  # noqa: E501
            emergency_break_set (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.vault_address = vault_address
        self.vault_name = vault_name
        self.advisor_email = advisor_email
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
