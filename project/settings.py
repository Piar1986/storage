import os
from dotenv import load_dotenv
from environs import Env

env = Env()
env.read_env()
DEBUG = env.bool("DEBUG")

load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE"),
        'HOST': os.getenv("HOST"),
        'PORT': os.getenv("PORT"),
        'NAME': os.getenv("NAME"),
        'USER': os.getenv("USER"),
        'PASSWORD': os.getenv("PASSWORD"),
    }
}

#DEBUG = os.getenv("DEBUG")

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv("SECRET_KEY")

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True