
from django.urls import path, re_path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    #path('products/<int:id>', views.index, name='index')
    re_path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #path('<int:question_id>', views.detail, name='detail'),
    re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    re_path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # re_path(r'^$', views.IndexView.as_view(), name='index'),
    # re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # re_path(r'^(?P<pk>[0-9]+)/results/$',views.ResultsView.as_view(), name='detail')

]