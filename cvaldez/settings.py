"""
Django settings for cvaldez project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7e#t9l=@(e6fs9ke))p_d$&p00!em&6jo)(o7c$o0+h)8axoty'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cvaldez',
    'cvaldez.datosvaldez',
)

#TEMPLATE_DIRS = ( 
   #'C:\Python27\cvaldez\cvaldez\plantillas',
#)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

)

#TEMPLATE_CONTEXT_PROCESSORS = (
    #'django.core.context_processors.media', 
    #'django.core.context_processors.static', 
     # #'django.contrib.messages.context_processors.messages',)

ROOT_URLCONF = 'cvaldez.urls'

WSGI_APPLICATION = 'cvaldez.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bdcvaldez2015',                  
        'USER': 'root',             
        'PASSWORD': 'catolica',                  
        'HOST': '',                     
        'PORT': '',                      
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
#STATICFILES_DIRS = (

 #  os.path.join(PROJECT_ROOT, "/static/"),

   # Put strings here, like "/home/html/static" or "C:/www/django/static".

   # Always use forward slashes, even on Windows.

   # Don't forget to use absolute paths, not relative paths.

#)


def rel (*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),*x)

#MEDIA_ROOT = rel('media/')
#MEDIA_ROOT ='C:/Python27/cvaldez/cvaldez/static/'
#MEDIA_URL = 'http://localhost:8000/static/'
#STATIC_ROOT = ''
#STATIC_URL = '/static/'

#STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'media')
#STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static-only')

#STATICFILES_DIRS = (
#    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'static'),
#)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'templates'),
)






LOGIN_URL = 'mysite_login'
LOGOUT_URL = 'mysite_logout'
LOGIN_REDIRECT_URL = '/'




import dj_database_url
DATABASES['default'] =  dj_database_url.config()


# anhadimos esta linea para poder acceder desde el modo seguro
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# aceptamos las peticiones desde cualquier host
ALLOWED_HOSTS = ['*']


#configuramos el acceso de los archivos estaticos
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
