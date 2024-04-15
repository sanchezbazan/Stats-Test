import os

# Set on the earliest possible moment
os.environ['PYTEST_RUNNING'] = 'true'

from stats_core.accounts.tests.fixtures import *  # noqa: F401, F403, E402
from stats_core.core.tests.fixtures import *  # noqa: F401, F403, E402
