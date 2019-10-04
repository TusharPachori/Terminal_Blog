import datetime
import uuid

from Terminal_blog.database import Database
from Terminal_blog.models.post import Post


class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id


    def new_post(self):
        title = input("Enter Post Title: ")
        content = input("Enter Post Content: ")
        date = input("Enter Post Date(leave blank for current date) Format(DDMMYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            data = datetime.datetime.strptime(date, "%d%m%y")
        post = Post(blogid=self.id,
                    title=title,
                    content=content,
                    create_date=date,
                    author=self.author)

        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection="blogs",
                        data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def get_from_mongo(cls, id):
        blog_data = Database.find_one(collection="blogs",
                                      query={'id': id})

        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
