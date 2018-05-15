import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import restlist
from django.db.models import Q
from .form import restcreate, restcreateclass

from django.http import HttpResponseRedirect


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


class restlistview(ListView):
    template_name = 'restraunt\list_of_restraunts.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = restlist.objects.filter(
                Q(location__icontains=slug) |
                Q(location__iexact=slug)
            )
        else:
            queryset = restlist.objects.all()
        return queryset


class restdetailview(DetailView):
    template_name = 'restraunt/restraunt_detailview.html'

    # queryset = restlist.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(restdetailview, self).get_context_data(*args, **kwargs)
    #     return context

    def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get("rest_id")

        object = get_object_or_404(restlist, id=rest_id)
        return object

@login_required(login_url='/login')
def restform(request):
    template_name = 'restraunt/form.html'
    form = restcreateclass(request.POST or None)

    if request.method == "POST":

        # name = request.POST.get("title")
        # location = request.POST.get("location")
        # obj = restlist.objects.create(
        #     name=name,
        #     location=location
        # )
        # form = restcreate(request.POST)

        if form.is_valid():
            if request.user.is_authenticated():
                instance = form.save(commit=False)
                instance.owner = request.user
                instance.save()
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        else:
            print(form.errors)
    context = {"form": form}
    return render(request, template_name, context)



class restformcreateview(LoginRequiredMixin, CreateView):
    template_name = 'restraunt/form.html'
    login_url = '/login/'
    form_class = restcreateclass
    success_url = '/restraunts_list/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(restformcreateview, self).form_valid(form)
