from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json


app = Flask(__name__)

MONGOD_HOST = 'localhost'
MONGOD_PORT = 27017
DBS_NAME = 'donorsUSA'
COLLECTION_NAME = 'projects'
FIELDS = {'funding_status': True, 'school_state': True, 'resource_type': True, 'poverty_level': True,
          'date_posted': True, 'total_donations': True, '_id': False
}


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/donorUS/projects")
def donor_projects():
    connection = MongoClient(MONGOD_HOST, MONGOD_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(projection=FIELDS, limit=87000)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    json_projects = json.dumps(json_projects)
    connection.close()
    return json_projects



if __name__ == '__main__':
    app.run(debug=True)
