import os
USER = os.environ['USER_NAME']
HOME = os.environ['HOME']
PATH_CREDETNIAL = f'{HOME}/.config/pydata/{USER}/'
CREDENTIAL_FILE = f'pydata_google_credentials.json'

if not os.path.exists(PATH_CREDETNIAL):
    os.makedirs(PATH_CREDETNIAL)