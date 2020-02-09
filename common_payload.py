"""
Copyright (c) 2020 Nutanix Inc. All rights reserved.
Author: bhawani.singh@nutanix.com

"""
from constant import ENDOR_PC_BUILD_URL


class BasePayload(object):

    """
    Payload parameters
    """
    def __init__(self):
        self.NUTEST_BRANCH = None
        self.NUTEST_COMMIT = None
        self.NUTEST_PATCH = ''
        self.PLUGINS = dict()
        self.AOS_REL_BRANCH = None
        self.PC_REL_BRANCH = None
        self.POOL_NAME = []
        self.PC_URL = ENDOR_PC_BUILD_URL
        self.PC_COMMIT_ID = None
        self.NOS_COMMIT_ID = None
        self.SKIP_COMMIT_VALIDATION = False
        self.CLUSTER_SELECTION = dict()
        self.FOUNDATION_BUILD_URL = ''
        self.NOS_URL = ''
        self.HYPERVISOR_URL = ''
        self.NOS_URL = ''
        self.BUILD_TYPE = "release"
        self.REQUESTED_HARDWARE = dict()
        self.BUILD_SELECTION = dict()
        self.SCHEDULING_OPTIONS = dict()
        self.USE_NOS_BY_COMMIT_ID = dict()
        self.USE_NOS_BY_SMOKE_PASSED = dict()
        self.GIT = dict()
        self.POST_RUN = [{u'args': {},
                          u'description': u'Sends mail to the recipients.',
                          u'stage': u'post_run',
                          u'name': u'EmailPlugin'}]
        self.PRE_RUN = []
        self.TASK_PRIORITY = 80
        self.RETRY_IMAGING = 2


class GlobalPayloadParameters(object):

    """
    Pass
    """
    def __init__(self):
        """
        Initializing global parameters.
        """
        self.payload = dict()
        self.RDM_TAG = u'rdm__virtual'
        self.OFFICIAL_TAG = u'official'
        self.DEPLOYMENT_TAG = u'max_deployments__20'
        self.THROTTLE_TAG = u'throttle_tests__20'
        self.EMAILS = [u'bhawani.singh@nutanix.com']


