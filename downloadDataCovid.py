# 1. Import libraries
from pkg_resources import parse_version
import requests, csv, json

URL_COVID_ITALIA_CSV = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
URL_COVID_ITALIA_JSON = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json"
URL_COVID_REGIONI_JSON = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-regioni.json"

def download_nuovi_positivi_ita_csv():
    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA_CSV)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:
        fileCovid = csv.reader(response.text.strip().split("\n"))
        next(fileCovid)
        for row in fileCovid:
            nuovi_positivi_inverso[row[0][: 10]] = int(row[8])

    nuovi_positivi = dict(reversed(list(nuovi_positivi_inverso.items())))

    return nuovi_positivi


def download_nuovi_positivi_ita_json():
    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA_JSON)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:    
        responseJson = response.json()

        for record in responseJson:
            nuovi_positivi_inverso[record['data'][: 10]] = record['nuovi_positivi']

            print(record['data'][: 10] 
                + " " 
                + str(record['nuovi_positivi'])
                )

        nuovi_positivi = dict(reversed(list(nuovi_positivi_inverso.items())))

    return nuovi_positivi

def download_nuovi_positivi_lazio_json():
    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_REGIONI_JSON)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:    
        responseJson = response.json()

        for record in responseJson:
            
            if record['codice_regione'] == 12:
                nuovi_positivi_inverso[record['data'][: 10]] = record['nuovi_positivi']

                print(type(record['nuovi_positivi']))

                print(record['data'][: 10] 
                    + " " 
                    + str(record['nuovi_positivi'])
                    + str(record['denominazione_regione'])
                    )

        nuovi_positivi = dict(reversed(list(nuovi_positivi_inverso.items())))

    return nuovi_positivi
