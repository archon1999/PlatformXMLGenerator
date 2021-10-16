from django.shortcuts import redirect, render
from django.views import View

from apps.frontend.forms.user import UserSettingsForm
from apps.backend.models import User


def user_settings_update(user: User, form: UserSettingsForm):
    if not form.has_error('first_name'):
        user.first_name = form.cleaned_data['first_name']

    if not form.has_error('last_name'):
        user.last_name = form.cleaned_data['last_name']

    if not form.has_error('date_of_birth'):
        user.date_of_birth = form.cleaned_data['date_of_birth']

    new_password = form.cleaned_data['new_password']
    if not form.has_error('old_password') and \
       not form.has_error('confirm_password') and \
       new_password:
        user.set_password(new_password)

    new_username = form.cleaned_data['new_username']
    if not form.has_error('new_username') and \
       not form.has_error('password') and new_username:
        user.username = form.cleaned_data['new_username']

    user.save()


class ProfileView(View):
    template_name = 'user/profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            return render(request, self.template_name, {
                'user': user,
            })
        else:
            return redirect('login')


class UserSettingsView(View):
    template_name = 'user/settings.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            return render(request, self.template_name, {
                'user': user,
            })
        else:
            return redirect('login')

    def post(self, request):
        user = request.user
        form = UserSettingsForm(request.POST, request.FILES)
        form.is_valid()
        username = form.cleaned_data['username']
        if username != user.username:
            return redirect('home')

        user_settings_update(user, form)
        return render(request, self.template_name, {
            'form': form
        })
