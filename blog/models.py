from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	publish_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.title	