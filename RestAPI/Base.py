from requests import Session


def construct_url(func):
    """
    Decorator that will rewrite the URL to query on the TrueNAS server and prepend the base URL
    provide to the TrueNASBase object to any URL provided.
    :param func:
    :return:
    """

    def wrapper_func(self, *args, **kwargs):
        if kwargs.get('url'):
            uri = kwargs.get('url')
            kwargs['url'] = self.base_url + uri
        else:
            uri = args[0]
            tmp = list(args)
            tmp[0] = self.base_url + uri
            args = tuple(tmp)

        return func(self, *args, **kwargs)

    return wrapper_func


class TrueNASBase(Session):

    def __init__(self, api_key, host, api_version='2.0', verify=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.verify = verify
        self.headers = {'Authorization': f'Bearer {api_key}'}
        self.base_url = f'https://{host}/api/v{api_version}'

    @construct_url
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs).json()

    @construct_url
    def put(self, *args, **kwargs):
        return super().get(*args, **kwargs).json()

    @construct_url
    def delete(self, *args, **kwargs):
        return super().delete(*args, **kwargs).json()

    @construct_url
    def post(self, *args, **kwargs):
        return super().post(*args, **kwargs).json()
