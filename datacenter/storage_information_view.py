from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render

def storage_information_view(request):
    in_storage = Visit.objects.filter(leaved_at = None)
    
    non_closed_visits = []
    for visit in in_storage:
      non_closed_visit = {
        "who_entered": visit.passcard,
        "entered_at": visit.entered_at,
        "duration": format_duration(get_duration(visit))
      }
      non_closed_visits.append(non_closed_visit)
   
    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
