ENDOR_PC_BUILD_URL = u'http://endor.dyn.nutanix.com/builds/PC-builds/'
MASTER_KWARGS = {
    "branch": "MASTER",
    "nos_branch": "master",
    "nos_commit": "a89356cd97a7517e541c6f88f8b8db4797f160a0",
    "build_type": 'release'
}
KWARGS_5_18 = {

}

# GOS_PATCH_MASTER = u'https://gerrit.eng.nutanix.com/changes/379816/revisions/27ebe5c9daeebd81563273efb4c7b1788dfc1df8/patch?zip'
GOS_PATCH_MASTER = u'https://gerrit.eng.nutanix.com/changes/379816/revisions/053841191e99b66ea07ced221a25e1ffd79fee9e/patch?zip'
BUILD_NOS_URL = 'http://builds.dyn.nutanix.com/nos-builds/{0}/{1}/x86_64/release/tar/cvm/'
BUILD_PC_URL = 'http://endor.dyn.nutanix.com/builds/PC-builds/{0}/{1}/{2}/'
BUILD_HYPERVISOR_URL = 'http://phx-eo-filer-prod-1.corp.nutanix.com/GoldImages/NestAHV/ahv_images/nested-ahv-20180802.97.qcow2'