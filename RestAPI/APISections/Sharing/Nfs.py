from RestAPI.APISections import BaseSection


class Nfs(BaseSection):

    @property
    def all_shares(self):
        return self.session.get('/sharing/nfs').json()

    @property
    def human_identifier(self):
        return self.session.get('/sharing/nfs/human_identifier').json()

    def create_share(self, params):
        pass

    def delete_share(self, id):
        pass

    def get_share(self, id):
        return self.session.get(f'/sharing/nfs/id/{id}').json()

    def update_share(self, id):
        pass

