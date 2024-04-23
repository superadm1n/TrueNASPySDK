from RestAPI.APISections import BaseSection


class TwoFactor(BaseSection):

    @property
    def provisioning_uri(self):
        return self.session.get('/auth/twofactor/provisioning_uri').json()

    def get_info(self):
        return self.session.get('/auth/twofactor').json()

    def update_twofactor(self, **kwargs):
        return self.session.put('/auth/twofactor', json=kwargs).json()

    def renew_secret(self):
        return self.session.get('/auth/twofactor/renew_secret').json()

    def verify_token(self, token):
        return self.session.post('/auth/twofactor/verify', json=token).json()