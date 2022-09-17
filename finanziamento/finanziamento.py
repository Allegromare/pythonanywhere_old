import math
import json


# FUNZIONI
# --------
def calcolaRataFinanziamento(importo, anni, tasso):
    tasso = tasso / 100.0
    mesi = 12  # rate per anno
    numeroRate = mesi * anni  # numero delle rate da pagare
    temp = math.pow(1 + (tasso / mesi), (numeroRate))

    return importo * (temp) * (tasso / mesi) / (temp - 1)


def checkImporto(importo):
    try:
        int(importo)
    except ValueError:
        print("Inserire un valore intero per l'importo (senza punti migliaia)")
        return False

    print(importo)
    if IMPORTO_FIN_MIN <= int(importo) <= IMPORTO_FIN_MAX:
        return True
    else:
        return False


def checkAnni(anni):
    return True


def checkRegione(regione):
    return True


def caricaConfigurazioni():
    with open("config_fin.json") as config_file:
        config_json = json.load(config_file)

    return config_json


# MAIN
# ----

# CONFIGURAZIONI
# --------------

caricaConfigurazioni()
IMPORTO_FIN_MIN = int(caricaConfigurazioni["importoFinanziamentoMin"])
IMPORTO_FIN_MAX = int(caricaConfigurazioni["importoFinanziamentoMax"])
print()
TASSI_REGIONI = {"Lombardia": 1, "Lazio": 2, "Campania": 3}

a = input("Importo: ")
print(checkImporto(a))

imp = int(input("Importo finanziamento (euro): "))


an = int(input("Durata finanziamento (anni): "))
# tas = float(input("Tasso di interesse (punti %): "))
reg = input("Regione dove l'azienda ha la sede legale: ")


tas = float(TASSI_REGIONI[reg])

# Si usa la funzione round(r,2) per limitare i calcoli alla seconda cifra decimale
# Se non usassimo round() i calcoli verrebero effettuati utilizzando tutti i decimali del float e potremmo avere un numero superiore quando si usa r in altre formule
# ES: non usando round() per un finanziamento di 10.900 di 3 anni al 2%, r sarebbe 312,2041081837678; la rata mensile mostrata 312,20, ma l'importo totale delle rate
# (importo complessivo da pagare) sarebbe 11.239,35 che è leggermente maggiore di 312,20 * 3 anni * 12 mesi = 11.239,20 in quanto nel mostrare r è stato preso il valore
# con due decimali, nella formula per calcolare il totale delle r è stato utilizzato r con tutti i decimali previsti dal float

r = round(calcolaRataFinanziamento(imp, an, tas), 2)

print()
print("Numero rate: ", an * 12)
print(f"Tasso annuale: {tas}%")
print("Importo rata mensile : {:.2f} euro".format(r))
print(r)
print("Importo complessivo da pagare : {:.2f} euro".format(an * 12 * r))
print("Costo del finanziamento : {:.2f} euro".format(an * 12 * r - imp))
