from django.test import TestCase
from login.models import Activity


class ActivityTests(TestCase):
    """Activity model tests"""

    def test_str(self):
        typ = Activity("Pisanie maila", "2015-10-04 21:23:00", "2015-10-04 22:22:22")
        
