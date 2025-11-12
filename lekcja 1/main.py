#rzut

from flask import Flask , render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/rzut")
def rzutmoneta():
    rzutmoneta = ["orzeł","reszka"]
    wynik = random.choice(rzutmoneta)
    
    if wynik == 'orzeł':
        img = "https://pressmania.pl/wp-content/uploads/2020/12/moneta-2-zl.jpg"
    else:
        img = "https://cdn.galleries.smcloud.net/t/galleries/gf-zggJ-gtQ7-m7EP_rzut-moneta-mniej-sprawiedliwy-niz-sadzono-664x442.jpg" 
    
    return render_template("rzut.html",wynik=wynik , img=img)
        

    



@app.route("/ciekawostka")
def ciekawostka():
    facts_list = ["Większość osób cierpiących na uzależnienie technologiczne doświadcza silnego stresu, gdy znajdują się poza zasięgiem sieci lub nie mogą korzystać ze swoich urządzeń.",
                  "Według badania przeprowadzonego w 2018 roku ponad 50% osób w wieku od 18 do 34 lat uważa się za zależne od swoich smartfonów.",
                  "Badanie zależności technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych.",
                  "Według badania z 2019 r. ponad 60% osób odpowiada na wiadomości służbowe na swoich smartfonach w ciągu 15 minut po wyjściu z pracy."]

    ciekawostka = random.choice(facts_list)
    return render_template("ciekawostka.html", ciekawostka=ciekawostka)


app.run(debug=True)

