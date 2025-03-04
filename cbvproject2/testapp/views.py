from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from testapp.models import Book
class BookListView(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'
class BookListView2(ListView):
    model = Book
    template_name = 'testapp/books.html'
    context_object_name = 'books'
class BookDetailView(DetailView):
    model = Book
class BookCreateView(CreateView):
    model = Book
    fields = ('title','author','pages','price')
class BookUpdateView(UpdateView):
    model = Book
    fields = ('pages','price')
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('list')


