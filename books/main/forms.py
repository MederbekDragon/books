from .models import Books
from django.forms import ModelForm,TextInput,Textarea

class BooksForm(ModelForm):
    class Meta:
        model= Books
        fields=['title','subtitle','description','price','genre','author','year']

widgets={
    "title":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Book name'
    }),
        "subtitle":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Short description'
    }),
        "description":Textarea(attrs={
        'class': 'form-control',
        'placeholder':'ABOUT BOOK'
    }),
        "price":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Price'
    }),
        "genre":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Genre'
    }),
        "author":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'Author'
    }),
        "year":TextInput(attrs={
        'class': 'form-control',
        'placeholder':'date of issue'
    }),
}