from django.core.management.base import BaseCommand, CommandError
from rest_api.models import ShoeColor, ShoeType


class Command(BaseCommand):
    help = 'Populates ShoeColor and ShoeType tables'

    def add_arguments(self, parser):

        parser.add_argument('name', nargs='+', type=str)
        parser.add_argument('--table', action='store', type=str)

    def handle(self, *args, **options):

        if options['table'] == 'ShoeColor':
            for name in options['name']:
                try:
                    table = ShoeColor.objects.create(color_name=name)
                except ShoeColor.DoesNotExist:
                    raise CommandError('Poll "%s" does not exist' % poll_id)

                self.stdout.write(self.style.SUCCESS(
                    'Successfully created "%s"' % name))
        elif options['table'] == 'ShoeType':
            for name in options['name']:
                try:
                    table = ShoeType.objects.create(style=name)
                except ShoeType.DoesNotExist:
                    raise CommandError('Poll "%s" does not exist' % poll_id)

                self.stdout.write(self.style.SUCCESS(
                    'Successfully created "%s"' % name))
# you see i grew up in savanah killing wilderbeast and lion alike. codeing is nothing compared to stalking a lion
