from django.forms import ModelForm
from comments.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
