from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import pandas as pd
import numpy as np
from locations import locations


app = Flask(__name__)
db_name = '../db/testdb.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Weather(db.Model):
   __tablename__ = 'merged_data'
   id = db.Column(db.Text, primary_key=True, name='field1')
   KWH = db.Column(db.Text, name='field4')


@app.route('/')
def home():
    try:
        usage = Weather.query.all()
        snow_text = '<ul>'
        for weather in usage:
            snow_text += '<li>' + weather.id + weather.KWH + '<li>'
        snow_text += '</ul>'
        return snow_text

    except Exception as er:
        error_text = '<p>The error:<br/>' + str(er) + '</p>'
        state = '<h1>Connection unsuccessful</h1>'
        return state + error_text        


locations_list = []

for location in locations:
    dict_location = locations[location]
    locations_list.append((dict_location['name'], dict_location['lat'],dict_location['lng']))


locations = pd.DataFrame(
    locations_list,
    columns= ['location','latitude','longitude']
)

locations.to_csv('./db/location_data.csv')



    

if __name__ == '__main__':
    app.run()
