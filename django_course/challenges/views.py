from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
month_dict = {
    'jan' : "jan works",
    'feb': "feb wroks"
}

# Create your views here.
def index(requset):
    month_list = ""
    months = list(month_dict.keys())
    return render(requset, "challenges/index.html",{
            "months":months 
            })



def month_handler_int(requset, month):
    months = list(month_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("This int month Not Supported!")
    suffix_url = months[month -1]
    redirect_path = reverse('monthly_handle_str',  args=[suffix_url], current_app="django_course")
    return HttpResponseRedirect(redirect_path)


def month_handler_str(requset, month):
    try:
        challenge_text= month_dict[month]
        return render(requset, "challenges/challenge.html", {
            "month":month,
            "month_challenge":challenge_text
        })
    except:
        raise Http404()
