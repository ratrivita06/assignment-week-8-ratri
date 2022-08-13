import pymongo
from datetime import datetime
from flask import Flask,request

app = Flask(__name__)


@app.route('/ratri',methods=['POST'])
def entry_isi():
    dt = datetime.now()

    client = pymongo.MongoClient("mongodb+srv://ratrivitap:smaciho1@cluster0.2ah5ecq.mongodb.net/?retryWrites=true&w=majority")
    db = client['ratri_8']
    my_collections = db['tugas_8']

    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
   
    tugas = {'kecepatan': kecepatan,
            'latitude' : latitude,
            'longitude' : longitude,
            'timestamp' : dt
            }

    result = my_collections.insert_many([tugas])
    return ('data sudah disimpan') 


if __name__ == '__main__':
         app.run(debug=True)