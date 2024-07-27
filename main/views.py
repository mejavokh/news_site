from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DeleteView, FormView

from .models import *
from .forms import *


def main_page(request):
    news = News.objects.all().order_by('-created_at')

    context = {
        'news': news,
        'title': 'Main Page'
    }
    return render(request, 'main/main_page.html', context)


def news_by_categories(request, category_id):
    category = Category.objects.get(id=category_id)
    news = News.objects.filter(category=category)

    context = {
        'title': category.name,
        'category': category,
        'news': news
    }

    return render(request, 'main/main_page.html', context)


class NewsPostCreateView(LoginRequiredMixin, CreateView):
    model = News
    form_class = NewsPostForm
    template_name = 'main/add_post.html'
    success_url = reverse_lazy('main_page')
    context_object_name = 'news'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class DetailNewsView(DeleteView):
    model = News
    template_name = 'main/news_detail.html'
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        news_item = self.get_object()

        news_item.views += 1
        news_item.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = Comments.objects.filter(news=self.get_object())
        return context


class CreateCommentView(FormView):
    form_class = CommentForm
    template_name = 'main/news_detail.html'

    def form_valid(self, form):
        news = get_object_or_404(News, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.news = news
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('news_detail',
                            kwargs={
                                'pk': self.kwargs['pk']
                            })


