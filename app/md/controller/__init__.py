from flask_restful import Api
from flask import Blueprint

from app.md.controller.notes import Noteview
md_blueprint=Blueprint('md',__name__,url_prefix='md')
api=Api(md_blueprint)

api.add_resource(Noteview,'/note/')