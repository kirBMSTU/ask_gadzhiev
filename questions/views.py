from django.shortcuts import render

from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from questions.models import Tag, Question, Answer, Profile

# Create your views here.
user1 = {
	'name': 'Kirill Gadzhiev'
}

user2 = {
	'name': 'Ksenia Kazantseva'
}

user3 = {
	'name': 'Vitya Cherkov'
}

user4 = {
	'name': 'fist09'
}

best_members1 = [user1, user2, user3, user4]

tags_list = Tag.objects.all()[:20]

best_members = Profile.objects.all()[:10]

answers = [
	{
		'id': 0,
		'user': user4,
		'text': """Для этого необходимо закончить школу с золотой медалью, 
					поступить в бауманку, закончить бакалавриат и магистратуру,
					отработать в макдоналдсе 3 года, потом в нашей компании уборщиком 2 года, 
					и после этого можете приходить к нам на собеседование на вакансию специалиста по ГАС "КОНТУР". """,
		'rating': 5,
		'correct': True
	},
	{
		'id': 1,
		'user': user3,
		'text': """Для разработки фотообъективов — для них «ширпотреб»,
					они занимаются более сложными системами. Конечно,
					такие заявления меня смутили, но на безрыбье и рак рыба. """,
		'rating': 10,
		'correct': False
	},
	{
		'id': 2,
		'user': user2,
		'text': """Да это каждый дурак знает!! """,
		'rating': -50,
		'correct': False
	}
]

authentificated = False


def index(request):
	page_type = 'index'
	return render(request, 'index.html', 
		{
		'authentificated': authentificated,
		'user': user1,
		'title': 'New Questions',
		'tags_list': tags_list,
		'page_type': page_type,
		'posts': paginate(Question.objects.get_last(), request, on_page=20),
		'best_members': best_members
		})

def hot(request):
	page_type = 'hot'
	return render(request, 'index.html', 
		{
		'authentificated': authentificated,
		'user': user1,
		'title': 'Hot Questions',
		'tags_list': tags_list,
		'page_type': page_type,
		'posts': paginate(Question.objects.get_hot(), request, on_page=20),
		'best_members': best_members
		})

def tags(request, tag):
	page_type = 'tag'
	return render(request, 'index.html', 
		{
		'authentificated': authentificated,
		'user': user1,
		'tags_list': tags_list,
		'page_type': page_type,
		'tag': tag,
		'title': '#' + tag,
		'posts': paginate(Question.objects.get_by_tag(tag), request, on_page=20),
		'best_members': best_members
		})

def ask(request):
	return render(request, 'ask.html',
		{
		'authentificated': authentificated,
		'user': user1,
		'title': 'New Questions',
		'tags_list': tags_list,
		'posts': posts,
		'best_members': best_members
		})

def login(request):
	return render(request, 'login.html',
		{
		'authentificated': False,
		'title': 'Login',
		'tags_list': tags_list,
		'posts': posts,
		'best_members': best_members
		})

def signup(request):
	return render(request, 'signup.html',
		{
		'authentificated': False,
		'title': 'Sign up',
		'tags_list': tags_list,
		'posts': posts,
		'best_members': best_members
		})

def question(request, question_id):
	return render(request, 'question.html',
		{
		'authentificated': authentificated,
		'user': user1,
		'tags_list': tags_list,
		'question': Question.objects.get(question_id),
		'title': Question.objects.get(question_id).question_title,
		'answers': Answer.objects.get_answers(question_id),
		'best_members': best_members
		})

def user_settings(request):
	return render(request, 'settings.html',
	{
	'authentificated': authentificated,
	'user': user1,
	'tags_list': tags_list,
	'title': 'Settings',
	'best_members': best_members
	})

def logout(request):
	pass

# def user_form(request):
# 	if request.method=="POST":
# 		form = UserForm(request.POST)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.published_date = timezone.now()
# 			post.save()
# 			return redirect('post_detail', pk=post.pk)
# 	else:
# 		form = UserForm()

# 	r_d = {
# 		'form': UserForm
# 	}

def paginate(objects_list, request, on_page):
	paginator = Paginator(objects_list, on_page)
	page = request.GET.get('page')
	return paginator.get_page(page)









