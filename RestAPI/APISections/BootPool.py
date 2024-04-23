from RestAPI.APISections import BaseSection


class BootPool(BaseSection):

    @property
    def disks(self):
        return self.session.get('/boot/get_disks').json()

    @property
    def scrub_interval(self):
        return self.session.get('/boot/get_scrub_interval').json()

    @property
    def state(self):
        return self.session.get('/boot/get_state').json()

    def attach_disk(self, dev, **options):
        return self.session.post('/boot/attach', json={'dev': dev, 'options': options}).json()

    def detach_disk(self, disk):
        return self.session.post('/boot/detach', json=disk).json()

    def replace(self, label, dev):
        return self.session.post('/boot/replace', json={'label': label, 'dev': dev}).json()

    def scrub(self):
        return self.session.get('/boot/scrub').json()

    def set_scrub_interval(self, num_days):
        return self.session.post('/boot/set_scrub_interval', json=num_days).json()
