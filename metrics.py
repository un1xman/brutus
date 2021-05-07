#!/usr/bin/python
from flask import Flask, request
import os
import requests
APP = Flask(__name__)
API_ENDPOINT = os.getenv('CONSUL_METRICS_ENDPOINT') #"http://10.0.80.10:31013/v1/agent/metrics?format=prometheus"
head = {'X-Consul-Token': os.getenv('CONSUL_TOKEN')} #'82432f00-6288-cd93-aeed-c70fa0983217'
@APP.route('/metrics',methods=['GET'])
def main():
    response = requests.get(API_ENDPOINT, headers=head).content
    return response
APP.run(host='0.0.0.0', port=5000)
