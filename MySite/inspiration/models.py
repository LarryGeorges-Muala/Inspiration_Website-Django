from django.db import models
from django.utils import timezone
# Create your models here.

class Author_Name(models.Model):
	
	author_name_value = models.CharField(max_length=200)
	
	def __str__(self):
		return self.author_name_value
		

class Author_text(models.Model):
	
	author_name_text_reference = models.ForeignKey(Author_Name, on_delete=models.CASCADE)
	author_text_value = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.author_text_value
	
	

class Full_text(models.Model):
	
	author_name_text_reference = models.ForeignKey(Author_Name, on_delete=models.CASCADE)
	full_text_value = models.CharField(max_length=1000)
	
	def __str__(self):
		return self.full_text_value

	
	
class Author_pic(models.Model):

	author_name_pic_reference = models.ForeignKey(Author_Name, on_delete=models.CASCADE)
	author_pic_value = models.CharField(max_length=500)
	
	def __str__(self):
		return self.author_pic_value
	

class Author_url(models.Model):

	author_name_url_reference = models.ForeignKey(Author_Name, on_delete=models.CASCADE)
	author_url_value = models.CharField(max_length=500)
	
	def __str__(self):
		return self.author_url_value
		
