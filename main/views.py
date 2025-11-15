from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_POST, require_GET
from .models import Incident


def home(request):
    return HttpResponse("Привет, Django!")


@require_POST
@csrf_exempt
def create_incident(request):

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    msg = data.get("msg")
    status = data.get("status")
    source = data.get("source")

    if not status or not source:
        return JsonResponse(
            {"error": "Fields 'status' and 'source' are required"},
            status=400,
        )

    incident = Incident.objects.create(
        msg=msg,
        status=status,
        source=source,
    )

    return JsonResponse(
        {
            "message": "incident created",
            "id": incident.id,
            "status": incident.status,
            "source": incident.source,
        },
        status=201,
    )


@require_GET
def get_incidents(request):

    status_text = request.GET.get("status")

    if not status_text:
        return JsonResponse(
            {"error": "Query param 'status' is required"},
            status=400,
        )

    incidents = Incident.objects.filter(status=status_text)

    data = [
        {
            "id": inc.id,
            "msg": inc.msg,
            "status": inc.status,
            "source": inc.source,
            "time": inc.time.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for inc in incidents
    ]

    return JsonResponse({"incidents": data}, status=200)


@require_http_methods(["POST", "PUT"])
@csrf_exempt
def update_incident_status(request):

    try:
        data = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    incident_id = data.get("id")
    new_status = data.get("new_status")

    if not incident_id:
        return JsonResponse({"error": "Field 'id' is required"}, status=400)

    if not new_status:
        return JsonResponse({"error": "Field 'new_status' is required"}, status=400)

    try:
        incident = Incident.objects.get(id=incident_id)
    except Incident.DoesNotExist:
        return JsonResponse(
            {"error": f"Incident with id={incident_id} not found"},
            status=404
        )

    incident.status = new_status
    incident.save()

    return JsonResponse(
        {
            "message": "status updated",
            "incident_id": incident.id,
            "new_status": incident.status,
        },
        status=200
    )