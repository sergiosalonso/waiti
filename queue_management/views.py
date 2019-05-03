from django.shortcuts import render

from .forms import FreeCheckOutForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import redis
r = redis.Redis(host='localhost', port=32768, charset="utf-8", decode_responses=True, db=0)

class FreeCheckOutView(LoginRequiredMixin, FormView):
    template_name = 'queue_management/update-queue.html'
    form_class = FreeCheckOutForm
    success_url = reverse_lazy('queue_management:update-queue')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #print("This is a form {}".format(type(form.cleaned_data["check_out_number"])))
        r.lpush("free-checkout", form.cleaned_data["check_out_number"])
        return super().form_valid(form)

class HomePageView(TemplateView):

    template_name = "queue_management/queue.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        check_out_number=r.rpop("free-checkout")

        if check_out_number == None:
            context['check_out_number'] = "Todas las cajas ocupadas espere"
        else:
            context['check_out_number'] = "Dirijase a la caja numero: "+str(check_out_number)
        return context
