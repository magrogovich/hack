from flask import*
import json
import subprocess



app = Flask(__name__)


@app.route('/',methods=['GET'])
def homepage():
    with open("coordinates.txt","r") as data:
        coord = data.read().split('\n')
        print(coord)

    dataset = {
	'id':'002',
        'lat':coord[0],
        'lng':coord[1],
	'speed':coord[2],
	'sat':coord[3]
	
    }
    json_dump = json.dumps(dataset)
    return json_dump



if __name__ == '__main__':

    app.run(host='192.168.1.186', port=7777)
