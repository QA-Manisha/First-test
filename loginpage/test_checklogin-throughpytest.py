import allure
import pytest
import requests
import json
supply_url='https://bookeats.co'

def test_login_valid():
	url = supply_url + "/login/"
	data = {'email':'chef1@yopmail.com','password':'admin786'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['token'] == "xuioWVI9Ur7jwUDeQdgCLmqn5l8rsHTssKkVqd5c", resp.text

# def test_login_no_password(supply_url):
# 	url = supply_url + "/login/"
# 	data = {'email':'chef1@yopmail.com'}
# 	resp = requests.post(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 400, resp.text
# 	assert j['error'] == "Missing password", resp.text
#
# def test_login_no_email(supply_url):
# 	url = supply_url + "/login/"
# 	data = {}
# 	resp = requests.post(url, data=data)
# 	j = json.loads(resp.text)
# 	assert resp.status_code == 400, resp.text
# 	assert j['error'] == "Missing email or username", resp.text