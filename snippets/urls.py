from rest_framework import renderers
from rest_framework.decorators import renderer_classes
from snippets.views import SnippetViewSet
from django.urls import path
from snippets import views

from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})



urlpatterns = [
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)




