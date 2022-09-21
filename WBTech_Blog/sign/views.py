from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import RegisterForm


class BaseRegisterView(CreateView):
    """
    Он имеет несколько атрибутов:
    модель формы, которую реализует данный дженерик;
    форма, которая будет заполняться пользователем;
    URL, на который нужно направить пользователя после успешного ввода данных в форму.
    """
    model = User
    form_class = RegisterForm
    success_url = '/'