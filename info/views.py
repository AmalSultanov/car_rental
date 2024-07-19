from math import ceil

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from info.forms import CommentModelForm
from info.models import (TeamModel, InfoModel, AboutImageModel, HistoryModel,
                         PostModel, BlogImageModel, CategoryModel)


class AboutListView(ListView):
    template_name = 'about.html'
    paginate_by = 6
    queryset = TeamModel.objects.order_by('-pk')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = AboutImageModel.objects.all()
        context['info'] = InfoModel.objects.all()
        context['history'] = HistoryModel.objects.all()
        x = ceil(TeamModel.objects.count() / self.paginate_by)
        context['page_count'] = range(x)

        return context


class BlogListView(ListView):
    template_name = 'blog.html'
    paginate_by = 6
    queryset = PostModel.objects.order_by('-pk')

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        category = self.request.GET.get('category')

        if tag:
            qs = qs.filter(tags__title=tag)

        if category:
            qs = qs.filter(category__title=category)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = BlogImageModel.objects.all()
        x = ceil(TeamModel.objects.count() / self.paginate_by)
        context['page_count'] = range(x)

        return context


class BlogDetailDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = PostModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bg_image'] = BlogImageModel.objects.all()
        context['categories'] = CategoryModel.objects.all()

        return context


class CommentCreateView(LoginRequiredMixin, CreateView):
    form_class = CommentModelForm

    def get_success_url(self):
        return reverse('info:blog-detail',
                       kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.post = get_object_or_404(PostModel, pk=pk)
        return super().form_valid(form)
