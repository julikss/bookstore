from django.http import HttpResponse
from django.template import loader
from .models import Book

def catalog(request):
    books = Book.objects.all().values()
    template = loader.get_template('catalog.html')
    context = {
        'books': books
    }
    return HttpResponse(template.render(context, request))

