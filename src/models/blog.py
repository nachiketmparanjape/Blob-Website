import uuid
import datetime

from src.common.database import Database
from src.models.post import Post



class Blog(object):
    def __init__(self, author, title, description, aurhor_id, _id=None):
        self.author = author
        self.author_id =
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        #title = input("Enter Post title: ")
        #content = input("Enter post content: ")
        #date = input("Enter post date, or leave blank for today (in format DDMMYYYY:")

        post = Post(blog_id = self._id,
                    title = title,
                    content = content,
                    author = self.author,
                    created_date = date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        return Database.insert(collection = 'blogs',
                                  data = self.json())
    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self._id
        }

    @classmethod
    def from_mongo(cls,_id):
        blog_data = Database.find_one(collection='blogs',
                                      query = {'_id':id})

        return cls(**blog_data)

        """cls(author = blog_data['author'],
            title = blog_data['title'],
            description = blog_data['description'],
            _id = blog_data['_id'])"""

