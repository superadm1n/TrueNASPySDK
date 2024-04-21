from RestAPI.Base import TrueNASBase


class BaseSection:

    def __init__(self, api_session):
        print(type(api_session))
        if not isinstance(api_session, TrueNASBase):
            raise TypeError('api_session must be an instance of TrueNASBase')
        self.session = api_session