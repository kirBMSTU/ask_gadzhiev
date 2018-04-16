from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
	avatar = models.ImageField(upload_to='%Y/%m/%d', default='default_avatar.jpg')

	def __str__(self):
		return self.user.username

class Tag(models.Model):
	label = models.CharField(max_length=25)

	def __str__(self):
		return self.label.lower()

	class Meta:
		ordering = ('label',)

class QuestionManager(models.Manager):
	def get_hot(self):
		return self.order_by('-rating')
	def get_last(self):
		return self.order_by('-date')
	def get_by_tag(self, tag):
		return self.filter(tags__label__iexact=tag).order_by('-date')

class Question(models.Model):
	question_title = models.CharField(max_length=100)
	question_text = models.TextField()
	tags = models.ManyToManyField(Tag)
	rating = models.IntegerField(default=0)
	question_author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
	date = models.DateTimeField(auto_now_add=True)
	objects = QuestionManager()

	class Meta:
		ordering = ('id',)

	def __str__(self):
		return self.question_title

class AnswerManager(models.Manager):
	def get_answers(self, question_id):
		return self.filter(question__id__exact=question_id).order_by('-rating', '-date')
	


class Answer(models.Model):
	answer_text = models.TextField()
	answer_author = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
	date = models.DateTimeField(auto_now_add=True)
	rating = models.IntegerField(default=0)
	correct = models.BooleanField(default=False)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	objects = AnswerManager()

class Like(models.Model):
    like_type = models.IntegerField(default=0) # 1 - если ЛАЙК, -1 - если ДИЗЛАЙК
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    class Meta:
    	abstract = True

class AnswerLike(Like):
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

class QuestionLike(Like):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)





















