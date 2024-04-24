from RestAPI.APISections import BaseSection


class BootEnv(BaseSection):

    def get_info(self, **params):
        '''
        Query all Boot Environments with query-filters and query-options.

        :param params:
        :return:
        '''
        return self.session.get('/bootenv', json=params)

    def create_env(self, name, source):
        '''
        Create a new boot environment using name.
        If a new boot environment is desired which is a clone of another boot environment, source can be passed.
        Then, a new boot environment of name is created using boot environment source by cloning it.Ensure that
        name and source are valid boot environment names.

        :param name:
        :param source:
        :return:
        '''
        return self.session.post('/bootenv', json={'name': name, 'source': source})

    def delete_env(self, id):
        '''
        Delete id boot environment. This removes the clone from the system.

        :param id:
        :return:
        '''
        return self.session.delete(f'/bootenv/id/{id}')

    def get_env(self, id, **params):
        '''
        Query all Boot Environments with query-filters and query-options.

        :param id:
        :param params:
        :return:
        '''
        return self.session.get(f'/bootenv/id/{id}', json=params)

    def update_env(self, id, name):
        '''
        Update id boot environment name with a new provided valid name.

        :param id:
        :param name:
        :return:
        '''
        return self.session.put(f'/bootenv/id/{id}', json={'name': name})

    def activate_env(self, id):
        '''
        Activates boot environment id.

        :param id:
        :return:
        '''
        return self.session.post(f'/bootenv/id/{id}/activate')

    def set_attribute(self, id, keep):
        '''


        :param id:
        :param keep:
        :return:
        '''
        return self.session.post(f'/bootenv/id/{id}/ste_attribute', json={'keep': keep})



