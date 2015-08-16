import datetime

from django.db import models

# Create your models here.


class Creator(models.Model):
	name = models.CharField(max_length=50)
	surname = models.CharField(max_length=50)
	photo = models.ImageField(upload_to='articles_img', blank=True)
	site = models.EmailField(max_length=254, blank=True)
	info = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.surname

	class Meta:
		abstract = True


class Author(Creator):
	authorinfo = models.CharField(max_length=500, blank=True)

class Painter(Creator):
	painterinfo = models.CharField(max_length=500, blank=True)


YEARS = [(i, i) for i in range(2011, 2050)]
MONTHS = [(i, i) for i in range(1, 13)]

class Magazine(models.Model):
	year = models.IntegerField(choices=YEARS)
	month = models.IntegerField(choices=MONTHS)
	cover = models.ImageField(upload_to='covers', blank=True)

	def __str__(self):
		return str(self.month) + '/' + str(self.year)  


class Category(models.Model):
	name = models.CharField(max_length=100)
	info = models.CharField(max_length=1000)

	def __str__(self):
		return self.name  



class Article(models.Model):
	title = models.CharField(max_length=255)
	authors = models.ManyToManyField(Author)
	def get_authors(self):
		return '\n'.join([p.surname for p in self.authors.all()])
	painters = models.ManyToManyField(Painter, blank=True)
	magazine = models.ForeignKey(Magazine)
	category = models.ForeignKey(Category)
	pdf = models.FileField(upload_to='articles_pdf', blank=True)
	slug = models.CharField(max_length=200)
	teaser = models.CharField(max_length=1000, blank=True)
	preview = models.ImageField(upload_to='articles_preview', blank=True)
	access = models.BooleanField()
	similar = models.ManyToManyField('self', blank=True)
	additional = models.CharField(max_length=2000, blank=True)

	def __str__(self):
		return self.title  


class ArticleImage(models.Model):
	image = models.ImageField(upload_to='articles_img')
	article = models.ForeignKey(Article)



# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
# 
# 
# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
