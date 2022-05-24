from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):

    passcard = Passcard.objects.get(passcode=passcode)
    serialized = Visit.objects.filter(passcard=passcard)

    this_passcard_serialized = []

    for visit in serialized:
        seconds = visit.get_duration().total_seconds()
        formated_duration = f"{seconds // 3600} h {(seconds % 3600) // 60} min"
        this_passcard_serialized.append(
            {
                'entered_at': visit.entered_at,
                'duration': formated_duration,
                'is_strange': visit.is_visit_long()
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_serialized
    }
    return render(request, 'passcard_info.html', context)
