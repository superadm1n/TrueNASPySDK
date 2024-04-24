from RestAPI.APISections import BaseSection


class Auth(BaseSection):

    @property
    def num_active_auth_sessions(self):
        return self.session.get('/auth/sessions', params={'count': True})

    def check_password(self, username, password):
        payload = {'username': username, 'password': password}
        return self.session.post('/auth/check_password', json=payload)

    def check_root_password(self, password):
        payload = {'username': 'root', 'password': password}
        return self.session.post('/auth/check_user', json=payload)

    def generate_auth_token(self, ttl, **kwargs):
        payload = {'ttl': ttl, 'attrs': kwargs}
        return self.session.post('/auth/generate_token', json=payload)

    def active_auth_sessions(self, **params):
        return self.session.get('/auth/sessions', params=params)

    def has_two_factor_auth(self):
        return self.session.get('/auth/two_factor_auth')
