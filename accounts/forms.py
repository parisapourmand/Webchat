from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام‌کاربری"
        self.fields['first_name'].label = "نام"
        self.fields['last_name'].label = "نام‌خانوادگی"
        self.fields['password1'].label = "رمز عبور"
        self.fields['password2'].label = "تکرار رمز عبور"
        for field in ["username", "first_name", "last_name", "password1", "password2"]:
            self.fields[field].help_text = None

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.is_active = None
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")


class CustomLogInForm(AuthenticationForm):
    error_messages = {
        "invalid_login":
            "رمز یا نام‌کاربری اشتباه است، " +
            "یا اکانت شما فعال نشده است.",
        "inactive": "اکانت شما فعال نشده است. تا تایید توسط پشتیبانی شکیبا باشید.",
    }

    def __init__(self, *args, **kwargs):
        super(CustomLogInForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام‌کاربری"
        self.fields['password'].label = "رمز عبور"
