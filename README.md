Creare un semplice sito (frontend e backend) con Python, Flask, Html, CSS e Javascript e caricarlo su pythonanywhere

1. Creare una cartella dove salvare i file del programma

2. Installare virtualenv

python3 -m pip install virtualenv

Nel mio caso è stato installato nella seguente directory:
/Users/giu/Library/Python/3.10/bin

NB: se lo si inserisce nel PATH non sarà necessario digitare tutto il path; io non lo farò in quanto non è un'azione che si svolge spesso

3. Entrare nella cartella dove si vuole posizionare il codice e creare un ambiente virtuale

/Users/giu/Library/Python/3.10/bin/virtualenv env

(env è il nome dato all'ambiente virtuale)

4. Attivare l'ambiente virtuale

Per il Mc si usa la seguente istruzione:

source env/bin/activate

Il prompt dei comandi dovrebbe evidenziare che si è all'interno dell'ambiente virtuale env

(env) giu@Air-di-Giu pythonanywhere %

5. Installare Flask nell'ambiente virtuale

pip install flask

6. Avviare flask

flask run

7. Aprire l'indirizzo internet evidenziato

env) giu@Air-di-Giu pythonanywhere % flask run

- Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
- Debug mode: off
- Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
