from RestAPI.APISections import BaseSection


class CertificateAuthority(BaseSection):

    @property
    def num_authorities(self):
        return self.session.get('/certificateauthority', json={'count': True})

    @property
    def get_info(self, **params):
        return self.session.get('/certificateauthority', json=params)

    def create_ca(self, **params):
        return self.session.post('/certificateauthority', json=params)

    def get_ca(self, id, **params):
        return self.session.get(f'/certificateauthority/id/{id}', json=params)

    def delete_ca(self, id):
        return self.session.delete(f'/certificateauthority/id/{id}')

    def update_ca(self, id, **params):
        return self.session.put(f'/certificateauthority/id/{id}', json=params)

    def ca_sign_csr(self, **params):
        return self.session.post('/certificateauthority/ca_sign_csr', json=params)

    def ca_profiles(self):
        return self.session.get('/certificateauthority/profiles')