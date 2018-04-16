from django.urls import path, include
from questions.views import index, ask, user_settings, logout, signup, login, tags, hot, question

urlpatterns = [
	path(r'', index, name='index'),
	path(r'ask', ask, name='ask'), 
	path(r'settings', user_settings, name='settings'),
	path(r'logout', logout, name='logout'), 
	path(r'signup', signup, name='signup'), 
	path(r'login', login, name='login'), 
	path(r'tag/<str:tag>', tags, name='tag'),
	path(r'hot', hot, name='hot'),
	path(r'question/<int:question_id>', question, name='question')
]