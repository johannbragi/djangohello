from django.test import TestCase

class PollsViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/admin/')
        self.assertEqual(resp.status_code, 200)