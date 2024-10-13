from django.core.management.base import BaseCommand
from polls.models import Question
from django.utils import timezone

test_var=None

class Command(BaseCommand):
    help = 'Creates a poll.'

    def handle(self, *args, **options):
        if not Question.objects.filter(question_text__startswith="What").exists():
            q = Question(question_text="What's new?", pub_date=timezone.now())
            q.save()
            q.choice_set.create(choice_text="Not much", votes=0)
            q.choice_set.create(choice_text="The sky", votes=0)
        print("Poll was created.")
