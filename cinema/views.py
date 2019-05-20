from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from cinema.models import Movie
from account.models import Profile
from django.http import JsonResponse


class MovieDetail(DetailView):
    template_name = 'cinema/movie_detail.html'
    model = Movie

    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super(MovieDetail, self).get_context_data(**kwargs)
        #get profile user data from account.models
        context['profile'] = Profile.objects.get(user=self.request.user.pk)
        return context

class MovieSearch(View):
    def post(self, request, *args, **kwargs):
        search_text = request.POST['search_text']
        json_result = []
        if search_text is not None and search_text != u"":
            results = Movie.objects.filter(title__contains=search_text)
        else:
            results = []

        for movie in results:
            json_result.append({
                "title": movie.title,
                "url": movie.get_absolute_url(),
            })
        return JsonResponse({"result": json_result})

class LoginPage(FormView):
    form_class = AuthenticationForm
    # If successful, redirect to home.
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        # if user is authenticated than we need to display a main page with movies
        if request.user.is_authenticated:
            self.template_name = "cinema/movies_list.html"
        # if not, display login page instead
        else:
            self.template_name = "cinema/login-form.html"
        return super(LoginPage, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LoginPage, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            #get profile user data from account.models
            context['profile'] = Profile.objects.get(user=self.request.user.pk)
            # get all Movies from database without filtration
            context['object_list'] = Movie.objects.all()
        else:
            # Call the base implementation first to get a context
            context['form'].fields['username'].label = ""
            context['form'].fields['username'].widget.attrs["placeholder"] = "username"

            context['form'].fields['password'].label = ""
            context['form'].fields['password'].widget.attrs["placeholder"] = "password"
            # get all Movies from database without filtration
            context['object_list'] = Movie.objects.all()
        return context

    def form_valid(self, form):
        # raise an error if user already authenticated
        if not self.request.user.is_authenticated:
            # We receive object of the user on the basis of the data entered into the form.
            self.user = form.get_user()
            # We perform user authentication.
            login(self.request, self.user)
        else:
            raise Http404
        return super(LoginPage, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
