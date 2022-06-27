# 1. Import the requests library
import requests, csv

URL_COVID_ITALIA = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"

# 2. download the data behind the URL
response = requests.get(URL_COVID_ITALIA)

if response.status_code != 200:
    print("Download dei dati non riuscito")
else:
    #fileCovid = csv.reader(response.text.strip().split("\n"))
    #next(fileCovid)
    #for record in fileCovid:
    #    giorno = record[0]
    #    nuoviPositivi = record[8]
    #    print("Giorno: " + giorno)
    #    print("Numero Nuovi Positivi: " + nuoviPositivi)

    fileCovid = csv.DictReader(response.text)
    
    # scrive i dati in una nuova lista con solamente data e numero positivi
    
    for row in fileCovid:
        giorno = row[data]
        nuoviPositivi = row[nuovi_positivi]
        print("Giorno: " + giorno)
        print("Numero Nuovi Positivi: " + nuoviPositivi)


    