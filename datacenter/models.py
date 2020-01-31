from django.db import models
from datetime import timedelta
from django.utils import timezone

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete = models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
        
def is_visit_long(visit, minutes=60):
  if visit.leaved_at == None:
    is_visit_long_flag = bool(timedelta(minutes = minutes) < timedelta(seconds = int((timezone.now().timestamp() - visit.entered_at.timestamp()))))
  else:
    is_visit_long_flag = bool(timedelta(minutes = minutes) < timedelta(seconds = (visit.leaved_at.timestamp() - visit.entered_at.timestamp())))
  return is_visit_long_flag
    
def get_duration(visit):
  if visit.leaved_at == None:
    duration = timezone.now().timestamp() - visit.entered_at.timestamp()
  else:
    duration = visit.leaved_at.timestamp() - visit.entered_at.timestamp()
  return duration
    
def format_duration(duration):
  return str(timedelta(seconds = int(duration)))