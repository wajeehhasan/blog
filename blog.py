import pymongo
import datetime


client=pymongo.MongoClient('mongodb://127.0.0.1:27018')



db=client.blog
class user:
	def __init__(self,user_name,user_age,user_email,user_id):
		self.user_name=user_name
		self.user_age=user_age
		self.user_email=user_email
		self.user_id=user_id

	def create_user(self,user_name,user_age,user_email,user_id)
		if db.users.find({'ID':self.user_id})['ID']==self.user_id:
			return "User ID already exist please try another"
		elif db.users.find({'ID':self.user_id})['e-mail']==self.user_email:
			return "e-mail already in use try another"
		db.users.insert_one(
			{
			'name':self.user_name,
			'age':self.user_age,
			'e-mail':self.user_email,
			'ID' : self.user_id
			})


class posts(user):
	def __init__(self,post_title,post_body,post_tags):
		self.post_title=post_title
		self.post_body=post_body
		self.post_tags=post_tags

	def create_post(self,post_title,post_body,post_tags):
		date_for_post=datetime.datetime.now()
		db.posts.insert_one(
			{
				'title': self.post_title,
				'body': self.post_body
				'author': user.user.user_name
				'Created-on': date_for_post.strftime('%B %d, %Y %H:%M')
				'tags':self.post_tags
			})
class comment(user,posts):
	def __init__(self,comment_text):
		self.comment_text=comment_text
	def comment(self):
		db.comments.insert_one(
			{
			'body': self.comment_text
			'commenter': user.user_name
			'on-post': posts.post_title
			})


