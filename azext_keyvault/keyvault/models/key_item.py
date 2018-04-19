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


class KeyItem(Model):
    """The key item containing key metadata.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param kid: Key identifier.
    :type kid: str
    :param attributes: The key management attributes.
    :type attributes: ~azure.keyvault.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    :ivar managed: True if the key's lifetime is managed by key vault. If this
     is a key backing a certificate, then managed will be true.
    :vartype managed: bool
    """

    _validation = {
        'managed': {'readonly': True},
    }

    _attribute_map = {
        'kid': {'key': 'kid', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed': {'key': 'managed', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(KeyItem, self).__init__(**kwargs)
        self.kid = kwargs.get('kid', None)
        self.attributes = kwargs.get('attributes', None)
        self.tags = kwargs.get('tags', None)
        self.managed = None
