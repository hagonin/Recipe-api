from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["recipe-api.up.railway.app", 
                "127.0.0.1"]

cloudinary.config(
    cloud_name=config('CLOUDINARY_NAME_1'),
    api_key=config('CLOUDINARY_API_1'),
    api_secret=config('CLOUDINARY_SECRET_1')
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
