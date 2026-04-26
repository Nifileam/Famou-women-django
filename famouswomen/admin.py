from itertools import count

from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import FamousWomen, Category

@admin.register(FamousWomen)
class FamousWomenAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'post_photo', 'is_published', 'updated', 'cat', ]
    list_display_links = ['name']
    list_editable = ['is_published']
    list_per_page = 10
    ordering = ['name']
    actions = ['set_published', 'set_draft']
    search_fields = ['name', 'cat__name']
    list_filter = ['cat', 'is_published']

    fields = ['name', 'slug', 'old', 'post_photo', 'photo', 'cat', 'content', 'tags', 'is_published', 'created', 'updated']
    readonly_fields = ['post_photo', 'created', 'updated']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True


    @admin.display(description='Images')
    def post_photo(self, women: FamousWomen):
        if women.photo:
            return mark_safe(f"<img src='{ women.photo.url }' width=50>")
        return 'Without Photo'

    @admin.action(description='Published')
    def set_published(self, request, queryset):
        num = queryset.update(is_published=FamousWomen.Status.PUBLISHED)
        self.message_user(request, f'Published { num } posts')

    @admin.action(description='Draft')
    def set_draft(self, request, queryset):
        num = queryset.update(is_published=FamousWomen.Status.DRAFT)
        self.message_user(request, f'Draft { num } posts', messages.WARNING)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
