menu = [
    {'title': 'Home','url_name':'home'},
    {'title': 'About','url_name':'about'},
    {'title': 'Add page','url_name':'add_page'},
]


class DataMixin:
    paginate_by = 10
    extra_context = {}
    cat_select = None
    title_page = None

    def __init__(self):
        if self.title_page is not None:
            self.extra_context['title'] = self.title_page

        if self.cat_select is not None:
            self.extra_context['cat_select'] = self.cat_select

    def get_mixin_context(self, context, **kwargs):
        context['cat_select'] = None
        context.update(kwargs)
        return context
