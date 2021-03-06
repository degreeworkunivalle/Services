from django.apps import AppConfig
from actstream import registry


class UserConfig(AppConfig):
    name = 'users'
    verbose_name = "User"

    def ready(self):
        registry.register(
		self.get_model('User')
	)
