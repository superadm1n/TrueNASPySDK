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

    @property
    def alert_classes(self):
        return self.session.get('/alertclasses').json()

    @property
    def alert_service_types(self):
        return self.session.get('/alertservice/list_types').json()

    def test_alert_service(self, **kwargs):
        return self.session.post('/alertservice/test', json=kwargs).json()

    def get_alert_services(self, limit, offset, count, sort):
        params = {'limit': limit, 'offset': offset, 'count': count, 'sort': sort}
        return self.session.get('/alertservice', params=params).json()

    def get_alert_service(self, id):
        return self.session.get(f'/alertservice/id/{id}').json()

    def update_alert_service(self, id, **kwargs):
        return self.session.put(f'/alertservice/id/{id}', json=kwargs).json()

    def create_alert_service(self, **kwargs):
        return self.session.post('/alertservice', json=kwargs).json()

    def delete_alert_service(self, id):
        return self.session.delete(f'/alertservice/id/{id}').json()

    def udpate_alert_classes(self, kwargs):
        return self.session.put('/alertclasses', json=kwargs).json()

    def restore_alert(self, id):
        return self.session.post('/alert/restore', json=id).json()

    def dismiss_alert(self, id):
        return self.session.post('/alert/dismiss', json=id).json()
