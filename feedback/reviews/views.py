from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .forms import ReviewForm
from .models import Review
# Create your views here.


class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = reverse_lazy("thank-you")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        return base_query.filter(rating__gt=3)


class ReviewDetailsView(DetailView):
    template_name = "reviews/review_details.html"
    model = Review
