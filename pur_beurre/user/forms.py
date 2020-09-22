"""
Gestion des formulaires
enregistrement / validation des données utilistateur
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    """
    Utilsation du formulaire standard
    avec ajout du champ 'email'
    """

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # TODO : Pour la modification la vérification ne doit se faire
        # uniquement que si le user courant est de type anonyme
        if User.objects.filter(email=email):
            print('Cet email est déjà utilisé. Veuillez recommencer.')
            raise forms.ValidationError('Cet email est déjà utilisé.'
                                        ' Veuillez recommencer.',
                                        code='invalid')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            print('Les mots de passe ne correspondent pas. '
                  'Veuillez les saisir à nouveau.')
            raise forms.ValidationError('Les mots de passe ne '
                                        'correspondent pas.'
                                        ' Veuillez les saisir à nouveau.',
                                        code='invalid')
        return password2

    def clean(self):
        super(CustomUserCreationForm, self).clean()
        data = self.cleaned_data
        if "password1" not in data:
            data["password1"] = ""
        if "password2" not in data:
            data["password2"] = ""
        if data["password1"] != data["password2"]:
            print('Les mots de passe doivent être identiques !')
            raise forms.ValidationError(
                {'password1': ["Les mots de passe doivent être identiques."]}
            )
        return data


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Email utilisateur'
