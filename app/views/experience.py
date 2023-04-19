import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app.models import Experience


@csrf_exempt
def json_experience(request, *args, **kwargs):
    if request.method == "POST" and request.body:
        experience = json.loads(request.body)
        try:
            experience = Experience.objects.create(**experience)
            response = JsonResponse(experience.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {"detail": "Некорректный набор данных"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
