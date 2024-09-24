from django import forms


class MakeTask():
    title = forms.CharField(label="title")
    f