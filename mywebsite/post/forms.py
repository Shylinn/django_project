from django import forms
from .models import Post

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if not self.instance.__dict__[field]:
                self.fields[field].widget.attrs['readonly'] = True