class MasterPayload(GlobalPayloadParameters, BasePayload):

    """
    Master Branch Payload
    """

    def __init__(self):
        GlobalPayloadParameters.__init__(self)
        BasePayload.__init__(self)
        self.POOL_NAME = [u'AHV-REG-NESTED-POOL']
        self.payload_map = dict()

    def load_payload(self):
        self.payload_map['git'] = self.get_git
        self.payload_map[u'scheduling_options'] = self.get_scheduling_options
        self.payload_map['tester_tags'] = self.get_tester_tags
        self.payload_map[u'requested_hardware'] = self.get_requested_hardware
        self.payload_map[u'emails'] = self.get_email_ids
        self.payload_map[u'plugins'] = self.get_jita_plugins
        self.payload_map['patch_url'] = self.get_nutest_patch_url
        self.payload_map[u'build_selection'] = self.get_build_selection
        self.payload_map[u'cluster_selection'] = self.get_cluster_selection
        self.payload_map[u'nutest_commit'] = self.get_nutest_commit
        self.payload_map[u'test_framework'] = None
        self.payload_map[u'nutest_branch'] = self.get_nutest_branch
        self.payload_map[u'skip_commit_id_validation'] = None

    @property
    def get_git(self):
        self.GIT = {
            u'repo': u'main',
            u'branch': self.nos_branch
        }
        return self.GIT

    @property
    def get_tester_tags(self):
        return [self.DEPLOYMENT_TAG, self.THROTTLE_TAG, self.RDM_TAG]

    @property
    def get_nutest_branch(self):
        self.NUTEST_BRANCH = self.nutest_commit
        return self.NUTEST_BRANCH

    @property
    def get_nutest_commit(self):
        return self.NUTEST_COMMIT

    @property
    def get_email_ids(self):
        self.EMAILS = self.email_ids
        return self.EMAILS

    @property
    def get_jita_plugins(self):
        self.PLUGINS = {
            u'post_run': self.post_run,
            u'pre_run': self.pre_run
        }
        return self.PLUGINS

    @property
    def get_build_selection(self):
        self.BUILD_SELECTION = self.get_nos_by_commit_id
        return self.BUILD_SELECTION

    @property
    def get_nos_by_commit_id(self):
        self.USE_NOS_BY_COMMIT_ID = {
            u'build_type': self.build_type,
            u'by_commit_id': True,
            u'commit_id': self.nos_commit,
            u'use_stable_agave_commit': False,
            u'use_stable_nutest_commit': False
        }
        return self.USE_NOS_BY_COMMIT_ID

    @property
    def get_cluster_selection(self):
        self.CLUSTER_SELECTION = {
            u'pool_name': self.POOL_NAME,
            u'by_node_pool': True
        }
        return self.CLUSTER_SELECTION

    @property
    def get_nutest_patch_url(self):
        self.NUTEST_PATCH = self.nutest_patch
        return self.NUTEST_PATCH

    @property
    def get_nos_url(self):
        self.NOS_URL = self.nos_url
        return self.NOS_URL

    @property
    def get_pc_url(self):
        self.PC_URL = dict(PRISM_CENTRAL={
            u'build': {
                u'nos_build_url': self.pc_url
            }
        })
        return self.PC_URL

    @property
    def get_foundation_build_url(self):
        self.FOUNDATION_BUILD_URL = self.foundation_url
        return self.FOUNDATION_BUILD_URL

    @property
    def get_hypervisor_url(self):
        self.HYPERVISOR_URL = self.hypervisor_url
        return self.HYPERVISOR_URL

    @property
    def get_requested_hardware(self):
        self.REQUESTED_HARDWARE = {
            u'hypervisor_version': u'branch_symlink',
            u'hypervisor': u'kvm',
            u'imaging_options': {
                u'datacenter': {
                    u'hyperv': {},
                    u'kvm': {},
                    u'vsphere': {},
                    u'use_host_names': False
                },
            u'foundation_build_url': self.get_foundation_build_url,
            u'min_ram': u'16',
            u'nos_url': self.get_nos_url,
            u'redundancy_factor': u'default',
            u'secondary_datacenters': {
                u'vsphere': {}
            },
            u'hypervisor_url': self.get_hypervisor_url
            }
        }
        return self.REQUESTED_HARDWARE

    @property
    def get_scheduling_options(self):
        self.SCHEDULING_OPTIONS = {
            u'optimize_scheduling': True,
            u'force_imaging': False,
            u'task_priority': self.task_priority,
            u'skip_resource_spec_match': False,
            u'upgrade': False,
            u'retry_imaging': self.retry_imaging,
            u'check_image_compatibility': True}
        return self.SCHEDULING_OPTIONS


# class GOSPayload(MasterPayload):
#
#     def __init__(self, **kwargs):
#         # GlobalPayloadParameters.__init__(self)
#         MasterPayload.__init__(self)
#
#         self.nos_commit = kwargs.get("nos_commit")
#         self.nutest_commit = kwargs.get("nutest_commit")
#         self.email_ids = kwargs.get("email_ids", [u'velurusruthi.naidu@nutanix.com',
#                                                   u'bhawani.singh@nutanix.com'])
#         self.task_priority = kwargs.get("priority", self.TASK_PRIORITY)
#         self.post_run = kwargs.get("post_run", self.POST_RUN)
#         self.pre_run = kwargs.get("pre_run", self.PRE_RUN)
#         self.retry_imaging = kwargs.get("retry_imaging", self.RETRY_IMAGING)
#         self.build_type = kwargs.get("build_type", self.BUILD_TYPE)
#         self.nutest_patch = kwargs.get('nutest_patch', self.NUTEST_PATCH)
#         self.foundation_url = kwargs.get("foundation_build_url", self.FOUNDATION_BUILD_URL)
#         self.hypervisor_url = kwargs.get("hypervisor_url", self.HYPERVISOR_URL)
#         self.nos_url = kwargs.get("nos_url", self.NOS_URL)
#
#     def load_payload(self):
#         super(GOSPayload, self).load_payload()
#
#
# if __name__ == '__main__':
#     gos = GOSPayload(nos_commit=None, nutest_commit=None)
#     print(gos.__dict__)
#     print(gos.get_tester_tags)
#     print(gos.load_payload())

