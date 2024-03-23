import datetime
import json
# from re import A
from flask import abort, jsonify, make_response, request, session
from flask_restful import Resource
from app import app
print('--------------------->...............')
from app.md.models import User
import jwt
from werkzeug.security import check_password_hash
from app.md.serilizer import UserSchema
class LoginView(Resource):
    def post(self):
        credentials=request.get_json()
        user=User.query.filter_by(username=credentials["username"]).first()
        # user = UserSchema().dump(user/\)
        if not user:
            abort(401)

        if not check_password_hash(user._password,credentials["password"]):
            print(user._password,credentials["password"])
            abort(401)
        session['user_id']=user.id
        token = jwt.encode({'user_id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'token' : token})
        
        
