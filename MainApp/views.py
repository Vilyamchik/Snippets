from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # Если пришел запрос с методом GET, вернем чистую форму для заполнения
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form,
            }
        return render(request, 'pages/add_snippet.html', context)
    # Если пришел запрос с методом POST, забираем данные из запросы, проверяем их и сохраняем в БД
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user = request.user
                snippet.save()
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
            'type': 'view',
            }
        return render(request, 'pages/snippet_detail.html', context)


def snippet_edit(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id) 
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id={snippet_id} not found')  
    else:
        # Хотим получить страницу Snippet'а для редактирования
        if request.method == 'GET':    
            context = {
                'pagename': 'Просмотр сниппета',
                'snippet': snippet,
                'type': 'edit',
                }
            return render(request, 'pages/snippet_detail.html', context)
        
        # Хотим взять данные из формы и сохранить изменения в БД
        if request.method == 'POST':
            data_form = request.POST
            snippet.name = data_form["name"]
            snippet.code = data_form["code"]
            snippet.creation_date = data_form["creation_date"]
            snippet.save()
            return redirect('snippets-list')
        

def snippet_delete(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id) 
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id={snippet_id} not found')  
    snippet.delete()
    return redirect('snippets-list')


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


# def create_snippet(request):
#     if request.method == "POST":
#         form = SnippetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("snippets-list")
#         return render(request,'add_snippet.html', {'form': form})


@login_required
def my_snippets(request):
    # Filter snippets by the currently authenticated user
    snippets = Snippet.objects.filter(user=request.user)

    # Render the template with the filtered snippets
    return render(request, 'pages/my_snippets.html', {'snippets': snippets})