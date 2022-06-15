from django.contrib.auth.forms import UserCreationForm
from .models import Monk


class SignUpForm(UserCreationForm):
    class Meta:
        model = Monk
        fields = ['user_name', 'userpic', 'title', 'first_name', 'city_of_origin', 'about', 'is_literate', 'is_ordained']