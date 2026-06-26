import json


class SettingsService:

    def load(self):

        with open("data/settings.json", "r") as file:

            return json.load(file)


settings_service = SettingsService()