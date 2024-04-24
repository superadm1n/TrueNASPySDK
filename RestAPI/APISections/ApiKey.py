from RestAPI.APISections import BaseSection


class ApiKey(BaseSection):

    @property
    def number_of_keys(self):
        return self.session.get('/api_key', params={'count': True})

    def get_key(self, id):
        return self.session.get(f'/api_key/id/{id}')

    def list_keys(self, **params):
        return self.session.get('/api_key', params=params)

    def create_key(self, name):
        return self.session.post('/api_key', json={'name': name})

    def delete_key(self, id):
        return self.session.delete(f'/api_key/id/{id}')

    def update_key_name(self, id, name):
        return self.session.put(f'/api_key/id/{id}', json={'name': name, 'reset': True})
