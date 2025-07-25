from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-$i@l54*dd53qe&hxz35yn#39**np)%i6nkb%52a75x#bl2av8$'

DEBUG = False  # Turn off in production
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'yourdomain.com']  # Replace with actual domain
# Enforce HTTPS redirect: all HTTP requests are redirected to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS) settings:
# Tell browsers to only use HTTPS for the next 1 year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000  # 1 year

# Apply HSTS to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow your domain to be included in browser preload lists for HSTS
SECURE_HSTS_PRELOAD = True

# Ensure session cookies are only sent over HTTPS connections
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS connections
CSRF_COOKIE_SECURE = True

# Protect against clickjacking attacks by denying framing
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing responses away from the declared content type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser’s XSS filter to prevent some cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'users',
    'csp',  # Content Security Policy
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # CSP middleware near the top
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

# Login/logout redirects
LOGIN_REDIRECT_URL = '/relationship_app/books/'
LOGOUT_REDIRECT_URL = '/relationship_app/login/'

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'script-src': ("'self'", 'https://cdnjs.cloudflare.com'),
        'style-src': ("'self'", 'https://fonts.googleapis.com'),
    }
}