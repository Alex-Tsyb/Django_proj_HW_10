from django.forms import ModelForm, CharField, TextInput, Textarea
from .models import Tag, Author, Quote


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = CharField(min_length=3, max_length=30, required=True, widget=TextInput())
    born_location = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    description = CharField(min_length=3, required=True, widget=Textarea)   

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):

    quote = CharField(min_length=10, max_length=255, required=True, widget=Textarea)  

    class Meta:
        model = Quote
        fields = ['quote']
        exclude = ['author', 'tags']
