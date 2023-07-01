from django.contrib.auth.models import User
from .models import ActivityLog

def log_activity(user, activity):
    activity_log = ActivityLog(user=user, activity=activity)
    activity_log.save()
