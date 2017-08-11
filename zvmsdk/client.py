# Copyright 2017 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from zvmsdk import config
from zvmsdk import log
from zvmsdk import utils as zvmutils


CONF = config.CONF
LOG = log.LOG

_XCAT_CLIENT = None
_SMUT_CLIENT = None


def get_xcatclient():
    global _XCAT_CLIENT
    if _XCAT_CLIENT is None:
        try:
            _XCAT_CLIENT = zvmutils.import_object(
                'zvmsdk.xcatclient.XCATClient')
        except ImportError:
            LOG.error("Unable to get zvmclient")
            raise ImportError
    return _XCAT_CLIENT


def get_smutclient():
    global _SMUT_CLIENT
    if _SMUT_CLIENT is None:
        try:
            _SMUT_CLIENT = zvmutils.import_object(
                'zvmsdk.smutclient.SMUTClient')
        except ImportError:
            LOG.error("Unable to get zvmclient")
            raise ImportError
    return _SMUT_CLIENT


def get_zvmclient():
    if CONF.zvm.client_type == 'xcat':
        return get_xcatclient()
    elif CONF.zvm.client_type == 'smut':
        return get_smutclient()
    else:
        # TODO: raise Exception
        pass


class ZVMClient(object):

    def guest_start(self, userid):
        pass

    def guest_stop(self, userid):
        pass

    def get_power_state(self, userid):
        pass

    def image_import(self, image_file_path, os_version, remote_host=None):
        pass

    def image_query(self, imagekeyword=None):
        pass

    def image_delete(self, image_name):
        pass

    def get_host_info(self):
        pass

    def get_diskpool_info(self, pool):
        pass

    def virtual_network_vswitch_query_iuo_stats(self):
        pass

    def get_vm_list(self):
        pass

    def image_performance_query(self, uid_list):
        pass

    def add_vswitch(self, name, rdev=None, controller='*',
                    connection='CONNECT', network_type='IP',
                    router="NONROUTER", vid='UNAWARE', port_type='ACCESS',
                    gvrp='GVRP', queue_mem=8, native_vid=1, persist=True):
        pass

    def couple_nic_to_vswitch(self, userid, nic_vdev,
                              vswitch_name, active=False):
        pass

    def create_nic(self, userid, vdev=None, nic_id=None,
                   mac_addr=None, ip_addr=None, active=False):
        pass

    def delete_nic(self, userid, vdev, active=False):
        pass

    def delete_vswitch(self, switch_name, persist=True):
        pass

    def get_vm_nic_vswitch_info(self, vm_id):
        pass

    def get_vswitch_list(self):
        pass

    def grant_user_to_vswitch(self, vswitch_name, userid):
        pass

    def revoke_user_from_vswitch(self, vswitch_name, userid):
        pass

    def set_vswitch_port_vlan_id(self, vswitch_name, userid, vlan_id):
        pass

    def set_vswitch(self, switch_name, **kwargs):
        pass

    def uncouple_nic_from_vswitch(self, userid, nic_vdev,
                                  active=False):
        pass

    def get_guest_connection_status(self, userid):
        pass

    def guest_deploy(self, node, image_name, transportfiles=None,
                     remotehost=None, vdev=None):
        pass

    def process_additional_minidisks(self, userid, disk_info):
        pass

    def get_image_performance_info(self, userid):
        pass

    def get_user_direct(self, userid):
        pass

    def create_vm(self, userid, cpu, memory, disk_list, profile):
        pass

    def delete_vm(self, userid):
        pass
