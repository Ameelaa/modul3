
from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
    return przywitanie()

@app.route("/przywitanie")
def przywitanie():
    return """<h1>Hello</h1>
    <a href="/ciekawostka"> ciekawostka!</a>"""

@app.route("/ciekawostka")
def ciekawostka():
    facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
                  "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
                  "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
                  "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy."]

    return f"""<p>{random.choice(facts_list)}</p>
<a href="/przywitanie"> strona główna</a>"""

app.run(debug=True)

