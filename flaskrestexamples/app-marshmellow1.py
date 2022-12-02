from flask import Flask
from flask_sqlalchemy import SQLAlchemy # new
from flask_marshmallow import Marshmallow # new
from flask_restful import Api, Resource # new
	

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # new
db = SQLAlchemy(app) # new
ma = Marshmallow(app) # new
api = Api(app) # new

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(255))

    def __repr__(self):
        return 'ID:{},Title:{},Author:{}'.format(self.id,self.title,self.author)


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")
        model = Post

post_schema = PostSchema()
posts_schema = PostSchema(many=True)

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return posts_schema.dump(posts)

    # new
    def post(self):
        new_post = Post(
            title=request.json['title'],
            content=request.json['content']
        )
        db.session.add(new_post)
        db.session.commit()
        return post_schema.dump(new_post)

    def patch(self, post_id):
        post = Post.query.get_or_404(post_id)

        if 'title' in request.json:
            post.title = request.json['title']
        if 'content' in request.json:
            post.content = request.json['content']

        db.session.commit()
        return post_schema.dump(post)

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)
        db.session.delete(post)
        db.session.commit()
        return '', 204

api.add_resource(PostListResource, '/posts')
api.add_resource(PostListResource, '/posts/<int:post_id>')


if __name__ == '__main__':
    app.run(debug=True)
