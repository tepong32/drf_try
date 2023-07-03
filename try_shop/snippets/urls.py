from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.snippet_list),
    path('<int:pk>/', views.snippet_detail),
]

# see https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#adding-optional-format-suffixes-to-our-urls
urlpatterns = format_suffix_patterns(urlpatterns)