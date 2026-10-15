import os
import mimetypes
from urllib.parse import unquote

# Base directory for static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def application(environ, start_response):
    """
    Standard WSGI application for serving Hacknova 2026 static assets on Render/Gunicorn.
    """
    raw_path = environ.get('PATH_INFO', '/').lstrip('/')
    req_path = unquote(raw_path) if raw_path else 'index.html'

    # Build target file path
    target = os.path.abspath(os.path.join(BASE_DIR, req_path))

    # Security check: ensure path stays within BASE_DIR
    if not target.startswith(BASE_DIR):
        start_response('403 Forbidden', [('Content-Type', 'text/plain')])
        return [b'403 Forbidden']

    # If directory requested, look for index.html
    if os.path.isdir(target):
        target = os.path.join(target, 'index.html')

    # If file doesn't exist, fallback to index.html (SPA fallback)
    if not os.path.isfile(target):
        target = os.path.join(BASE_DIR, 'index.html')

    if not os.path.isfile(target):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return [b'404 Not Found']

    content_type, _ = mimetypes.guess_type(target)
    if not content_type:
        content_type = 'application/octet-stream'

    file_size = os.path.getsize(target)
    headers = [
        ('Content-Type', content_type),
        ('Content-Length', str(file_size)),
        ('Accept-Ranges', 'bytes')
    ]

    start_response('200 OK', headers)
    
    # Return file in chunks
    def file_stream():
        with open(target, 'rb') as f:
            while chunk := f.read(65536):
                yield chunk

    return file_stream()

# Alias app for gunicorn wsgi:app
app = application
