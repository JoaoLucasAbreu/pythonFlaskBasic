from flask_restplus import fields
from src.config.restplus import api


post_request = api.model('Post Request', {
    'title': fields.String(required=True, description='Title of the post'),
    'subtitle': fields.String(required=True, description='Subtitle of the post'),
    'author_id': fields.Integer(required=True, description='Author Id of the post')
})

post_result = api.model('Post Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'title': fields.String(required=True, description='Title of the post'),
    'subtitle': fields.String(required=True, description='Subtitle of the post'),
    'author_id': fields.Integer(required=True, description='Post author Id'),
    'created': fields.String(required=True, description='Date post created')
})
