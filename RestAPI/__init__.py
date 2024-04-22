from RestAPI.Base import TrueNASBase
from RestAPI.APISections.Sharing import Sharing
from RestAPI.APISections.ActiveDirectory import ActiveDirectory
from RestAPI.APISections.Afp import Afp
from RestAPI.APISections.Alerts import Alerts


class TrueNAS(TrueNASBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sharing = Sharing(self)
        self.active_directory = ActiveDirectory(self)
        self.afp = Afp(self)
        self.alerts = Alerts(self)