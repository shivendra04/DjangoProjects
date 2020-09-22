from django import forms
from django.core import validators

# my own validator
def starts_with(value):
    if value[0].lower()!='s':
        raise forms.ValidationError('Name should start with s')

class FeedBackForm(forms.Form):
        name=forms.CharField(validators=[starts_with])
        rollno=forms.IntegerField()
        email=forms.EmailField()
        password=forms.CharField(widget=forms.PasswordInput)
        rpassword=forms.CharField(label='password(again)', widget=forms.PasswordInput)
        feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
        bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

        '''def clean_name(self):
            inputname=self.cleaned_data['name']
            if len(inputname)<4:
                raise forms.ValidationError('The length of name should be >=4')
            return inputname'''
        def clean(self):
            print('Total forms validation')
            cleaned_data=super().clean()
            inputpwd=cleaned_data['password']
            inputrpwd=cleaned_data['rpassword']
            print('BOT Validation..')
            bot_handler_value=cleaned_data['bot_handler']
            if len(bot_handler_value)>0:
                raise forms.ValidationError('Thanks BOT!!')

            if inputpwd!=inputrpwd:
                raise forms.ValidationError('Password must be same')
