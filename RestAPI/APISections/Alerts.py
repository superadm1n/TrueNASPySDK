from RestAPI.APISections import BaseSection


class Alerts(BaseSection):

    @property
    def all_alerts(self):
        return self.session.get('/alert/list').json()

    @property
    def categories(self):
        return self.session.get('/alert/list_categories').json()

    @property
    def policies(self):
        return self.session.get('/alert/list_policies').json()

    def restore_alert(self, id):
        return self.session.post('/alert/restore', json=id).json()

    def dismiss_alert(self, id):
        return self.session.post('/alert/dismiss', json=id).json()
