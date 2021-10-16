from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render
from django.views import View
from django.core.mail import send_mail

from apps.frontend.forms.user import UserAuthForm, UserRegistrationForm
from apps.backend.models import User
from core.settings import DEFAULT_FROM_EMAIL


class AuthLoginView(View):
    template_name = 'user/auth-login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        if request.GET.get('error', None):
            request.error = True

        return render(request, self.template_name)

    def post(self, request):
        form = UserAuthForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            if (next := request.GET.get('next', None)):
                return redirect(next)
            else:
                return redirect('home')
        else:
            return render(request, self.template_name, {
                'form': form,
            })


class AuthLogoutView(View):
    def get(self, request):
        logout(request)
        if (next := request.GET.get('next', None)):
            return redirect(next)
        else:
            return redirect('home')


class RegistrationView(View):
    template_name = 'user/registration.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, {})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.users.create_user(username, email, password)
            user.update_token()
            link = f'http://localhost/registration/confirm?token={user.token}'
            send_mail(
                'Регистрация на сайте',
                f'Чтобы закончить регистрацию, перейдите по ссылке:\n{link}',
                DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            return render(request, 'user/registration_done.html', {})
        else:
            return render(request, self.template_name, {
                'form': form,
            })


class RegistrationConfirmView(View):
    template_name = 'user/registration_confirm.html'

    def get(self, request):
        token = request.GET.get('token', None)
        if User.users.filter(token=token):
            user = User.users.get(token=token)
            user.type = User.Type.VERIFIED
            user.save()
            user.update_token()
            return render(request, self.template_name, {})
        else:
            return redirect('home')
