import requests

def test_getUsers():
    r = requests.get('http://127.0.0.1:5001/users')
    resultAtt = '[{"adresse":"45 rue de la fillaudière","codeP":"44840","complementAdresse":null,"genre":"Monsieur","id":1,"mail":"test@test.com","password":"test","pseudo":"test","role":"admin","telephone":"0240152585","ville":"Les sorinières"},{"adresse":"3 rue de hotel de ville","codeP":"44100","complementAdresse":null,"genre":"Madame","id":2,"mail":"florian@civel.com","password":"aze","pseudo":"florian","role":"user","telephone":"0618002677","ville":"Nantes"}]'
    assert r.text == resultAtt

def test_Exist():
    r = requests.post("http://127.0.0.1:5001/login", json={"pseudo": "test","password": "test"})
    resultAtt = 200
    assert r.status_code == resultAtt
def test_NotExist():
    r = requests.post("http://127.0.0.1:5001/login", json={"pseudo": "FAUX","password": "INCORRECT"})
    resultAtt = 401
    assert r.status_code == resultAtt

def test_getUser():
    r = requests.get('http://127.0.0.1:5001/user/1')
    resultAtt = '["adresse":"45 rue de la fillaudière","codeP":"44840","complementAdresse":null,"genre":"Monsieur","id":1,"mail":"test@test.com","password":"test","pseudo":"test","role":"admin","telephone":"0240152585","ville":"Les sorinières"]'
    assert r.text == resultAtt

def test_UserDelete():
    r = requests.delete("http://127.0.0.1:5001/user/1")
    resultAtt = 'User with the id 1 has been deleted'
    assert r.text == resultAtt

def test_InsertUser():
    r = requests.post("http://127.0.0.1:5001/users", json={"pseudo": "deux","mail": "deux@test.com","password": "deux"})
    resultAtt = 'User with the id 2 created successful'
    assert r.text == resultAtt  

def test_getUsersFin():
    r = requests.get('http://127.0.0.1:5001/users')
    resultAtt = '[{"id":2,"mail":"deux@test.com","password":"deux","pseudo":"deux"}]\n'
    assert r.text == resultAtt