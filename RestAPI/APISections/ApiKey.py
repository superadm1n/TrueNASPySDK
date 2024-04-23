from RestAPI.APISections import BaseSection


class ApiKey(BaseSection):

    @property
    def number_of_keys(self):
        return self.session.get('/api_key', params={'count': True}).json()

    def get_key(self, id):
        return self.session.get(f'/api_key/id/{id}').json()

    def list_keys(self, **params):
        return self.session.get('/api_key', params=params).json()

    def create_key(self, name):
        return self.session.post('/api_key', json={'name': name}).json()

    def delete_key(self, id):
        return self.session.delete(f'/api_key/id/{id}').json()

    def update_key_name(self, id, name):
        return self.session.put(f'/api_key/id/{id}', json={'name': name, 'reset': True}).json()
