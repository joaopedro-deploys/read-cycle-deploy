from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from ..forms import LoginForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, ModelFormMixin
from django.views import View
from ..forms import UserForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from ..auth import AppDjangoAuth, GenericAuth
from django.shortcuts import get_object_or_404
from ..forms import UserInfoForm
from utils import Message
from ..services import fetch_user_loc_data
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings

UserModel = get_user_model()    


class LoginView(View):
    """ so far im use the django_auth default, but i was make a depency injection at top auth class, if i implement another type of auth """
    @method_decorator(cache_page((int(settings.TIME_CACHE_LIST_VIEWS) * 60))) 
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form})

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]

        default_auth = AppDjangoAuth() #default django_auth
        user_auth = GenericAuth(default_auth) # change to other auth, if necessary
        authenticated = user_auth.make_authenticate(request=request, email=email, password=password)

        if authenticated:
            return redirect(reverse('main:home-page'))
        else:
            messages.error(request=request, message='Credenciais inválidas')
            return redirect('main:login-page')

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        default_auth = AppDjangoAuth()         
        user =  GenericAuth(default_auth)
        user.logout(request=request)
        return redirect('main:login-page')



class CreateUser(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'main/create_user.html'
    success_url = reverse_lazy('main:login-page')

    def form_valid(self, form): 
        #a callback to display when the post form is valid
        user = form.save(commit=False)

        user_loc = fetch_user_loc_data(user=form.cleaned_data)
        user.latitude =  user_loc.get('lat')
        user.longitude = user_loc.get('lng')
        user.save()        
        #display the task to send confirmation email

        return super().form_valid(form) 

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        invalid = super().form_invalid(form)
        print('form: ', form, form.errors)
        messages.error(self.request, f'Erro ao criar usuário: {form.errors}' )
        return invalid

class EditeUserView(View, ModelFormMixin, LoginRequiredMixin):
    """ view to edit with post and patch """
    model = UserModel
    form_class = UserInfoForm
    
    def get_context_data(self, **kwargs: dict) -> dict[str]:
        context  = super().get_context_data(**kwargs)
        context['user_form'] = UserInfoForm(instance=self.get_object())

    def post(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            form = self.form_class(instance=self.object, data=request.POST)

            if form.is_valid():
                form.save()
                messages = [Message('usuário atualizado com sucesso', 'success')]

        except Exception as err:
            messages = [Message(f'Erro ao atualizar usuário: {err}', 'error')]

        return render(
            request,
            'main/render_user_info_form.html',
            context={
                'user_form': form,
                'messages': messages
            }
        )

    def get_object(self, *args, **kwargs):  
        return get_object_or_404(
            UserModel.objects.filter(
                uuid=self.kwargs.get('id')
            )
        )
    

    
