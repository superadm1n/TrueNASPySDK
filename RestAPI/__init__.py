from RestAPI.Base import TrueNASBase
from RestAPI.APISections.Sharing import Sharing


class TrueNAS(TrueNASBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sharing = Sharing(self)