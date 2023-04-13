from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView, FormView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, LoginForm
from django.http import HttpResponse
from django.views.generic import View
# from learn_python_with_5_box_quiz.flashcards.process import html_to_pdf

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


# class GeneratePdf(View):
#     def show_certificate(self, request, *args, **kwargs):
#         pdf = html_to_pdf('accounts/result.html')
#
#         return HttpResponse(pdf, content_type='application/pdf')
