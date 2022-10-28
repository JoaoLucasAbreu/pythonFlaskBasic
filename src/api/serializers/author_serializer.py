from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.post_serializer import post_result

author_request = api.model('Author Request', {
    'name': fields.String(required=True, description='Name of the author') ,
    'age': fields.Integer(required=True, description='Age of the author')
})

author_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Author Id'),
    'name': fields.String(required=True, description='Name of the author'), 
    'age': fields.Integer(required=True, description='Age of the author') 
    
})

author_posts_result = api.model('Author Post Result', {
    'id': fields.Integer(required=True, description='Author Id'),
    'name': fields.String(required=True, description='Name of the author'), 
    'age': fields.Integer(required=True, description='Age of the author'),
    'posts': fields.List(fields.Nested(post_result), required=True, description='Age of the author')
    
})
