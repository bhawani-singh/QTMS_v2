"""
Copyright (c) 2020 Nutanix Inc. All rights reserved.
Author: bhawani.singh@nutanix.com

"""
from job_profile import *
from gos_payload import GOSPayload
from gos_linux_install_payload import GOSLIPayload
from pc_payload import PCPayload
from catalog_pc_payload import CatalogPCPayload
from catalog_pe_payload import CatalogPEPayload
from catalog_pc_config_1_payload import CatalogPC_1Payload
from scheduler_payload import SchedulerPayload
from pe_payload import PEPayload
from pe_ui_payload import PEUIPayload
from qtms import QTMS
from constant import *
from pprint import pprint


class BaseRunner(QTMS):

    def __init__(self, ops, **kwargs):
        QTMS.__init__(self)
        self.branch = kwargs.get("branch")
        self.nos_branch = kwargs.get("nos_branch")
        self.nos_commit = kwargs.get("nos_commit")
        self.build_type = kwargs.get("build_type")
        self.job_profiles = []
        self.jita_operations = []

    def update_job_profile_payload(self):
        self.jita_operations = [{
            'op': 'update_job_profile'
        }]
        for jp_category in BRANCH_METADATA[self.branch].keys():
            kwargs = {'nos_branch': self.nos_branch, 'nos_commit': self.nos_commit,
                      'nos_url': BUILD_NOS_URL.format(self.nos_branch, self.nos_commit),
                      'hypervisor_url': BUILD_HYPERVISOR_URL,
                      }

            if jp_category == "NAHV-GOS-OPT":
                flag = False
                # flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSPayload(**gos_kwargs)
                    # pprint(gos_payload.load_payload())

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-GOS":
                flag = False
                flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSPayload(**gos_kwargs)
                    # print("GOS Payload --> {}".format(gos_local_payload.load_payload()))
                    # pprint(gos_payload.load_payload())

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-PC":
                flag = False
                flag = True

                if flag:
                    pc_kargs = kwargs.copy()
                    pc_kargs['pc_url'] = BUILD_PC_URL.format(self.nos_branch, self.nos_commit, self.build_type)
                    pc_local_payload = PCPayload(**pc_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pc_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-CATALOG-PE":
                flag = False
                flag = True

                if flag:
                    pe_kargs = kwargs.copy()
                    pe_local_payload = CatalogPEPayload(**pe_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-CATALOG-PC":
                flag = False
                flag = True

                if flag:
                    pc_kargs = kwargs.copy()
                    pc_kargs['pc_url'] = BUILD_PC_URL.format(self.nos_branch, self.nos_commit, self.build_type)
                    pc_local_payload = CatalogPC_1Payload(**pc_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pc_local_payload.load_payload()
                    }])


            if jp_category == "NAHV-SCHEDULER":
                flag = False
                flag = True

                if flag:
                    sched_kargs = kwargs.copy()
                    sched_local_payload = SchedulerPayload(**sched_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': sched_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-PE":
                flag = False
                flag = True

                if flag:
                    pe_kargs = kwargs.copy()
                    pe_local_payload = PEPayload(**pe_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-GOT-OPT-1-NODE":
                flag = False
                # flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSLIPayload(**gos_kwargs)
                    # pprint(gos_payload.load_payload())
                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-UI":
                flag = False
                flag = True

                if flag:
                    pe_ui_kargs = kwargs.copy()
                    pe_ui_local_payload = PEUIPayload(**pe_ui_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_ui_local_payload.load_payload()
                    }])

        self.execute_qtms_ops()


    def trigger_job_profiles(self):
        self.jita_operations = [{
            'op': 'trigger_job_profile'
        }]
        for jp_category in BRANCH_METADATA[self.branch].keys():
            kwargs = {'nos_branch': self.nos_branch, 'nos_commit': self.nos_commit,
                      'nos_url': BUILD_NOS_URL.format(self.nos_branch, self.nos_commit),
                      }
            if jp_category == "NAHV-GOS-OPT":
                flag = False
                flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSPayload(**gos_kwargs)
                    # pprint(gos_payload.load_payload())

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-GOT-OPT-1-NODE":
                flag = False
                flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSLIPayload(**gos_kwargs)
                    # pprint(gos_payload.load_payload())
                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-GOS":
                flag = False
                # flag = True

                if flag:
                    gos_kwargs = kwargs.copy()
                    gos_kwargs['nutest_patch'] = GOS_PATCH_MASTER
                    gos_local_payload = GOSPayload(**gos_kwargs)
                    # pprint(gos_payload.load_payload())

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': gos_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-PC":
                flag = False
                # flag = True

                if flag:
                    pc_kargs = kwargs.copy()
                    pc_kargs['pc_url'] = BUILD_PC_URL.format(self.nos_branch, self.nos_commit, self.build_type)
                    pc_local_payload = PCPayload(**pc_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pc_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-CATALOG-PE":
                flag = False
                # flag = True

                if flag:
                    pe_kargs = kwargs.copy()
                    pe_local_payload = CatalogPEPayload(**pe_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-CATALOG-PC":
                flag = False
                # flag = True

                if flag:
                    pc_kargs = kwargs.copy()
                    pc_kargs['pc_url'] = BUILD_PC_URL.format(self.nos_branch, self.nos_commit, self.build_type)
                    pc_local_payload = CatalogPC_1Payload(**pc_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pc_local_payload.load_payload()
                    }])


            if jp_category == "NAHV-SCHEDULER":
                flag = False
                # flag = True

                if flag:
                    sched_kargs = kwargs.copy()
                    sched_local_payload = SchedulerPayload(**sched_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': sched_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-PE":
                flag = False
                # flag = True

                if flag:
                    pe_kargs = kwargs.copy()
                    pe_local_payload = PEPayload(**pe_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_local_payload.load_payload()
                    }])

            if jp_category == "NAHV-UI":
                flag = False
                # flag = True

                if flag:
                    pe_ui_kargs = kwargs.copy()
                    pe_ui_local_payload = PEUIPayload(**pe_ui_kargs)

                    self.job_profiles.extend([{
                        'jps': BRANCH_METADATA[self.branch][jp_category],
                        'payload': pe_ui_local_payload.load_payload()
                    }])

        self.execute_qtms_ops()

    def clone_job_profiles(self):
        pass

    def kill_jita_tasks(self):
        pass

    def send_report(self):
        pass

    def add_job_profiles(self):
        pass


if __name__ == '__main__':
    qtms_operations = [
        'update_job_profiles_payload',
        # 'trigger_job_profiles'
    ]

    br = BaseRunner(qtms_operations, **MASTER_KWARGS)
    for op in qtms_operations:
        if op == 'update_job_profiles_payload':
            br.update_job_profile_payload()
        if op == 'trigger_job_profiles':
            br.trigger_job_profiles()
