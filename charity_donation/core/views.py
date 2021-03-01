from django.shortcuts import render
from django.views import View
from core.models import Category, Institution, Donation
from django.core.paginator import Paginator


# Create your views here.

class LandingPage(View):

    def get(self, request):
        instytucja = []  # powoduje zajęcie dużej pamieci
        ins_count = Institution.objects.all().count()
        don_count = Donation.objects.all().count()
        # inst = Institution.objects.all()  # https://docs.djangoproject.com/en/3.1/ref/models/expressions/ WINDOW
        # https://stackoverflow.com/questions/49367130/django-orm-group-by-and-find-latest-item-of-each-group-window-functions
        inst_type_1 = Institution.objects.all().filter(type=1)
        inst_type_2 = Institution.objects.all().filter(type=2)
        inst_type_3 = Institution.objects.all().filter(type=3)
        paginator_sys = Paginator(inst_type_1, 5)
        page = request.GET.get('tab1')
        inst_type_1_pag = paginator_sys.get_page(page)
        paginator_sys = Paginator(inst_type_2, 5)
        page = request.GET.get('tab2')
        inst_type_2_pag = paginator_sys.get_page(page)
        paginator_sys = Paginator(inst_type_3, 5)
        page = request.GET.get('tab3')
        inst_type_3_pag = paginator_sys.get_page(page)
        return render(request, 'index.html', context={'ins_count': ins_count, 'don_count': don_count,
                                                      'inst_type_1_pag': inst_type_1_pag,
                                                      'inst_type_2_pag': inst_type_2_pag,
                                                      'inst_type_3_pag': inst_type_3_pag,
                                                      })


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')


class AddDonation(View):

    def get(self, request):
        return render(request, 'form.html')
