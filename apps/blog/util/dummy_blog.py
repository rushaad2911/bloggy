import random
from faker import Faker
from django.contrib.auth import get_user_model
from apps.user.models import Interest
from apps.blog.models import BlogModel

fake = Faker()
User = get_user_model()

def create_dummy_users_and_blogs(user_count=5, blogs_per_user=20):
    try:
        interests = list(Interest.objects.all())
        if not interests:
            raise Exception("No interests found. Add them before running this script.")

        for i in range(user_count):
            username = f"user{i}_{fake.user_name()}"
            email = fake.email()
            password = "testpassword123"
            
            # Create user
            user, created = User.objects.get_or_create(username=username, defaults={"email": email})
            if created:
                user.set_password(password)
                user.save()
                print(f"Created user: {username} | Password: {password}")
            else:
                print(f"User already exists: {username}")
            
            # Assign random interests
            user_interests = random.sample(interests, k=min(1, len(interests)-2))
            user.interest.set(user_interests)

            # Create blogs
            for j in range(blogs_per_user):
                title = fake.sentence(nb_words=6)
                content = "\n".join(fake.paragraphs(nb=random.randint(3, 7)))
                blog = BlogModel.objects.create(
                    title=title,
                    content=content,
                    author=user,
                )
                # Assign random tags
                blog.tags.set(random.sample(interests, k=random.randint(2, 5)))
                blog.save()
                print(f"  ➤ Blog {j+1} created for {username}: {title[:40]}")

        print("\n✅ Done creating dummy users and blogs.")

        return True
    except:
        return False
    
    
    
    
    
    
    
    
#     interests = [
#     "Technology", "AI", "Machine Learning", "Cybersecurity", "Web Development", "App Development", "Gadgets",
#     "Blockchain", "Startup", "Data Science", "Programming", "Education", "Learning Tips", "Productivity",
#     "Study Hacks", "Career Advice", "College Life", "Motivation", "Travel", "Photography", "Adventure", "Nature",
#     "Luxury", "Road Trips", "Backpacking", "Fitness", "Workout", "Yoga", "Nutrition", "Mental Health",
#     "Healthy Recipes", "Books", "Movies", "Music", "TV Shows", "Anime", "Painting", "Gaming", "Dance",
#     "Finance", "Investing", "Crypto", "Stock Market", "Side Hustle", "Freelancing"
# ]

# from apps.user.models import Interest
# for name in interests:
#     Interest.objects.get_or_create(name=name)
