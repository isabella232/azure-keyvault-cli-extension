# coding=utf-8
# pylint: disable-all

# ---------------------------------------------------------------------------------
# The code for this extension file is pulled from the azure-sdk-for-python repo and
# modified to run inside a cli extension.  Changes may cause incorrect behavior and
# will be lost if the code is regenerated. Please see the readme.md at the base of
# the keyvault extension for details.
# ---------------------------------------------------------------------------------

# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SecretRestoreParameters(Model):
    """The secret restore parameters.

    All required parameters must be populated in order to send to Azure.

    :param secret_bundle_backup: Required. The backup blob associated with a
     secret bundle.
    :type secret_bundle_backup: bytes
    """

    _validation = {
        'secret_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'secret_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, *, secret_bundle_backup: bytes, **kwargs) -> None:
        super(SecretRestoreParameters, self).__init__(**kwargs)
        self.secret_bundle_backup = secret_bundle_backup
