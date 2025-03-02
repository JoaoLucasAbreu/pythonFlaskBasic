from src.models import db
from src.models.post import Post
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de author e incluir um apelido ao get para evitar conflito com o get do post
from src.services.author_service import get as get_author

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Post
###

def create(data):
    try:

        title = data.get('title')
        if not title:
            json_abort(400,"title is required")

        subtitle = data.get('subtitle')
        if not subtitle:
            json_abort(400,"subtitle is required")

        author_id = data.get('author_id')
        if not author_id:
            json_abort(400,"author_id is required")

        author = get_author(author_id)
 
        created = datetime.datetime.now()

        post = Post(title=title, subtitle=subtitle ,created=created , author_id=author_id,author=author)
        db.session.add(post)
        db.session.commit()

        return post

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        post = Post.query.filter_by(id=id).first()

        if not post:
            json_abort(400,"Post not found")
        else:
            return post

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        post = Post.query.filter_by(id=id).first()

        if not post:
            json_abort(400,"Post not found")
        else:

            title = data.get('title')
            if not title:
                json_abort(400,"title is required")
                
            subtitle = data.get('subtitle')
            if not subtitle:
                json_abort(400,"subtitle is required")
 
            post.title = title
            post.subtitle = subtitle
            
            db.session.commit()
        
            return post

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        post = Post.query.filter_by(id=id).first()

        if not post:
            json_abort(400,"Post not found")
        else:
            db.session.delete(post)
            db.session.commit()
        
            return post

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)