from django.shortcuts import render
from task2.forms import ReviewForm
from django.http import HttpResponse
from django.views.generic.edit import FormView


# Create your views here.
class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self,form):
        form.send_email()
        return HttpResponse('Thanks for your review!')