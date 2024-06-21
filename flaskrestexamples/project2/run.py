from flask_restful import Api
from app.resources import BookListResource
from app import create_app

app = create_app()
api = Api(app)

api.add_resource(BookListResource, "/books")

if __name__ == '__main__':
    app.run()
