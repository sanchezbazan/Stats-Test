import pytest
from model_bakery import baker

from stats_core.core.utils.cryptography import KeyPair


@pytest.fixture
def sender_key_pair():
    return KeyPair(
        public='943326bfb95160f9ac73cadd7fa6361fd542963dd86adb60c410fcc22e3c96c1',
        private='acb34653559abebeabf67e01c89ab5f0859674c8a643b294b9ffc89012ac2e2e'
    )


@pytest.fixture
def sender_account_number(sender_key_pair):
    return sender_key_pair.public


@pytest.fixture
def sender_account(sender_account_number, db):
    return baker.make('accounts.Account', account_number=sender_account_number, balance=20000)
