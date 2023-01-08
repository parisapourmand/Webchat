from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2")
