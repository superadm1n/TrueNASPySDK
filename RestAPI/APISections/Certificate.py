from RestAPI.APISections import BaseSection


class BootPool(BaseSection):

    @property
    def num_certs(self):
        return self.session.get('/sertificate', json={'count': True})