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
		self.create_user(user_name,user_age,user_email,user_id)

	def create_user(self,user_name,user_age,user_email,user_id):
		print (db.users.find_one({'ID':self.user_id}, {'ID': True, '_id': False}))
		user_exists = db.users.find_one({'ID':self.user_id}, {'ID': True, '_id': False})
		email_exists = db.users.find_one({'ID':self.user_id}, {'e-mail': True, '_id': False})
		if user_exists:
			print ("User ID already exist please try another")
			return 0
		elif email_exists:
			print("e-mail already in use try another")
			return 0
			
		db.users.insert_one(
			{
			'name':self.user_name,
			'age':self.user_age,
			'e-mail':self.user_email,
			'ID' : self.user_id
			})

class posts(user):
	def __init__(self, user, post_title,post_body,post_tags):
		self.post_title=post_title
		self.post_body=post_body
		self.post_tags=post_tags
		self.post_creator=user.user_name
		self.create_post(user, post_title,post_body,post_tags)

	def create_post(self, user, post_title,post_body,post_tags):
		date_for_post=datetime.datetime.now()
		db.posts.insert_one(
			{
				'title': self.post_title,
				'body': self.post_body,
				'author': user.user_name,
				'Created-on': date_for_post.strftime('%B %d, %Y %H:%M'),
				'tags':self.post_tags
			})
	def show_post(self):
		return (self.post_title, self.post_body, self.post_tags, self.post_creator)
class comment(posts):
	def __init__(self,comment_text):
		self.comment_text=comment_text
	def comment(self):
		db.comments.insert_one(
			{
			'body': self.comment_text,
			'commenter': user.user_name,
			'on-post': posts.post_title
			})
# if __name__=='__main__':
# 	main()

user1=user('Rafay',14,'sraff@gmail.com','srafayms')
post = posts(user1, "Title1", "Hello body", "#hashtag")
print (post.show_post())