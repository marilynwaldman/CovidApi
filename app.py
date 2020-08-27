#from elasticsearch import Elasticsearch, exceptions
#import os
#import time
#from flask import Flask, jsonify, request, render_template
#import sys
import requests
import json


def load_data_in_es():
    """ creates an index in elasticsearch """
    url = "https://services3.arcgis.com/66aUo8zsujfVXRIT/arcgis/rest/services/Community_Testing_Sites/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    #url = "http://data.sfgov.org/resource/rqzj-sfat.json"
    r = requests.get(url)
    data = r.json()
    print("Loading data in elasticsearch ...")
    #print(json.dumps(data, indent=2))
    #ßprint(data)
    #print(json.dumps(data['features'], indent=2))
    for id, site in enumerate(data['features']):
      res = es.index(index="codata", doc_type="site", id=id, body=site)
    print("Total sites loaded: ", len(data['features']))



load_data_in_es()
