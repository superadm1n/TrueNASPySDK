from RestAPI.Base import TrueNASBase
from RestAPI.APISections.Sharing import Sharing
from RestAPI.APISections.ActiveDirectory import ActiveDirectory
from RestAPI.APISections.Afp import Afp
from RestAPI.APISections.Alerts import Alerts
from RestAPI.APISections.ApiKey import ApiKey
from RestAPI.APISections.Auth import Auth
from RestAPI.APISections.TwoFactor import TwoFactor
from RestAPI.APISections.BootPool import BootPool
from RestAPI.APISections.BootEnv import BootEnv
from RestAPI.APISections.Certificate import Certificate
from RestAPI.APISections.CertificateAuthority import CertificateAuthority
from RestAPI.APISections.CloudSync import CloudSync
from RestAPI.APISections.CloudSyncCreds import CloudSyncCreds
from RestAPI.APISections.Config import Config
from RestAPI.APISections.CronJob import CronJob


class TrueNAS(TrueNASBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sharing = Sharing(self)
        self.active_directory = ActiveDirectory(self)
        self.afp = Afp(self)
        self.alerts = Alerts(self)
        self.api_key = ApiKey(self)
        self.authentication = Auth(self)
        self.two_factor = TwoFactor(self)
        self.boot_pool = BootPool(self)
        self.boot_env = BootEnv(self)
        self.certificate = Certificate(self)
        self.certificate_authority = CertificateAuthority(self)
        self.cloudsync = CloudSync(self)
        self.cloudsync_creds = CloudSyncCreds(self)
        self.config = Config(self)
        self.cronjob = CronJob(self)


