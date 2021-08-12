from django import forms


# Forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CreateTicketForm(forms.Form):
    title = forms.CharField(max_length=120)
    description = forms.CharField(widget=forms.Textarea)
