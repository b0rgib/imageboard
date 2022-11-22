from django import forms


class CreateNewThread(forms.Form):
    name = forms.CharField(label='Имя', max_length=20, required=False)
    head = forms.CharField(label='Заголовок', max_length=30)
    text = forms.CharField(label='Текст', max_length=1000,
                           widget=forms.Textarea)
    media = forms.FileField(required=True)


class CreateNewPost(forms.Form):
    name = forms.CharField(label='Имя', max_length=20, required=False)
    text = forms.CharField(label='Текст', max_length=1000,
                           widget=forms.Textarea)
    sage = forms.BooleanField(label='Не поднимать тред', required=False)
    media = forms.FileField(required=False)
