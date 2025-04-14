from apps.blog.models import BlogModel

def tag_recommend(user, top_k=10):
    # Get the list of user's interests (tags they are interested in)
    interests = user.interest.all()

    print("User Interests:", [interest.name for interest in interests])

    # Get blogs where at least one of the tags matches any of the user's interests
    matching_blogs = BlogModel.objects.filter(
        tags__name__in=[i.name for i in interests],
        
    ).exclude(author=user).distinct()

    # Return the top_k matching blogs
    return matching_blogs[:top_k]
