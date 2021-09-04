from django import forms
from django.contrib.auth import get_user_model

MyUser = get_user_model()


class MyUserForm(forms.ModelForm):

    address = forms.CharField(widget=forms.Textarea, required=False)
    profile_pic = forms.ImageField(label="Profile Picture", required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(MyUserForm, self).clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")

        if password != confirm:
            self.add_error('confirm', "Password does not match")
        return cleaned_data

    class Meta():
        model = MyUser
        fields = ['full_name', 'email', 'phone', 'address', 'profile_pic', 'password', 'confirm']


class MyUserEditForm(MyUserForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm = forms.CharField(widget=forms.PasswordInput, required=False)


class NumberstoWordsForm(forms.Form):
    enter_number = forms.CharField(widget=forms.NumberInput)