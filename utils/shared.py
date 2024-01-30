class AppSettings(object):

    def __init__(self, init_dict=None):
        self._app_settings = init_dict if init_dict else {}

    def get(self, name, default_value=None):
        return self._app_settings.get(name, default_value)

    def set(self, name, value):
        self._app_settings[name] = value

    def update(self, items: dict):
        self._app_settings.update(items)


class AppContext(object):
    __app_settings = AppSettings()

    @classmethod
    def app_settings(cls, new_value: AppSettings = None):
        """

        :param new_value:
        :return:
        :rtype: AppSettings
        """
        if new_value:
            cls.__app_settings = new_value

        return cls.__app_settings

