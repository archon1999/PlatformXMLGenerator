from django import forms

from apps.backend.models import User


def check_username_char(char: str):
    return char.isalnum() or char in '._'


class UserAuthForm(forms.Form):
    username = forms.CharField(max_length=255,
                               help_text='Только буквы, цифры, символы "_", "."')
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
        if not User.users.filter(username=username).exists():
            self.add_error('username',
                           'Пользователя с таким логином не существует')
        else:
            password = self.cleaned_data['password']
            user = User.users.get(username=username)
            if not user.check_password(password):
                self.add_error('password', 'Неправильный пароль')
            else:
                if user.type == User.Type.USER:
                    self.add_error('username',
                                   'Вы не подтверждали электронную почту')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data['username']
        if User.users.filter(username=username).exists():
            self.add_error('username',
                           'Пользователя с таким логином уже существует')

        for char in username:
            if not check_username_char(char):
                self.add_error('username', 'Некорректный символ')

        email = self.cleaned_data['email']
        if User.users.filter(email=email).exists():
            self.add_error(
                'username',
                'Пользователя с такой электронной почтой уже существует',
            )

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            self.add_error('password', 'Пароли не совпадают!')
        else:
            if len(password) < 8:
                self.add_error('password',
                               'Длина пароля должна быть не меньше 8')


class UserSettingsForm(forms.Form):
    username = forms.CharField(max_length=255)
    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    date_of_birth = forms.DateField(required=False)
    new_username = forms.CharField(
        min_length=3,
        max_length=25,
        required=False,
        help_text='Только буквы, цифры, символы "_", "."',
    )
    password = forms.CharField(widget=forms.PasswordInput(),
                               required=False)
    old_password = forms.CharField(widget=forms.PasswordInput(),
                                   required=False)
    new_password = forms.CharField(widget=forms.PasswordInput(),
                                   required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(),
                                       required=False)

    def clean(self):
        username = self.cleaned_data['username']
        user = User.users.get(username=username)
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        if new_password != confirm_password:
            text = 'Пароли не совпадают'
            self.add_error('confirm_password', text)

        new_username = self.cleaned_data['new_username']
        if User.users.filter(username=new_username).exists():
            text = 'Пользователь с таким логином существует'
            self.add_error('new_username', text)

        for char in new_username:
            if not check_username_char(char):
                self.add_error('new_username', 'Некорректный символ')

        password = self.cleaned_data['password']
        if new_username and not user.check_password(password):
            text = 'Неверный пароль'
            self.add_error('password', text)

        old_password = self.cleaned_data['old_password']
        if old_password and not user.check_password(old_password):
            text = 'Неверный пароль'
            self.add_error('old_password', text)
