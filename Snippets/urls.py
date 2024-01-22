from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name="snippets-add"),
    path('snippets/list', views.snippets_page, name='snippets-list'),
    path('snippet/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippet/create', views.create_snippet, name='create-snippet'),
    path('delete_snippet/<int:snippet_id>/', views.deleteSnippet, name='delete-snippet'),
    path('edit/<int:snippet_id>/', views.editSnippet, name='editSnippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)