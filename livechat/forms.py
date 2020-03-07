from django.forms import ModelForm
from .models import Chat, Note


class ChatForm(ModelForm):

    class Meta:
        model = Chat
        fields = ('message', )

class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ('note', )