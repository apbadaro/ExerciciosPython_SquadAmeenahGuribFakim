from flask import Flask, render_template
import urllib.request as ur
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


app = Flask(__name__)


# JSON COM TODOS OS PERSONAGENS
@app.route("/")
def get_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = ur.urlopen(url)
    data = response.read()
    characters_data = json.loads(data)

    return render_template("characters.html", characters=characters_data["results"])


# LISTA DE TODOS OS PERSONAGENS
@app.route("/lista")
def get_characters():
    with ur.urlopen("https://rickandmortyapi.com/api/character/") as url:
        response = url.read()
        characters_list = json.loads(response)
        characters = []

        for character in characters_list["results"]:
            character = {
                "name": character["name"],
                "status": character["status"],
            }
            characters.append(character)

        return {"characters": characters}


# PERFIL DE CADA PERSONAGEM
@app.route("/profile/<id>")
def get_profile(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = ur.urlopen(url)
    data = response.read()
    character_profile = json.loads(data)

    return render_template("profile.html", profile=character_profile)


# LISTA DE TODOS OS EPISÓDIOS: Jessica Souza


# PERFIL DE CADA EPISÓDIO: Monique Cristina Cerqueira de Souza Mendes


# LISTA DE TODAS AS LOCALIZAÇÕES: Marcia Moreira


# PERFIL DE CADA LOCALIZAÇÃO: Ana Paula Badaró
@app.route("/location/<id>")
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    try:
        response = ur.urlopen(url)
        data = response.read()
        location_profile = json.loads(data)
        # "location.html" -> ALTERAR PARA O NOME DA URL CERTA!!
        return render_template("location.html", location=location_profile)

    except Exception as e:
        return f"Erro inesperado: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
