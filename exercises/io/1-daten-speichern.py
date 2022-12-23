import json


def speichern(teilnehmer, dateiname):

    datensammlung = {}
    datensammlung['teilnehmer:innen'] = teilnehmer

    with open(dateiname, 'w') as f:
        json.dump(datensammlung, f)


teilnehmer = ['Anna', 'Bob', 'Theo', 'Karim', 'Robert']

speichern(teilnehmer, 'daten.json')
