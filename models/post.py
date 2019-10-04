import uuid
import datetime
from Terminal_blog.database import Database


class Post(object):

    def __init__(self, blogid, title, content, author, create_date=datetime.datetime.utcnow(), id=None):
        self.blogid = blogid
        self.title = title
        self.content = content
        self.author = author
        self.create_date = create_date
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        Database.insert(collection= 'posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blogid': self.blogid,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'create_date': self.create_date
        }

    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one('posts', {'id': id})
        return cls(blogid=post_data['blogid'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   create_date=post_data['create_date'],
                   id=post_data['id'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find('posts', {'blogid': id})]