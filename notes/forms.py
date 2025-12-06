from django import forms
from .models import Note



class NoteForm(forms.ModelForm):
    """
    Form for creating and updating Note objects.
    """


    class Meta:
        model = Note
        # We only ask the user for title and content.
        fields = ['title', 'content']

