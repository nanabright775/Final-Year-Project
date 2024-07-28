from django.contrib.auth.models import User

#creating a user using the default user model
def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user