from calendarApp.tasks import send_event_reminders

class Command(BaseCommand):
    help = 'Send reminders for upcoming events'

    def handle(self, *args, **options):
        send_event_reminders()
        self.stdout.write(self.style.SUCCESS('Successfully sent reminders'))