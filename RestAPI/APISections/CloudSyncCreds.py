from RestAPI.APISections import BaseSection


class CloudSyncCreds(BaseSection):

    @property
    def num_creds(self):
        return self.session.get('/cloudsync/credentials', json={'count': True})

    def credentials(self, **params):
        return self.session.get('/cloudsync/credentials', json=params)

    def create_credentials(self):
        return self.session.post('/cloudsync/credentials')

    def delete_credentials(self, id):
        return self.session.delete(f'/cloudsync/credentials/id/{id}')

    def get_credential(self, id, **params):
        return self.session.get(f'/cloudsync/credentials/id/{id}', json=params)

    def update_credentials(self, id, **params):
        return self.session.put(f'/cloudsync/credentials/id/{id}', json=params)

    def verify_credentials(self, **params):
        return self.session.post('/cloudsync/credentials/verify', json=params)