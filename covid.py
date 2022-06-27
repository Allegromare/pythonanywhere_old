# 1. Import the requests library
import requests, csv
URL_COVID_ITALIA = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"


def download_nuovi_positivi():

    nuovi_positivi = [[], []]

    # 2. download the data behind the URL
    response = requests.get(URL_COVID_ITALIA)

    if response.status_code != 200:
        print("Download dei dati non riuscito")
    else:
        fileCovid = csv.reader(response.text.strip().split("\n"))
        next(fileCovid)
        for record in fileCovid:
            nuovi_positivi.append([record[0], record[8]])

    print(nuovi_positivi[[0][0]])
    
    return nuovi_positivi