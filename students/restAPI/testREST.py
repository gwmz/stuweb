#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import requests

HEADER = {'Content-Type':'application/json'}

def test_indexAPI():
    apiurl = "http://127.0.0.1:8000/rest/v1/indexAPI"
    r=requests.get(apiurl,headers=HEADER)
    print r.status_code
    print r.text
    
def test_cardAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/cardAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_familyAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/familyAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_gradeAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/gradeAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_healthyAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/healthyAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_sleepAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/sleepAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_testAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/testAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
def test_timelineAPI(quest):
    apiurl = "http://127.0.0.1:8000/rest/v1/timelineAPI"
    data = json.dumps(quest)
    r=requests.get(apiurl,data=data,headers=HEADER)
    print r.status_code
    print r.text
    
if __name__ == '__main__':
    test_indexAPI()
    test_cardAPI("123456")
    test_familyAPI("123456")
    test_timelineAPI("123456")
    test_testAPI("123456")
    test_sleepAPI("123456")
    test_healthyAPI("123456")
    test_gradeAPI("123456")
