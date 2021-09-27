from django import forms
from . models import GameModel,GameModelYourself


class GameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['computer', 'gamer']
    def __init__(self, *args, **kwargs):
        super(GameModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {"class": "form-control"}
            self.fields['computer'].widget.attrs['readonly'] = True
            self.fields['gamer'].widget.attrs['readonly'] = True

class GameModelYourselfForm(forms.ModelForm):
    gamer = forms.ChoiceField(choices=GameModelYourself.SELECT, widget=forms.RadioSelect())
    class Meta:
        model = GameModelYourself
        fields = ['computer', 'gamer']

    def __init__(self, *args, **kwargs):
        super(GameModelYourselfForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['computer'].widget = forms.HiddenInput()


