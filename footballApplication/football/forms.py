from django import forms

from footballApplication.football.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Please enter your name'}),
            'content': forms.Textarea(attrs={'placeholder': 'Please enter your comment'}),
        }

        error_messages = {
            'author': {
                'max_length': 'You have entered too many characters.',
            }
        }

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.author = comment.author.capitalize()

        if commit:
            comment.save()

        return comment



