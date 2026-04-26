from django.urls import path
from . import views


urlpatterns = [
    path('', views.FamousWomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('post/<slug:slug>/', views.FamousWomenShowPost.as_view(), name='show_post'),
    path('category/<slug:slug_select>/', views.FamousWomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.FamousWomenTagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit'),
]