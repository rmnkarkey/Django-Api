from django.db import models

# Create your models here.
class Reporter(models.Model):
	first_name=models.CharField(max_length=29)
	last_name=models.CharField(max_length=29)
	email = models.EmailField()

	def __str__(self):
		return self.first_name +" "+ self.last_name

class Article(models.Model):
	headline = models.CharField(max_length=29)
	pub_date=models.DateField()
	reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
