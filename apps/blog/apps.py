# apps.py
from django.apps import AppConfig
from sentence_transformers import SentenceTransformer

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.blog'

    def ready(self):
        print("BlogConfig is ready")
        try:
            from .util import vectorize  # Importing util module here
            self.model = vectorize.initialize_model()  # Calling the initialization method to load the model
            print("Model loaded")
            
        except Exception as e:
            print(f"Error loading model: {e}")

    def get_model(self):
        return self.model  # This will return the model loaded in util
