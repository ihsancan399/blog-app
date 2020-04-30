from django import forms
from django.contrib.auth.middleware import RemoteUserMiddleware
from datetime import datetime,timedelta
from django.conf import settings
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Kullanıcı Adı")
    first_name = forms.CharField(max_length=25, min_length=2, label="Adınız")
    last_name = forms.CharField(max_length=25, min_length=2, label="Soyadınız")
    password = forms.CharField(
        max_length=45,min_length=6,label="Parola",widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        max_length=45,min_length=6,label="Parolayı Doğrula",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if (password) and (confirm_password) and (password != confirm_password):
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        values = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "password": password,
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)


class AutoLogout:
  def process_request(self, request):
    if not request.user.is_authenticated():
      #Can't log out if not logged in
      return

    try:
      if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
        auth.logout(request)
        del request.session['last_touch']
        return
    except KeyError:
      pass

    request.session['last_touch'] = datetime.now()

