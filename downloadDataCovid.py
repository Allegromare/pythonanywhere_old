# 1. Import libraries
import requests, csv, json

URL_COVID_ITALIA_CSV = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
URL_COVID_ITALIA_JSON = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"

def download_nuovi_positivi_csv():
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


def download_nuovi_positivi_json():
    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA_JSON)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:
        response.json()
        fileCovid = json.loads(response.text)
        
        csv.reader(response.text.strip().split("\n"))
        next(fileCovid)
        for row in fileCovid:
            nuovi_positivi_inverso[row[0][: 10]] = int(row[8])

    nuovi_positivi_json = dict(reversed(list(nuovi_positivi_inverso.items())))

    return nuovi_positivi_json