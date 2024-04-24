from RestAPI.APISections import BaseSection


class Certificate(BaseSection):

    @property
    def num_certs(self):
        return self.session.get('/certificate', json={'count': True})

    def get_info(self, **params):
        return self.session.get('/certificate', json=params)

    @property
    def acme_server_choices(self):
        return self.session.get('/certificate/acme_server_choices')

    @property
    def country_choices(self):
        return self.session.get('/certificate/country_choices')

    @property
    def ec_curve_choices(self):
        return self.session.get('/certificate/ec_curve_choices')

    @property
    def extended_key_usage_choices(self):
        return self.session.get('/certificate/extended_key_usage_choices')

    @property
    def key_type_choices(self):
        return self.session.get('/certificate/key_type_choices')

    @property
    def profiles(self):
        return self.session.get('/certificate/profiles')

    def create_cert(self, **kwargs):
        return self.session.post('/certificate', kwargs)

    def delete_cert(self, id):
        return self.session.delete(f'/certificate/id/{id}')

    def get_cert(self, id, **params):
        return self.session.get(f'/certificate/id/{id}', json=params)

    def update_cert(self, id, **params):
        return self.session.put(f'/certificate/id/{id}', json=params)

