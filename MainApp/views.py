from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
            }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request,'add_snippet.html', {'form': form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = { 
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets,
        }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id) 
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id={snippet_id} not found')  
    else:    
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet,
            }
        return render(request, 'pages/snippet_detail.html', context)


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request,'add_snippet.html', {'form': form})
    

def deleteSnippet(request, snippet_id):
    if request.method == "POST":
        snippet = Snippet.objects.get(pk=snippet_id)
        snippet.delete()
        return redirect("snippets-list")
    

def editSnippet(request, snippet_id):
    pass