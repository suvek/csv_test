from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
	help = "A sample command"

	def handle(self, *args, **options):
		print "Hello World!"