from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView
from ..models import BookModel
from ..forms import AvaliationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

class DetailBookView(DetailView):
    model = BookModel
    context_object_name = 'book'
    template_name = 'book/detail_book.html'


    def get_queryset(self) -> QuerySet[Any]:
        # sourcery skip: inline-immediately-returned-variable
        qs =  BookModel.objects.prefetch_related('avaliations').filter(
            pk=self.kwargs.get('pk')
        )
        return qs
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        # sourcery skip: inline-immediately-returned-variable
        print('comentarios: ', self.get_queryset().first().avaliations.first())
        context =  super().get_context_data(**kwargs)
        context['comment_form'] = AvaliationForm()
        return context