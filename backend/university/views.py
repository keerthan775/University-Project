from django.shortcuts import render
from university.models import *
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def get(request):
    value = json.loads(request.body)['value']

    print("------", value, "-------")
    student = list(Student.objects.filter(usn=value).values())
    iot = list(Iot.objects.filter(usn_id=value).values())
    bda = list(Bda.objects.filter(usn_id=value).values())
    sms = list(Sms.objects.filter(usn_id=value).values())
    internship = list(Internship.objects.filter(usn_id=value).values())
    project_phase2 = list(ProjectPhase2.objects.filter(
        usn_id=value).values())
    seminar = list(Seminar.objects.filter(usn_id=value).values())
    return JsonResponse({"student":   student, "iot": iot, "bda": bda, "sms": sms, "internship": internship, "project phase2": project_phase2, "seminar": seminar})
