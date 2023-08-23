from django.db import models

# Create your models here.
class Faculty(models.Model):
	name= models.CharField(max_length=100,blank=True)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	subject=models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Student(models.Model):
	name=models.CharField(max_length=100,blank=True)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	subject=models.CharField(max_length=100,blank=True)
	faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)

	def __str__(self):
		return self.subject+ " - " +self.name