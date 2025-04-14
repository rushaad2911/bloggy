# util/vectorizer.py
from apps.blog.apps import BlogConfig
from sentence_transformers import SentenceTransformer

model = None  # This will be initialized in apps.py

def initialize_model():
    print("""Initialize the model.""")
    global model
    if model is None:
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def create_embedding(title, tags_queryset):
    print("""Create an embedding for the blog title and tags.""")
    print(model)
    if model is None:
        raise ValueError("Model not loaded. Please initialize the model first.")

    tag_names = [tag.name for tag in tags_queryset]
    text = title + " " + " ".join(tag_names)
    vector = model.encode(text).tolist()  # Generate the vector
    print(vector)  # Optional: print the vector for debugging
    return vector
