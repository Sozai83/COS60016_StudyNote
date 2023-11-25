from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


app = Flask(__name__)

db_name = r'.\db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>Successful connection'
    except Exception as er:
        error_text = '<p>The error:<br/>' + str(er) + '</p>'
        state = '<h1>Connection unsuccessful</h1>'
        return state + error_text


if __name__ == '__main__':
    app.run(debug=True)