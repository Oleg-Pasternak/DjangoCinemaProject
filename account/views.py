from django.shortcuts import render, redirect
from account.models import Profile
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.urls import reverse


class RegisterFormView(CreateView):
    template_name = "registration/register.html"
    # Default Django Form
    form_class = UserCreationForm
    # If successful, redirect to home.
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        password = form.cleaned_data.get('password1')
        if password:
            new_user = form.save(commit=False)
            new_user.set_password(password)
            new_user.save()
            profile, is_created = Profile.objects.get_or_create(user=new_user)
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RegisterFormView, self).get_context_data(**kwargs)
        context['form'].fields['username'].label = ""
        context['form'].fields['username'].widget.attrs["placeholder"] = "username"

        context['form'].fields['password1'].label = ""
        context['form'].fields['password1'].widget.attrs["placeholder"] = "password"

        context['form'].fields['password2'].label = ""
        context['form'].fields['password2'].widget.attrs["placeholder"] = "confirmation"
        return context


class ProfileView(TemplateView):
    model = Profile
    template_name = "registration/profile.html"

    #Get profile user data from account.models
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(*args, **kwargs)
        context['profile'] = Profile.objects.get(user=self.request.user.pk)
        return context

    def post(self, request, *args, **kwargs):
        # if user is auntheticated
        if request.user.is_authenticated:
            # get user from Django Auth system
            user = request.user
            # Get profile using User object
            try:
                profile = Profile.objects.get(user=user.pk)
            except Profile.DoesNotExists:
                # if user does not exists
                return redirect("/")  # тут можно перенаправить на страницу с ошибкой

            # Get values from form
            # Note: POST is a simple dict {key: value}, so we using .get() method,
            # which will return None in case if field is empty
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            birthday = request.POST.get('birthday')
            image = request.FILES.get('image')
            print(birthday, image)
            # Check if all fields is valid
            if first_name or last_name or birthday or image:
                # if birthday / image / name was changed
                if (first_name and profile.first_name != first_name) or (last_name and profile.last_name != last_name) or (birthday and profile.birthday != birthday) or (image and profile.image != image):
                    profile.first_name = first_name
                    profile.last_name = last_name
                    profile.birthday = birthday
                    profile.image = image
                    profile.save()
        return redirect("/")
