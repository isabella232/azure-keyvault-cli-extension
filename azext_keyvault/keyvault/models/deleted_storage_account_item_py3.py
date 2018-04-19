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

from .storage_account_item import StorageAccountItem


class DeletedStorageAccountItem(StorageAccountItem):
    """The deleted storage account item containing metadata about the deleted
    storage account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Storage identifier.
    :vartype id: str
    :ivar resource_id: Storage account resource Id.
    :vartype resource_id: str
    :ivar attributes: The storage account management attributes.
    :vartype attributes: ~azure.keyvault.models.StorageAccountAttributes
    :ivar tags: Application specific metadata in the form of key-value pairs.
    :vartype tags: dict[str, str]
    :param recovery_id: The url of the recovery object, used to identify and
     recover the deleted storage account.
    :type recovery_id: str
    :ivar scheduled_purge_date: The time when the storage account is scheduled
     to be purged, in UTC
    :vartype scheduled_purge_date: datetime
    :ivar deleted_date: The time when the storage account was deleted, in UTC
    :vartype deleted_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'resource_id': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
        'scheduled_purge_date': {'readonly': True},
        'deleted_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'StorageAccountAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'recovery_id': {'key': 'recoveryId', 'type': 'str'},
        'scheduled_purge_date': {'key': 'scheduledPurgeDate', 'type': 'unix-time'},
        'deleted_date': {'key': 'deletedDate', 'type': 'unix-time'},
    }

    def __init__(self, *, recovery_id: str=None, **kwargs) -> None:
        super(DeletedStorageAccountItem, self).__init__(, **kwargs)
        self.recovery_id = recovery_id
        self.scheduled_purge_date = None
        self.deleted_date = None
