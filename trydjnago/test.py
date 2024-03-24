import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
    def test_secrect_key_strength(self):
        secrect_key = os.environ.get('DJANGO_SECRECT_KEY') # returns abc123
        # self.assertNotEqual(secrect_key, 'abc124')
        try:
            is_strong = validate_password(secrect_key)
        except Exception as e:
            msg = f'Bad Secrect Key {e.messages}'
            self.fail(msg)