from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,request
from django.shortcuts import render
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
    @method_decorator(csrf_exempt)   #quitaMiddleware
    def dispatch(self, request, *args, **kwargs):
        # if request.method == 'GET':
        #     return redirect('erp:category_list2')
        return super().dispatch(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # print(request.POST)
            data = Category.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = cat.name
        except Exception as e:
            data['error'] = str(e)

        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
