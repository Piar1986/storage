from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from datacenter.models import get_duration
from datacenter.models import format_duration
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode = passcode)
    visits_by_this_employee = Visit.objects.filter(passcard = passcard)
       
    this_passcard_visits = []
    for visit in visits_by_this_employee:
      this_passcard_visit = {
            "entered_at": visit.entered_at,
            "duration": format_duration(get_duration(visit)),
            "is_strange": is_visit_long(visit)
      }
      this_passcard_visits.append(this_passcard_visit)

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
