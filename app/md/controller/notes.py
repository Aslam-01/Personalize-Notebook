from flask_restful import Resource
from app.md.models import User,Note
from app.md.serilizer import UserSchema,NotesSchema
from flask import Flask,request,session,jsonify
from app import db
from app.auth.decorator import token_required

class Noteview(Resource):
    @token_required
    def get(self):
        notes=Note.query.filter_by(user_id=self.id)
        print(notes)
        schema=NotesSchema(many=True).dump(notes)
        # for note in schema:
        #     note.pop('user_id',None)
        return schema
    
    @token_required
    def post(self):
        schema=NotesSchema().load(request.get_json())
        new_note=Note(data=schema['data'],user_id=session['user_id'])
        db.session.add(new_note)
        db.session.commit()
        return NotesSchema().dump(new_note)
    

    @token_required
    def put(self):
        data = request.get_json()
        note= Note.query.filter_by(id=data['id']).update(data)
        db.session.commit()
        return jsonify({"message":"data update"})
    

    @token_required
    def delete(self):
        data = request.get_json()
        Note.query.filter_by(id=data['id']).delete()
        db.session.commit()
        return jsonify({"mesage":"data deleted"})