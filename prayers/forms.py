from django.forms import ModelForm
from .models import Prayer, Comment


class AddPrayerForm(ModelForm):
    class Meta:
        model = Prayer
        fields = ['titulum', 'oratio']

class AddCommentFormUnauth(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']

class AddCommentFormAuth(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']