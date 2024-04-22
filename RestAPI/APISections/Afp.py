from RestAPI.APISections import BaseSection


class Afp(BaseSection):

    @property
    def info(self):
        return self.session.get('/afp').json()

    @property
    def bindip_choices(self):
        return self.session.get('/afp/bindip_choices').json()

    def update_afp(self, **kwargs):
        return self.session.put('/afp', json=kwargs).json()
