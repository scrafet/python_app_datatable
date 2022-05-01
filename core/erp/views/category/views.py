from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from core.erp.models import Category


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all()
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # @method_decorator(login_required) 'solicita login
    @method_decorator(csrf_exempt)  #quita middleware
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('erp:category_list2')
        return super().dispatch(request, *args, **kwargs)

    def __pos__(self):
        data = {'name': 'William'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
