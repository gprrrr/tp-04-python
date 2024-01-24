from flask import Flask, render_template, request
import json
import requests
import folium

app = Flask(__name__)


def get_bike_data():
    api_url = "https://opendata.lillemetropole.fr/api/explore/v2.1/catalog/datasets/vlille-realtime/records"
    params = {
            "limit": "100",
        }
    response = requests.get(api_url, params=params)
    data = response.json()["results"]

    filtered_data = [repo for repo in data if repo['etatconnexion'] == 'CONNECTÉ']

    return filtered_data


@app.route("/")
def index():

    user_latitude = 50.6292
    user_longitude = 3.0573

    bike_data = get_bike_data()

    map_center = [user_latitude, user_longitude]
    my_map = folium.Map(location=map_center, zoom_start=14)

    for record in bike_data:
        bike_count = record["nbvelosdispo"]
        place_count = record["nbplacesdispo"]
        station_location = [record["localisation"]["lat"], record["localisation"]["lon"]]

        marker_text = f"<b>Bikes:</b> {bike_count} <br> <b>Places:</b> {place_count}"
        folium.Marker(location=station_location, popup=marker_text).add_to(my_map)


    map_filename = "templates/map.html"
    my_map.save(map_filename)


    return render_template("index.html")

@app.route('/maps/map.html')
def show():
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
