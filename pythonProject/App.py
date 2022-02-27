from flask import Flask
from Materiel import Materiel
import json

app=Flask(__name__)

@app.route('/listeMateriels',methods=['GET','POST'])
def getAllMateriels():
    m=Materiel
    liste=m.getListe(m)
    return liste

if __name__=='__main__':
    app.run(host='0.0.0.0',port=105)