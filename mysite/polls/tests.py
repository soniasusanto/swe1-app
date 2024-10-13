from django.test import TestCase
from django.urls import reverse


class PollsPageTest(TestCase):
    def test_pollspage_status_code(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
