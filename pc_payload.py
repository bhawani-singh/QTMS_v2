
from common_payload import MasterPayload
from constant import BUILD_NOS_URL, BUILD_HYPERVISOR_URL


class PCPayload(MasterPayload):

    def __init__(self, **kwargs):
        # GlobalPayloadParameters.__init__(self)
        MasterPayload.__init__(self)

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
        self.pc_url = kwargs.get("pc_url", self.PC_URL)

    def load_payload(self):
        super(PCPayload, self).load_payload()
        self.payload_map[u'resource_manager_json'] = self.get_pc_url
        return self.payload_map