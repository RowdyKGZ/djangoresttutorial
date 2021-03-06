from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>,', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]



urlpatterns = format_suffix_patterns(urlpatterns)
