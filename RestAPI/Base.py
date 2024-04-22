from requests import Session


class TrueNASBase(Session):

    def __init__(self, api_key, host, api_version='2.0', verify=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verify = verify
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.base_url = f'https://{host}/api/v{api_version}'

    def _construct_url(self, *args, **kwargs):
        if kwargs.get('url'):
            uri = kwargs.get('url')
            kwargs['url'] = self.base_url + uri
        else:
            uri = args[0]
            tmp = list(args)
            tmp[0] = self.base_url + uri
            args = tuple(tmp)

        return args, kwargs

    def get(self, *args, **kwargs):
        args, kwargs = self._construct_url(*args, **kwargs)
        return super().get(*args, **kwargs)

    def put(self, *args, **kwargs):
        args, kwargs = self._construct_url(*args, **kwargs)
        return super().get(*args, **kwargs)

    def delete(self, *args, **kwargs):
        args, kwargs = self._construct_url(*args, **kwargs)
        return super().delete(*args, **kwargs)

    def post(self, *args, **kwargs):
        args, kwargs = self._construct_url(*args, **kwargs)
        return super().post(*args, **kwargs)




