import requests, os
from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    pass



@app.route('/search_weather', methods=['GET','POST'])
def search_weather():
    
    if request.method == "POST":
        location = request.form['location'].replace(' ', '+')
        if location:
            api_key = os.environ.get('GoogleMapAPIKey')
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&key=' + api_key
            resp = requests.get(url)

            if resp.status_code != 200 or  resp.json()['status'] == 'ZERO_RESULTS':
                return render_template("index.html")
            else:
                resp_cord = resp.json()['results'][0]['geometry']['location']
                lat = resp_cord['lat']
                lon = resp_cord['lng']
                return redirect(url_for('weather', location=location, lat=lat, lon=lon))
    else:
        return render_template("index.html")


@app.route('/weather')
def weather():
    location = request.args['location'].replace('+', ' ')
    lat = request.args['lat']
    lon = request.args['lon']
    API_key = os.environ.get('OpenWeather_API_key')
    url = 'https://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_key
    resp = requests.get(url)

    if resp.status_code == 200 and len(resp.text) > 0:
        weather = resp.json()['weather'][0]['description']
        max_temp = resp.json()['main']['temp_max']
        min_temp = resp.json()['main']['temp_min']
        return render_template("result.html", location=location, weather=weather, max_temp=max_temp, min_temp=min_temp)
    else:
        return render_template("index.html")




if __name__ == '__main__':
    app.run()