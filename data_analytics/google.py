import os

import pydata_google_auth
from pydata_google_auth.cache import ReadWriteCredentialsCache

from data_analytics import config


def get_credentials(scope=None):
    if not scope:
        scope = [
            'https://www.googleapis.com/auth/cloud-platform',
            'https://www.googleapis.com/auth/bigquery',
        ]
    credentials_cached = \
        ReadWriteCredentialsCache(dirname=config.PATH_CREDETNIAL,
                                  filename=config.CREDENTIAL_FILE)

    credential = pydata_google_auth.get_user_credentials(
        scopes=scope,
        credentials_cache=credentials_cached,
        use_local_webserver=False,
    )
    return credential