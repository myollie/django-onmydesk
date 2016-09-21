"""Command used to process schedulers."""

from datetime import date
import tempfile
from os import path

from django.core.management.base import BaseCommand

import filelock
from onmydesk.models import Scheduler
from onmydesk.utils import log_prefix


class Command(BaseCommand):
    """Process schedulers."""

    help = 'Process schedulers'

    def handle(self, *args, **options):
        """Entrypoint of our command."""
        try:
            self._process_with_lock()
        except filelock.Timeout:
            self.stdout.write('Could not obtain lock to process scheduler')
        except Exception as e:
            self.stdout.write('Error: {}'.format(e))

    def _process_with_lock(self):
        lock = filelock.FileLock(self._get_lock_filepath())

        with lock.acquire(timeout=10):
            self._process_schedulers()

    def _get_lock_filepath(self):
        return path.join(tempfile.gettempdir(), 'onmydesk-scheduler-processor-lock')

    def _process_schedulers(self):
        self.stdout.write(log_prefix() + 'Starting scheduler process')

        today = date.today()

        self.stdout.write('Using date {} as reference to get schedulers'.format(today))

        items = Scheduler.objects.pending(today)

        count = len(items)

        self.stdout.write(log_prefix() + 'Found {} schedulers to process'.format(count))

        for i, scheduler in enumerate(items, start=1):
            self.stdout.write('Processing scheduler #{} - {} of {}'.format(
                scheduler.id, i, count))

            try:
                scheduler.process(reference_date=today)
                self.stdout.write(log_prefix() + 'Scheduler #{} processed'.format(scheduler.id))
            except Exception as e:
                self.stderr.write(log_prefix() + 'Error processing scheduler #{}: {}'.format(
                    scheduler.id, str(e)))
