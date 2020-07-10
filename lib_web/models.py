from django.db import models

# Create your models here.


class Author(models.Model):
	name = models.TextField()
	surname = models.TextField()
	
	def __str__(self):
		return f"{self.name} {self.surname}"
	

class Book(models.Model):
	name = models.TextField()
	year = models.IntegerField()
	author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
	isbn = models.CharField(max_length=17)
	
	def __str__(self):
		return f"{self.name}, {self.year}"
