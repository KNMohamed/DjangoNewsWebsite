# articles/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DeleteView, UpdateView, DetailView, CreateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from . import models


class ArticleListView(LoginRequiredMixin, ListView):
    model = models.Article
    template_name = 'article_list.html'
    login_url = 'login'


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleEditView(LoginRequiredMixin, UpdateView):
    model = models.Article
    fields = ['title','body',]
    template_name = 'article_edit.html'
    login_url = 'login'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = models.Article
    fields = [ 'title', 'body',]
    template_name = 'article_new.html'
    login_url = 'login' # new

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
