from django.test import TestCase
from .models import Footer


class FooterModelUnitTestCase(TestCase):
    def setUp(self):
        self.footer = Footer.objects.create(
            copyright="Armando Del Rio",
        )

    def test_footer_model(self):
        data = self.footer
        self.assertIsInstance(data, Footer)
