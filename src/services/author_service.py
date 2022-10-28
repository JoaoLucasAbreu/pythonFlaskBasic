from src.models import db
from src.models.author import Author
from src.models.post import Post
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do author
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"Name is required")
            
        age = data.get('age')
        if not age:
            json_abort(400,"Age is required")

 
        author = Author(name=name, age=age)
        db.session.add(author)
        db.session.commit()

        return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def getPosts(id):
    try:
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:
            posts = Post.query.filter_by(author_id=id).all()
            return {"id":author.id,
                    "name": author.name,
                    "age": author.age,
                    "posts": posts
                    }

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)
        
def get(id):
    try:
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400,"Name is required")
                
            age = data.get('age')
            if not age:
                json_abort(400,"Age is required")


            author.name = name
            author.age = age
            
            db.session.commit()
        
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:
            db.session.delete(author)
            db.session.commit()
        
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)