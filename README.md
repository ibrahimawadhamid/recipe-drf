# recipe-drf
A Django REST Framework project for learning purposes

## Development
- create a file next to the `settings.py` file names `local_settings.py` with the following content:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
    }
}
```
This should override the default database settings `"PostgeSQL in production"` with the default `"sql lite"` database