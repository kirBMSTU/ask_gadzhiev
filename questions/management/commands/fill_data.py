from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Tag, Answer, Profile, User

class Command(BaseCommand):
	help = 'Fills the database with testing data.'

	def execute(*args, **options):
		for i in range(5):
			user = User.objects.create(username='user{0}'.format(i), password='abc12345')
			profile = Profile.objects.create(user=user)


		for i in range(7):
			tag = Tag.objects.create(label='tag{0}'.format(i))

		for i in range(50):
			print('id={0}'.format(i%5))
			author = Profile.objects.get(user__username__exact='user{0}'.format(i%5))
			new_question = Question.objects.create(
							question_title='Interesting question title {0}'.format(i), 
							question_text='Interesting question text {0}'.format(i) * 10, 
							rating=(i-25),
							question_author=author
							)
			tag1 = Tag.objects.get(label__exact='tag{0}'.format(i%7))
			tag2 = Tag.objects.get(label__exact='tag{0}'.format((i+3)%7))
			tag3 = Tag.objects.get(label__exact='tag{0}'.format((i+5)%7))
			new_question.tags.add(tag1, tag2, tag3)


		for i in range(20):
			author = Profile.objects.get(user__username__exact='user{0}'.format((25-i)%5))
			question = Question.objects.get(question_title__exact='Interesting question title {0}'.format(49-i))
			answer = Answer.objects.create(answer_text='Good answer {0}'.format(i), 
								  answer_author=author,
								  rating=i%10-5,
								  correct=bool(i%5%2),
								  question=question
								  )








