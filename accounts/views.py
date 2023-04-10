from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, LoginForm
from django.http import HttpResponse

from .models import CustomUser

# Create your views here

User = get_user_model()


class RegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('flashcard')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *arg, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("flashcard")
        return super(RegisterView, self).get(*arg, **kwargs)


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)


@login_required
def profile(request):
    user = CustomUserCreationForm(instance=request.user)
    return render(request, 'accounts/profile.html', {"user": user})
