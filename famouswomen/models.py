from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=FamousWomen.Status.PUBLISHED)

class FamousWomen(models.Model):
    class Status(models.IntegerChoices):
        PUBLISHED = 1, 'published'
        DRAFT = 0, 'draft'

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True)
    content = models.TextField(blank=True)
    old = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]),Status.choices)), default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('show_post', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug_select': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})