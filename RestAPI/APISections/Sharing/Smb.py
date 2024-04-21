from RestAPI.APISections import BaseSection


class Smb(BaseSection):

    @property
    def all_shares(self):
        return self.session.get('/sharing/smb').json()

    @property
    def presets(self):
        return self.session.get('/sharing/smb/presets').json()

    def create_share(self, params):

        pass

    def delete_share(self, id):
        pass

    def get_share(self, id):
        return self.session.get(f'/sharing/smb/id/{id}')

    def update_share(self, id):
        pass

