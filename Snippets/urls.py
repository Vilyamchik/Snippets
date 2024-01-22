from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('snippets/add', views.add_snippet_page, name='add_snippet'),
    path('snippets/list', views.snippets_page, name='snippets_list'),
    path('snippet/<int:snippet_id>/', views.snippet, name='snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

