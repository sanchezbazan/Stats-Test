import pytest
from django.test import override_settings


@pytest.fixture(autouse=True)
def test_settings(settings):
    with override_settings(SECRET_KEY='7k7d2z#sf8xp*n0rx&ftld!-0s(p194=t7878-_5%*&&-xp43k',):
        yield
