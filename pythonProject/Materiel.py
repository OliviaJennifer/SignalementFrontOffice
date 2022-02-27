import collections

from Connexion import Connexion

import json
import pyodbc


class Materiel:
    def __init__(self,id,nom,tension,intensite,prix,marge,dateFabrication):
        self._id=id
        self._nom=nom
        self._tension=tension
        self._intensite=intensite
        self._prix=prix
        self._marge=marge
        self._dateFabrication

    def getId(self):
        return self._id
    def setId(self,id):
        self._id=id

    def getNom(self):
        return self._nom
    def setNom(self,nom):
        self._mon=nom

    def getTension(self):
        return self._tension
    def setTension(self,tension):
        self._tension=tension

    def getIntensite(self):
        return self._intensite
    def setIntensite(self,intensite):
        self._intensite=intensite

    def getPrix(self):
        return self._prix
    def setPrix(self,prix):
        self._prix=prix

    def getMarge(self):
        return self._marge
    def setMarge(self,marge):
        self._marge=marge

    def getDateFabrication(self):
        return self._dateFabrication
    def setDateFabrication(self,dateFabrication):
        self._dateFabrication=dateFabrication

    def getListe(self):
        liste=[]
        req="select * from VraiMateriel"
        connection=Connexion()
        con=Connexion.getConnexion(connection)
        cursor=con.cursor()
        try:
            stmt= con.cursor()
            stmt.execute(req)
            for s in stmt:
                d=collections.OrderedDict()
                d["id"]=s[0]
                d["nom"]=s[1]
                d["tension"]=s[2]
                d["intensite"]=s[3]
                d["prix"]=s[4]
                d["marge"]=s[5]
                d["dateFabrication"]=s[6]

                liste.append(d)
            print(liste)
            j=json.dumps(liste)
            return j
        except Exception as e:
            print(e)

    def getListeM(self):
        liste = []
        req = "select * from VraiMateriel"
        connection = Connexion
        con = Connexion.getConnexion(connection)
        liste.append(("id","nom","tension","intensite","prix","marge","dateFabrication"))
        try:
            stmt = con.cursor()
            stmt.execute(req)
            for s in stmt:
                m=(s[0], s[1], s[2], s[3], s[4], s[5],s[6])
                liste.append(m)
        except Exception as e:
            print(e)
        return liste









