#
# NUTEST_BRANCH = u'master'
# AOS_REL_BRANCH = u'master'
# PC_REL_BRANCH = u'master'
#
#
# #POOL_NAME = [u'AHV-REG-NODE-POOL-MASTER']
# GPU_POOL_NAME = [u'ahv-gpu-regression']
# POOL_NAME = [u'AHV_NODE_POOL_OSL']
# DUMMY_POOL = [u'AHV-REG-NODE-POOL-MASTER']
# SCALE_PC_POOL = [u'acropolis_scale_Testing']
#
#
# PC_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/' + PC_REL_BRANCH + '/'
# PC_COMMIT_ID = "e070a787925ea915002ebc90029a8c08e4c08ec4"
#
#
# NOS_COMMIT_ID = "e070a787925ea915002ebc90029a8c08e4c08ec4"
#
#
# #SKIP_COMMIT_VALIDATION = u'on'
# SKIP_COMMIT_VALIDATION = False
#
# FOUNDATION_BUILD_URL = ''
# #FOUNDATION_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/foundation-builds/4.5/foundation-4.5-90-88e38e12-universal-release.x86_64.tar.gz'
#
# NOS_URL = ''
# #NOS_URL = u'http://endor.dyn.nutanix.com/builds/nos-builds/master/da8465eb3e3755676486be2212d8bd0cf607fdbe/x86_64/opt/tar/nutanix_installer_package-opt-master-da8465eb3e3755676486be2212d8bd0cf607fdbe-x86_64.tar.gz'
#
# HYPERVISOR_URL = ''
# #HYPERVISOR_URL = u'http://endor.dyn.nutanix.com/builds/ahv-builds/20190308.101176/iso/AHV-DVD-x86_64-el7.nutanix.20190308.101176.iso'
#
#
#
# BUILD_FOLDERS = 'x86_64'
# BUILD_TYPE = 'opt'
# #BUILD_TYPE = 'release'
#
#
# USE_NOS_BY_COMMIT_ID = {
#     u'build_type': BUILD_TYPE,
#     u'by_commit_id': True,
#     u'commit_id': NOS_COMMIT_ID,
#     u'use_stable_agave_commit': False,
#     u'use_stable_nutest_commit': False
# }
# USE_NOS_BY_SMOKE_PASSED = {
#         u'use_stable_nutest_commit': False,
#         u'by_latest_smoked': True,
#         u'build_type': BUILD_TYPE,
#         u'use_stable_agave_commit': False
# }
#
#
# ACROPOLIS_PAYLOAD_MASTER = dict()
# # ACROPOLIS_PAYLOAD_MASTER['tester_tags'] = [u'all', u'v3.1', u'max_deployments__30', u'phx1',
# #                                            u'sched__phx1', u'rdm__phx1', u'sched__alpha',
# #                                            u'official']
#
# ACROPOLIS_PAYLOAD_MASTER['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']
#
# ##### Specify Nutest Branch
# ACROPOLIS_PAYLOAD_MASTER['nutest_branch'] = NUTEST_BRANCH
# ACROPOLIS_PAYLOAD_MASTER['skip_commit_id_validation'] = SKIP_COMMIT_VALIDATION
# ACROPOLIS_PAYLOAD_MASTER['test_framework'] = u'nutest'
#
# ACROPOLIS_PAYLOAD_MASTER['nutest_commit'] = None
#
# ACROPOLIS_PAYLOAD_MASTER[u'emails'] = [u'velurusruthi.naidu@nutanix.com',
#                                        u'bhawani.singh@nutanix.com',
#                                        u'ritopa.dey@nutanix.com'
#                                        ]
#
# # ACROPOLIS_PAYLOAD_MASTER[u'emails'] = [u'muthu.kumaran@nutanix.com']
#
# ACROPOLIS_PAYLOAD_MASTER['plugins'] = {u'post_run': [
#            {u'args': {},
#             u'description': u'Sends mail to the recipients.',
#             u'stage': u'post_run',
#             u'name': u'EmailPlugin'}
#         ],
#          u'pre_run': []
# }
#
# # ACROPOLIS_PAYLOAD_MASTER['plugins'] = {u'post_run': [
# #         {u'args': {},
# #          u'description': u'Sends mail to the recipients.',
# #          u'stage': u'post_run',
# #          u'name': u'EmailPlugin'},
# #         {u'args': {u'xml_file': None, u'services': [u'acropolis', u'ergon'], u'db_password': None,
# #                    u'enable_traceability': False,
# #                    u'db_coverage_ip': u'drt-rlb-mongo-codecoverage-prod-1.corp.nutanix.com', u'port': 27017,
# #                    u'db_name': u'cc', u'db_username': None, u'collection_name': u'code_coverage',
# #                    u'local_mount': u'/home/nutanix/code_coverage/python', u'pycov_options': [u'-i acropolis',
# #                                                                                              u'-i ergon'],
# #                    u'tool_name': u'pycov'},
# #          u'description': u'Computes code coverage data for a given NOS service in python source code.',
# #          u'stage': u'post_run', u'name': u'CodeCoverageComputePythonPostPlugin'}],
# #         u'pre_run': [
# #             {u'args': {u'xml_file': None, u'services': [u'acropolis', u'ergon'], u'enable_traceability': False,
# #                        u'nfs_filer_location': u'10.53.192.66:/volume1/code_coverage/python',
# #                        u'pycov_location': u'http://10.4.16.50/home/rachit.sinha/python_coverage/pycov',
# #                        u'local_mount': u'/home/nutanix/code_coverage/python', u'pycov_options': [u'-i acropolis',
# #                                                                                                  u'-i ergon'],
# #                        u'tool_name': u'pycov'},
# #              u'description': u'Computes code coverage data for a given NOS service in python source code.',
# #              u'stage': u'pre_run',
# #              u'name': u'CodeCoverageComputePythonPrePlugin'}]
# # }
#
#
# ACROPOLIS_PAYLOAD_MASTER['scheduling_options'] = {
#     u'optimize_scheduling': True,
#     u'force_imaging': False,
#     u'task_priority': 80,
#     u'skip_resource_spec_match': False,
#     u'upgrade': False,
#     u'retry_imaging': 2,
#     u'check_image_compatibility': True
# }
#
# ACROPOLIS_PAYLOAD_MASTER['patch_url'] = ''
#
# ACROPOLIS_PAYLOAD_MASTER['build_selection'] = USE_NOS_BY_COMMIT_ID
# ##### Specify Release Branch
# ACROPOLIS_PAYLOAD_MASTER['git'] = {
#         u'repo': u'main',
#         u'branch': AOS_REL_BRANCH
# }
#
# ACROPOLIS_PAYLOAD_MASTER['cluster_selection'] = {
#         u'pool_name': POOL_NAME,
#         u'by_node_pool': True
# }
#
# ACROPOLIS_PAYLOAD_MASTER[u'requested_hardware'] = {
#     u'hypervisor_version': u'branch_symlink',
#     u'hypervisor': u'kvm',
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'15',
#         u'redundancy_factor': u'default',
#         u'nos_url': NOS_URL,
#         u'secondary_datacenters': {
#             u'vsphere': {}
#         },
#         u'hypervisor_url': HYPERVISOR_URL
#     }
# }
#
# ACROPOLIS_PAYLOAD_MASTER['resource_manager_json'] = dict(PRISM_CENTRAL={
#     u'build': {
#         u'nos_build_url': PC_URL + PC_COMMIT_ID + '/' + BUILD_TYPE + '/'
#     }
# })
#
# ACROPOLIS_PAYLOAD_PC_MASTER = ACROPOLIS_PAYLOAD_MASTER.copy()
# ACROPOLIS_PAYLOAD_PC_NO_CLONE_MASTER = ACROPOLIS_PAYLOAD_PC_MASTER.copy()
# ACROPOLIS_PAYLOAD_NO_PC_MASTER = {k: v for (k, v) in ACROPOLIS_PAYLOAD_MASTER.items() if k != 'resource_manager_json'}
# ACROPOLIS_PAYLOAD_GPU_MASTER = ACROPOLIS_PAYLOAD_NO_PC_MASTER.copy()
#
#
# ACROPOLIS_PAYLOAD_SCALEOUT_PC_MASTER = ACROPOLIS_PAYLOAD_MASTER.copy()
# ACROPOLIS_PAYLOAD_SCALEOUT_PC_MASTER['tester_tags'] = [u'nutest', u'max_deployments__1', u'official']
# ACROPOLIS_PAYLOAD_SCALEOUT_PC_MASTER['cluster_selection'] = {
#     u'pool_name': SCALE_PC_POOL,
#     u'by_node_pool': True
# }
#
# # ACROPOLIS_PAYLOAD_GPU_MASTER['cluster_selection'] = {
# #     u'cluster_names': [u'gardenia'],
# #     u'by_names': True
# # }
#
#
# ACROPOLIS_PAYLOAD_GPU_MASTER['cluster_selection'] = {
#         u'pool_name': POOL_NAME,
#         u'by_node_pool': True
# }
#
# ACROPOLIS_PAYLOAD_VNUMA_MASTER = ACROPOLIS_PAYLOAD_NO_PC_MASTER.copy()
#
# # ACROPOLIS_PAYLOAD_VNUMA_MASTER['cluster_selection'] = {
# #     u'cluster_names': [u'cottonwood'],
# #     u'by_names': True
# # }
#
# ACROPOLIS_PAYLOAD_VNUMA_MASTER['cluster_selection'] = {
#     u'pool_name': POOL_NAME,
#     u'by_node_pool': True
# }
#
#
# ACROPOLIS_PAYLOAD_NO_PC_HA_MASTER = ACROPOLIS_PAYLOAD_NO_PC_MASTER.copy()
# ACROPOLIS_PAYLOAD_NO_PC_HA_MASTER[u'requested_hardware'] = {
#     u'hypervisor_version': u'branch_symlink',
#     u'hypervisor': u'kvm',
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'16',
#         u'nos_url': NOS_URL,
#         u'redundancy_factor': u'3',
#         u'secondary_datacenters': {
#             u'vsphere': {}
#         },
#         u'hypervisor_url': HYPERVISOR_URL
#     }
# }
#
# ACROPOLIS_PAYLOAD_NO_PC_MASTER[u'requested_hardware'] = {
#     u'hypervisor_version': u'branch_symlink',
#     u'hypervisor': u'kvm',
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'16',
#         u'nos_url': NOS_URL,
#         u'redundancy_factor': u'default',
#         u'secondary_datacenters': {
#             u'vsphere': {}
#         },
#         u'hypervisor_url': HYPERVISOR_URL
#     }
# }
#
# ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY = ACROPOLIS_PAYLOAD_PC_MASTER.copy()
# ACROPOLIS_PAYLOAD_PC_OVA_HYPERVISOR_ANY[u'requested_hardware'] = {
#     u'hypervisor_version': None,
#     u'hypervisor': None,
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'15',
#         u'nos_url': NOS_URL,
#         u'redundancy_factor': u'default',
#         u'secondary_datacenters': {
#             u'vsphere': {}
#         },
#         u'hypervisor_url': HYPERVISOR_URL
#     }
# }
#
# ACROPOLIS_PAYLOAD_PC_CATALOG_MASTER = ACROPOLIS_PAYLOAD_MASTER.copy()
# ACROPOLIS_PAYLOAD_PC_CATALOG_MASTER["emails"] = [u'velurusruthi.naidu@nutanix.com', u'bhawani.singh@nutanix.com',
#                                                  u'acropolis-catalog@nutanix.com', u'vivekanandan.k@nutanix.com',
#                                                  u'ritopa.dey@nutanix.com']
# # ACROPOLIS_PAYLOAD_PC_CATALOG_MASTER["emails"] = [u'muthu.kumaran@nutanix.com']
#
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MASTER = ACROPOLIS_PAYLOAD_PC_CATALOG_MASTER.copy()
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MASTER['tester_tags'] = [u'v3.1', u'nutest__resources', u'official', u'max_deployments__6']
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ANY_MASTER[u'requested_hardware'] = {
#     u'hypervisor_version': u'branch_symlink',
#     u'hypervisor': None,
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'15',
#         u'nos_url': NOS_URL,
#         u'redundancy_factor': u'default',
#         u'secondary_datacenters': {
#             u'vsphere': {}
#         },
#         u'hypervisor_url': ''
#     }
# }
#
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ESX_ANY_MASTER = ACROPOLIS_PAYLOAD_PC_CATALOG_MASTER.copy()
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ESX_ANY_MASTER['tester_tags'] = [u'v3.1', u'official', u'max_deployments__1']
# ACROPOLIS_PAYLOAD_PC_CATALOG_HYPERVISOR_ESX_ANY_MASTER[u'requested_hardware'] = {
#     u'hypervisor_version': None,
#     u'hypervisor': None,
#     u'imaging_options': {
#         u'datacenter': {
#             u'hyperv': {},
#             u'kvm': {},
#             u'vsphere': {},
#             u'use_host_names': False
#         },
#         u'foundation_build_url': FOUNDATION_BUILD_URL,
#         u'min_ram': u'15',
#         u'nos_url': NOS_URL,
#         u'redundancy_factor': u'default',
#         u'secondary_datacenters': {u'vsphere': {u'vcenters': [u'10.41.25.40']}},
#         u'hypervisor_url': ''
#     }
# }
#
#
# ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MASTER = ACROPOLIS_PAYLOAD_NO_PC_MASTER.copy()
# ACROPOLIS_PAYLOAD_SCHEDULER_OPT_MASTER['scheduling_options'] = {
#     u'optimize_scheduling': True,
#     u'force_imaging': False,
#     u'task_priority': 80,
#     u'skip_resource_spec_match': False,
#     u'upgrade': False,
#     u'retry_imaging': 2,
#     u'check_image_compatibility': True
# }
#
#
# ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER = ACROPOLIS_PAYLOAD_NO_PC_MASTER.copy()
# ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER['tester_tags'] = [u'v3.1', u'max_deployments__1', u'official']
#
# ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER['scheduling_options'] = {
#     u'optimize_scheduling': False,
#     u'force_imaging': False,
#     u'task_priority': 80,
#     u'skip_resource_spec_match': False,
#     u'upgrade': False,
#     u'retry_imaging': 2,
#     u'check_image_compatibility': True,
#     u'class_wise_scheduling': True
# }
# ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER['patch_url'] = u'https://gerrit.eng.nutanix.com/changes/309714/revisions/c222aead53bfc9b528f579f4f7b54c1166c010af/patch?zip'
# #ACROPOLIS_PAYLOAD_GUEST_OS_OPT_MASTER[u'emails'] = [u'bhawani.singh@nutanix.com']


from common_payload import MasterPayload
from constant import BUILD_NOS_URL, BUILD_HYPERVISOR_URL


class GOSLIPayload(MasterPayload):

    def __init__(self, **kwargs):
        # GlobalPayloadParameters.__init__(self)
        MasterPayload.__init__(self)
        self.THROTTLE_TAG = u'throttle_tests__1'

        self.nos_branch = kwargs.get("nos_branch")
        self.nos_commit = kwargs.get("nos_commit")
        self.nutest_commit = kwargs.get("nutest_commit", self.NUTEST_COMMIT)
        self.email_ids = kwargs.get("email_ids", self.EMAILS)
        self.task_priority = kwargs.get("priority", self.TASK_PRIORITY)
        self.post_run = kwargs.get("post_run", self.POST_RUN)
        self.pre_run = kwargs.get("pre_run", self.PRE_RUN)
        self.retry_imaging = kwargs.get("retry_imaging", self.RETRY_IMAGING)
        self.build_type = kwargs.get("build_type", self.BUILD_TYPE)
        self.nutest_patch = kwargs.get('nutest_patch', self.NUTEST_PATCH)
        self.foundation_url = kwargs.get("foundation_build_url", self.FOUNDATION_BUILD_URL)
        self.hypervisor_url = kwargs.get("hypervisor_url", self.HYPERVISOR_URL)
        self.nos_url = kwargs.get("nos_url", self.NOS_URL)

    def load_payload(self):
        super(GOSLIPayload, self).load_payload()
        return self.payload_map


    @property
    def get_scheduling_options(self):
        self.SCHEDULING_OPTIONS = {
            u'optimize_scheduling': True,
            u'force_imaging': False,
            u'task_priority': self.task_priority,
            u'skip_resource_spec_match': False,
            u'upgrade': False,
            u'retry_imaging': self.retry_imaging,
            u'check_image_compatibility': True,
            u'class_wise_scheduling': True
        }
        return self.SCHEDULING_OPTIONS

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
            u'min_host_cpu_cores': 56,
            u'min_host_gb_ram': 140,
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



