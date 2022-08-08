from rest_framework import throttling

import datetime

class WorkingHoursRateThrottle(throttling.BaseThrottle):

    def allow_request(self, request, view):
        now = datetime.datetime.now().hour
        if now >= 4 and now <= 5:
            return False
        return True
