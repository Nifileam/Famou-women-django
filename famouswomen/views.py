from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import title
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView

from .forms import AddPostForm, ContactForm
from .models import FamousWomen, Category, TagPost
from .utils import DataMixin


class FamousWomenHome(DataMixin, ListView):
    template_name = 'famouswomen/index.html'
    context_object_name = 'posts'
    title_page = 'Famous Women'
    cat_select = 0

    def get_queryset(self):
        return FamousWomen.published.all().select_related('cat')

def about(request):
    return HttpResponse('About')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'famouswomen/add_page.html'
    success_url = reverse_lazy('home')
    title_page = 'Add Page'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(LoginRequiredMixin, DataMixin, UpdateView):
    model = FamousWomen
    fields = ['name', 'slug', 'photo', 'content', 'old', 'cat', 'tags']
    template_name = 'famouswomen/add_page.html'
    success_url = reverse_lazy('home')
    title_page = 'Edit Page'

    def get_queryset(self):
        return FamousWomen.objects.filter(author=self.request.user)

class ContactFormView(LoginRequiredMixin, DataMixin, FormView):
    form_class = ContactForm
    template_name = 'famouswomen/contact.html'
    success_url = reverse_lazy('home')
    title_page = 'Feedback'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class FamousWomenShowPost(DataMixin, DetailView):
    template_name = 'famouswomen/show_post.html'
    context_object_name = 'info'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(context, title=context['info'].name)

    def get_object(self, queryset=None):
        return get_object_or_404(FamousWomen.published, slug=self.kwargs[self.slug_url_kwarg])


class FamousWomenCategory(DataMixin, ListView):
    template_name = 'famouswomen/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return FamousWomen.published.filter(cat__slug=self.kwargs['slug_select']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['posts'][0].cat
        return self.get_mixin_context(context, title=f'Category: { cat.name }', cat_select=cat.pk)


class FamousWomenTagPostList(DataMixin, ListView):
    template_name = 'famouswomen/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return FamousWomen.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = get_object_or_404(TagPost, slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context, title=f'Tag: { tag.tag }')

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
