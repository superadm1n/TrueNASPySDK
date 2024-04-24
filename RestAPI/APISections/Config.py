from RestAPI.APISections import BaseSection


class Config(BaseSection):

    def reset(self, reboot):
        return self.session.post('/config/reset', json={'reboot': reboot})