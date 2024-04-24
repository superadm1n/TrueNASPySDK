from RestAPI.APISections import BaseSection


class ActiveDirectory(BaseSection):

    @property
    def info(self):
        return self.session.get('/activedirectory')

    @property
    def nss_info_choices(self):
        return self.session.get('/activedirectory/nss_info_choices')

    @property
    def started(self):
        return self.session.get('/activedirectory/started')

    @property
    def state(self):
        return self.session.get('/activedirectory/get_state')

    def domain_info(self, domain):
        return self.session.post('/activedirectory/domain_info', json=domain)

    def leave(self, username, password):
        return self.session.post('/activedirectory/leave', json={'username': username, 'password': password})

    def update_domain_info(self, **kwargs):
        return self.session.put('/activedirectory', json=kwargs)
