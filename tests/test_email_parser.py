# Import all required modules
from unittest import TestCase
from src.email_parser import EmailParser


class TestEmailParser(TestCase):

    def setUp(self) -> None:
        self.exec = lambda email: EmailParser.parse(email)

    def test_parse_simple_valid_email(self):

        result = {'username': 'ola', 'domain': 'gmail.com'}

        self.assertEqual(self.exec('ola@gmail.com'), result)

    def test_parser_with_invalid_email(self):
        self.assertEqual(self.exec('olat.gmail.com'), None)
        self.assertEqual(self.exec('www.olatgmail.com'), None)

    def test_parser_with_username_with_plus(self):
        result = {'username': 'ola+sodiq', 'domain': 'yahoo.com'}
        self.assertEqual(self.exec('ola+sodiq@yahoo.com'), result)

    def test_parser_with_characters(self):
        self.assertEqual(self.exec('ola=sodiq@gmail.com'), None)
        self.assertEqual(self.exec('ola_sodiq@gmail.com'), None)

    def test_parser_with_domain_endwith_number(self):
        result = {'username': 'ola+sodiq', 'domain': 'yahoo33.com'}
        self.assertEqual(self.exec('ola+sodiq@yahoo33.com'), result)

    def test_parser_with_random_data_types(self):
        self.assertEqual(self.exec(''), None)
        self.assertEqual(self.exec(123), None)
        self.assertEqual(self.exec(['olatunde@gmail.com']), None)

    def test_parser_with_email_start_with_number(self):
        self.assertEqual(self.exec('9ola@gmail.com'), None)
        self.assertEqual(self.exec('ola@6gmail.com'), None)

    def test_parser_with_email_not_end_with_dotcom(self):
        self.assertEqual(self.exec('ola@gmail.co'), None)
        self.assertEqual(self.exec('ola@gmail.co.uk'), None)

    def tearDown(self) -> None:
        self.exec = None
