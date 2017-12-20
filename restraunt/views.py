import random
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from .models import restlist

# Create your views here.

#
# def home(request):
#     num = random.randint(0, 12238)
#     sumlist = ["a", "b", "c", "d"]
#     return render(request, "home.html", {"num": num, "sumlist": sumlist})
#
#
# def about(request):
#     context = {}
#     return render(request, "about.html", context)
#
#
# def contact(request):
#     context = {"num": 3}
#     return render(request, "contact.html", context)


# class ContactView(View):
#     def get(self, request):
#         context = {}
#         return render(request, "contact.html", context)

#
# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(HomeView, self).get_context_data(*args, **kwargs)
#         num = random.randint(0, 10000)
#         sumlist = ["a", "b", "c", "d"]
#         context = {
#             "num": num,
#             "sumlist": sumlist
#         }
#         return context
#
#
# class AboutView(TemplateView):
#     template_name = 'about.html'
#
#
# class ContactView(TemplateView):
#     template_name = 'contact.html'
#
#     def get_context_data(self, *args, **kwargs):
#         # context = super(ContactView, self).get_context_data(*args, **kwargs)
#         contextt = {
#             "num": 3
#         }
#         return contextt


def list_of_restraunts(request):
    template_name = 'restraunt\list_of_restraunts.html'
    queryset = restlist.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)


