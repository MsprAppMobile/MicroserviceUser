from flask import Blueprint,request,jsonify,json
from DatabaseManager.connection import db_connection

user_api = Blueprint('user_api',__name__)



@user_api.route('/users', methods=['GET','POST'])
def users() :
    conn = db_connection()
    cursor = conn.cursor()
    if request.method=='GET':
        cursor.execute("SELECT * FROM user")
        users = [
            dict(id=row[0],pseudo = row[1], mail=row[2], password=row[3], telephone=row[4], genre=row[5], codeP=row[6], ville=row[7], adresse=row[8], complementAdresse=row[9],role=row[10])
            for row in cursor.fetchall()
        ]
        if users is not None :
            cursor.close()
            conn.close()
            return jsonify(users),200

    if request.method =='POST':
        data = request.get_json()
        print('test')
        pseudo = data['pseudo']
        mail = data['mail']
        password = data['password']
        telephone = data['telephone']
        genre = data['genre']
        codeP = data['codeP']
        ville = data['ville']
        adresse = data['adresse']
        complementAdresse = data['complementAdresse']
        role = data['role']
        sql = """INSERT INTO user (pseudo,mail,password,telephone,genre,codeP,ville,adresse,complementAdresse,role) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """
        cursor.execute(sql,(pseudo,mail,password,telephone,genre,codeP,ville,adresse,complementAdresse,role))
        conn.commit()
        cursor.close()
        conn.close()
        return f"User with the id {cursor.lastrowid} created successful"

@user_api.route('/user/<int:id>',methods=['GET','PUT','DELETE'])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM user WHERE id =%s",(int(id)))
        rows = cursor.fetchall()
        for r in rows :
            user = r
        if user is not None :
            cursor.close()
            conn.close()
            return jsonify(user),200
        else :
            cursor.close()
            conn.close()
            return "Something wrong",405

    if request.method == 'PUT':
        data = request.get_json()
        role = data ['role']
        sql = """UPDATE  user SET role = %s WHERE id=%s; """
        cursor.execute(sql,(role,int(id)))
        conn.commit()
        cursor.close()
        conn.close()
        return "User with the id {} has been modify".format(id),200

    if request.method == 'DELETE':
        sql = """ DELETE FROM user WHERE id=%s """
        cursor.execute(sql,(int(id),))
        conn.commit()
        cursor.close()
        conn.close()
        return "User with the id {} has been deleted".format(id),200
