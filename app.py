# -*- coding: utf-8 -*-
"""
Created on Tue May 11 10:54:07 2021

@author: harsha
"""

# Importing the necessary Libraries
from flask_cors import CORS,cross_origin
from flask import Flask, render_template, request,jsonify
from scrapperImage.ScrapperImage import ScrapperImage
from businesslayer.BusinessLayerUtil import BusinessLayer
import os

# import request
app = Flask(__name__) # initialising the flask app with the name 'app'


@app.route('/')  # route for redirecting to the home page
@cross_origin()
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000) # port to run on local machine
   #app.run(debug=True) # to run on cloud