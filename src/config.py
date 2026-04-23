# Configuration settings for My AI App

# Video Quality Settings
VIDEO_QUALITY = {
    'resolution': '1080p',
    'frame_rate': '30fps'
}

# API Configuration
API_SETTINGS = {
    'base_url': 'https://api.example.com',
    'timeout': 30
}

# Redis Configuration
REDIS_SETTINGS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0
}

# Celery Settings
CELERY_SETTINGS = {
    'broker_url': 'redis://localhost:6379/0',
    'result_backend': 'redis://localhost:6379/0'
}

# File Storage Settings
FILE_STORAGE = {
    'max_file_size': '10MB',
    'allowed_file_types': ['jpg', 'png', 'mp4']
}

# Model Settings
MODEL_SETTINGS = {
    'model_name': 'GPT-4',
    'max_tokens': 2048
}

# Branding Options
BRANDING_OPTIONS = {
    'app_name': 'My AI App',
    'version': '1.0.0',
    'logo_url': 'https://example.com/logo.png'
}