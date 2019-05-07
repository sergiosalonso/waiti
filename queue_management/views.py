from django.shortcuts import render
from .forms import FreeCheckOutForm, CheckOutNumberForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
import redis
r = redis.Redis(host='localhost', port=32768, charset="utf-8", decode_responses=True, db=0)

class CheckOutNumberView(LoginRequiredMixin, FormView):
    template_name = 'queue_management/update-queue.html'
    form_class = CheckOutNumberForm
    success_url = reverse_lazy('queue_management:free-queue')
    
    def form_valid(self, form):
        #print("This is a form {}".format(type(form.cleaned_data["check_out_number"])))
        user=str(self.request.user)
        print(user)
        r.set("user:"+user, form.cleaned_data["check_out_number"])
        return super().form_valid(form)

class FreeCheckOutView(LoginRequiredMixin, FormView):
    template_name = 'queue_management/free-queue.html'
    form_class = FreeCheckOutForm
    success_url = reverse_lazy('queue_management:free-queue')

    def form_valid(self, form):
        #print("This is a form {}".format(type(form.cleaned_data["check_out_number"])))
        user=str(self.request.user)
        number=int(r.get("user:"+user))
        r.lpush("free-checkout", number)
        return super().form_valid(form)

class HomePageView(TemplateView):

    template_name = "queue_management/queue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        check_out_number=r.rpop("free-checkout")

        if check_out_number == None:
            context['check_out_number'] = "Espere, en breve se le asignará una caja "
        else:
            context['check_out_number'] = "Dirijase a la caja numero: "+str(check_out_number)
        return context
