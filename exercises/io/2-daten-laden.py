import json


def laden(dateiname):
    with open(dateiname) as f:
        datensammlung = json.load(f)
        return datensammlung['teilnehmer:innen']


teilnehmer = laden('daten.json')
print(teilnehmer)
