from django.db import models

# Create your models here.
class query(models.Model):
	
	Name = models.CharField(max_length=20)
	Email = models.EmailField()
	Phone = models.CharField(max_length=10)

	Serivce = models.CharField(max_length=100)
	Location = models.CharField(max_length=20)
	Budget = models.CharField(max_length=10)
	Date = models.DateField()

	def __unicode__(self):
		return self.Name


	