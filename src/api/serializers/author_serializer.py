from flask_restplus import fields
from src.config.restplus import api


author_request = api.model('Author Request', {
    'name': fields.String(required=True, description='Name of the author') ,
    'age': fields.Integer(required=True, description='Age of the author')
})

author_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Author Id'),
    'name': fields.String(required=True, description='Name of the author'), 
    'age': fields.Integer(required=True, description='Age of the author') 
    
})

""" author_post_result = api.model('Author Post Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'title': fields.String(required=True, description='Title of the post'),
    'subtitle': fields.String(required=True, description='Subtitle of the post'),
    'created': fields.String(required=True, description='Date post created')
    
})
 """