from django.shortcuts import render

# Create your views here.
["book_list"]

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Article

@permission_required('bookshelf.can_view', raise_exception=True)
def view_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'bookshelf/article_detail.html', {'article': article})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        # Handle form submission for creating an article
        pass
    return render(request, 'bookshelf/article_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Handle form submission for editing the article
        pass
    return render(request, 'bookshelf/article_form.html', {'article': article})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        # Redirect to a success page
    return render(request, 'bookshelf/article_confirm_delete.html', {'article': article})
