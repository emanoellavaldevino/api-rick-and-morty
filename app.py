from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters_page():
    
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])


@app.route("/profile/<id>")
def get_profile(id):
    
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)


@app.route("/lista")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        }

        characters.append(character)

    return {"characters": characters}


@app.route("/locations/")
def get_location():

    url = "https://rickandmortyapi.com/api/location" 
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    location = []

    for locations in dict["results"]:
        locations = {
            "name": locations["name"],
            "status": locations["type"],
            "dimension": locations["dimension"]
        }

        location.append(locations)
    
    return render_template("location.html", locations=dict["results"])

@app.route("/location/<id>")
def get_location_id(id):
    
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("location.html", get_location=dict)

@app.route("/episodes")
def get_episode():

    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    episode = []

    for episodes in dict["results"]:
        episodes = {
             "name": episodes["name"],
             "air_date": episodes["air_date"],
             "episode": episodes["episode"]
        }

        episode.append(episodes)

    return render_template("episodes.html", episodes=dict["results"])

@app.route("/episode/<id>")
def get_episode_id(id):
    
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    episodes_id = []

    for episode_id in dict["results"]:
        episodes_id = {
            "name": episodes_id["name"],
            "air_date": episodes_id["air_date"],
            "episode": episodes_id["episode"],
            
        }
          
        episodes_id.append(episode_id)

    return {"episodes_id": episode_id}

if __name__ == "__main__":
    app.run(debug=True)

