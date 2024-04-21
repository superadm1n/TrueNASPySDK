from RestAPI.APISections import BaseSection
from RestAPI.APISections.Sharing.Smb import Smb
from RestAPI.APISections.Sharing.Nfs import Nfs


class Sharing(BaseSection):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.smb = Smb(self.session)
        self.nfs = Nfs(self.session)

