from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from partyou.registration.models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Necessário, no máximo 254 caracteres e deve ser válido.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('O email já está registrado, tente outro.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Endereço'}),
            'link': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Telefone'}),
        }


class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Necessário, no máximo 254 caracteres e deve ser válido.')

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('O email já está registrado, tente outro.')
        return email
