# -*- coding: UTF-8 -*-
"""
Baby's First Flask App for CloudFoundry

Author: Adam Duston
License: See LICENSE.txt
"""

from flask import Flask
import os
import json

app = Flask(__name__)
# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("VCAP_APP_PORT", 9099))
methods = ('GET', 'POST')
@app.route('/', methods=methods)
def hello_world():
    return 'Hello! This is an instance of the Python Demo app for CloudFoundry. I am instance ' + str(os.getenv("CF_INSTANCE_INDEX", 0))

@app.route('/map/', methods=methods)
def map_():
    return 'ok'
@app.route('/map/query' , methods=methods)
@app.route('/map/search' , methods=methods)
def map_query():
    return getfilecontent('data/map.txt')

@app.route('/workhour_15/', methods=methods)
def workhour_15_():
    return 'ok'
@app.route('/workhour_15/query', methods=methods)
@app.route('/workhour_15/search', methods=methods)
def workhour_15_query():
    return getfilecontent('data/workhour_15.txt')


@app.route('/dayworkhour/', methods=methods)
def dayworkhour_():
    return 'ok'
@app.route('/dayworkhour/query', methods=methods)
@app.route('/dayworkhour/search', methods=methods)
def dayworkhour_query():
    return getfilecontent('data/dayworkhour.txt')


@app.route('/dayworkequnum/', methods=methods)
def dayworkequnum_():
    return 'ok'
@app.route('/dayworkequnum/query', methods=methods)
@app.route('/dayworkequnum/search', methods=methods)
def dayworkequnum_query():
    return getfilecontent('data/dayworkequnum.txt')

@app.route('/totalequnum/')
def total_equ_num_():
    return 'ok'
@app.route('/totalequnum/query', methods=methods)
@app.route('/totalequnum/search', methods=methods)
def totalequnum_query():
    return getfilecontent('data/totalequnum.txt')


@app.route('/workpercent_15/', methods=methods)
def workpercent_15_():
    return 'ok'
@app.route('/workpercent_15/query', methods=methods)
@app.route('/workpercent_15/search', methods=methods)
def workpercent_15_query():
    return getfilecontent('data/workpercent_15.txt')


@app.route('/list/')
def list_():
    return 'ok'
@app.route('/list/search',  methods=methods)
@app.route('/list/query',  methods=methods)
def list_query():
    data = getfilecontent('data/list.txt')
    json_data = data.replace('北京市北京市','北京市').replace('天津市天津市','天津市').replace('重庆市重庆市','重庆市').replace('上海市上海市','上海市')
    return json_data


@app.route('/totalequnum_offline/')
def totalequnum_offline_():
    return 'ok'
@app.route('/totalequnum_offline/search',  methods=methods)
@app.route('/totalequnum_offline/query',  methods=methods)
def totalequnum_offline_query():
    return getfilecontent('data/totalequnum_offline.txt')

@app.route('/totalequnum_online/')
def totalequnum_online_():
    return 'ok'
@app.route('/totalequnum_online/search',  methods=methods)
@app.route('/totalequnum_online/query',  methods=methods)
def totalequnum_online_query():
    return getfilecontent('data/totalequnum_online.txt')

@app.route('/totalequnum_sleep/')
def totalequnum_sleep_():
    return 'ok'
@app.route('/totalequnum_sleep/search',  methods=methods)
@app.route('/totalequnum_sleep/query',  methods=methods)
def totalequnum_sleep_query():
    return getfilecontent('data/totalequnum_sleep.txt')



# @app.route('/params/test')
# def list_params():
#     message = request.args.get('provice')
#     response = requests.get('http://localhost/api/?provinceName=' + message).text
#     print('response:{}'.format(response))
#     print('message:{}'.format(message))
#     return response


def getfilecontent(filename):
    file_object = open(filename)
    try:
        file_content = file_object.read()
    finally:
        file_object.close()
    return file_content


if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
