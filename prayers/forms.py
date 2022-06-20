from django.forms import ModelForm
from .models import Prayer, Comment


class AddPrayerForm(ModelForm):
    class Meta:
        model = Prayer
        fields = ['titulum', 'oratio']

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']