from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

# Create a custom user creation form with the additional fields
class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'profile_picture', 'email', 'address_line1', 'city', 'state', 'pincode')

    # Override the clean method to check if the password and confirm password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password1')
        confirm_password = cleaned_data.get('password2')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('The passwords do not match.')
        return cleaned_data
