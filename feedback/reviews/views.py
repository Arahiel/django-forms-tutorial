from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
# Create your views here.


def review(request: HttpRequest):
    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("thank-you"))
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form,
    })


def thank_you(request: HttpRequest):
    return render(request, "reviews/thank_you.html")
