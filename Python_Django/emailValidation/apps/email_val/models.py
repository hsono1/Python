from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class EmailManager(models.Manager):
	def emailValidation(self, postdata):
		errors = []
		regexEmail = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if len(postdata['user_email']) < 1:
			errors.append("Email too short")
		elif not regexEmail.match(postdata['user_email']):
			errors.append("Not a valid email")
		elif  len(self.filter(email=postdata['user_email'])) > 0:
			errors.append("Email already exists")
		else:
			emails = self.create(email=postdata['user_email'])
			return (True, emails)
		return (False, errors)




class Email(models.Model):
	email = models.EmailField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True) 
	updated_at = models.DateTimeField(auto_now=True)
	objects = EmailManager()