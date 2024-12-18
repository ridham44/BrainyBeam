from django.views import View
from django.http import JsonResponse
from django.db import transaction
from myapp.models import MyModel
from django.http import HttpResponse


from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')  

class SaveDataView(View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = {
            'field1': request.POST.get('field1'),
            'field2': request.POST.get('field2')
        }
        obj = MyModel(**data)
        obj.save()
        return JsonResponse({'status': 'success', 'message': 'Data saved successfully!'})
