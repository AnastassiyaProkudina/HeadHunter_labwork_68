import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from app.models import Education


def json_education_delete(request, id, *args, **kwargs):
    cv = get_object_or_404(Education, id=id)
    cv.delete()
    return JsonResponse(status=200)


@csrf_exempt
def json_education(request, *args, **kwargs):
    if request.method == "POST" and request.body:
        education = json.loads(request.body)
        try:
            education = Education.objects.create(**education)
            response = JsonResponse(education.as_dict)
            response.status_code = 201
        except Exception:
            response_data = {"detail": "Некорректный набор данных"}
            response = JsonResponse(response_data)
            response.status_code = 400
        return response
