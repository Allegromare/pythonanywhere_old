# 1. Import the requests library
import requests, csv
URL_COVID_ITALIA = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"


def download_nuovi_positivi():

    # nuovi_positivi = [[], []]

    nuovi_positivi_inverso = {}

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:
        fileCovid = csv.reader(response.text.strip().split("\n"))
        next(fileCovid)
        for row in fileCovid:
            #nuovi_positivi.append([row[0], row[8]])
            nuovi_positivi_inverso[row[0][: 10]] = row[8]
    
    nuovi_positivi = dict(reversed(list(nuovi_positivi_inverso.items())))
    
    return nuovi_positivi
