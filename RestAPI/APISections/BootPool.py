from RestAPI.APISections import BaseSection


class BootPool(BaseSection):

    @property
    def disks(self):
        return self.session.get('/boot/get_disks')

    @property
    def scrub_interval(self):
        return self.session.get('/boot/get_scrub_interval')

    @property
    def state(self):
        return self.session.get('/boot/get_state')

    def attach_disk(self, dev, **options):
        return self.session.post('/boot/attach', json={'dev': dev, 'options': options})

    def detach_disk(self, disk):
        return self.session.post('/boot/detach', json=disk)

    def replace(self, label, dev):
        return self.session.post('/boot/replace', json={'label': label, 'dev': dev})

    def scrub(self):
        return self.session.get('/boot/scrub')

    def set_scrub_interval(self, num_days):
        return self.session.post('/boot/set_scrub_interval', json=num_days)
