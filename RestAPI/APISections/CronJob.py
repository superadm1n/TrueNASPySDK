from RestAPI.APISections import BaseSection


class CronJob(BaseSection):

    @property
    def num_jobs(self):
        return self.session.get('/cronjob', json={'count': True})

    @property
    def jobs(self, **params):
        return self.session.get('/cronjob', json=params)

    def new_job(self, **params):
        return self.session.post('/cronjob', json=params)

    def delete_job(self, id):
        return self.session.delete(f'/cronjob/id/{id}')

    def get_job(self, id, **params):
        return self.session.get(f'/cronjob/id/{id}', json=params)

    def update_job(self, id, **params):
        return self.session.put(f'/cronjob/id/{id}', json=params)

    def run_job(self, id, skip_disabled):
        return self.session.post('/cronjob/run', json={'id': id, 'skip_disabled': skip_disabled})