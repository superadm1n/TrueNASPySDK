from RestAPI.APISections import BaseSection


class CloudSync(BaseSection):

    @property
    def num_tasks(self):
        return self.session.get('/cloudsync', json={'count': True})

    def get_tasks(self, **params):
        return self.session.get('/cloudsync', json=params)

    def new_cloudsync(self, **params):
        return self.session.post('/cloudsync', json=params)

    def delete_cloudsync(self, id):
        return self.session.post(f'/cloudsync/{id}')

    def get_cloudsync(self, id, **params):
        return self.session.get(f'/cloudsync/{id}', json=params)

    def update_cloudsync(self, id, **params):
        return self.session.put(f'/cloudsync/{id}', json=params)

    def abort_cloudsync_task(self, id):
        return self.session.post(f'/cloudsync/id/{id}/abort')

    @property
    def common_task_schema(self):
        return self.session.get(f'/cloudsync/common_task_schema')

    @property
    def list_buckets(self):
        return self.session.post('/cloudsync/list_buckets')

    @property
    def list_directory(self):
        return self.session.post('/cloudsync/list_directory')

    @property
    def list_onedrive_drives(self):
        return self.session.post('/cloudsync/onedrive_list_drives')

    @property
    def providers(self):
        return self.session.get('/cloudsync/providers')

    def restore(self, id):
        return self.session.post(f'/cloudsync/id/{id}/restore')

    def sync(self, id):
        return self.session.post(f'/cloudsync/id/{id}/sync')

    def sync_onetime(self):
        return self.session.post(f'/cloudsync/sync_onetime')



