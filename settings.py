INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp'#激活应用
]

DATABASES = {
     'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'bishe',
        'USER':'sa',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'',
        'OPTIONS': {
              'driver':'SQL Server Native Client 11.0',
              'MARS_Connection': True,
         }
    }
}
