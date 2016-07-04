"""Managers."""

from django.db import models


class SchedulerManager(models.Manager):
    """Scheduler manager adding methods to improve it."""

    def pending(self, date):
        """Return schedulers pending to process."""
        from .models import Scheduler
        periodicities = Scheduler.PERIODICITIES_BY_WEEKDAY.get(date.weekday())
        return self.all().filter(periodicity__in=periodicities)
