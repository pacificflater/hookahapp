from hookahapp.sklad.models import Manufacturer, Flavour, Mix, Membership
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from hookahapp.sklad.serializers import ManufacturerListSerializer, FlavourSerializer, MixSerializer, MembershipSerializer, MembershipCreateSerializer, FlavourCreateSerializer
from rest_framework import permissions, viewsets

class Manufacturers(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all().order_by('name')
    serializer_class = ManufacturerListSerializer
    permission_classes = [permissions.IsAuthenticated]

class FlavoursView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Flavour.objects.all().order_by('manufacturer__name', 'flavour_name')
    def get_serializer_class(self):
        if self.action == "create":
            return FlavourCreateSerializer
        elif self.action == "update":
            return FlavourCreateSerializer
        return FlavourSerializer

class MixesView(viewsets.ModelViewSet):
    serializer_class = MixSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Mix.objects.all().order_by('mix_name')

class MembershipView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Membership.objects.all().order_by('flavour__flavour_name')
    def get_serializer_class(self):
        if self.action == "create":
            return MembershipCreateSerializer
        elif self.action == "update":
            return MembershipCreateSerializer
        return MembershipSerializer



# def index(request):
#     context = {'index': index}
#     return render(request, 'sklad/index.html', context)
#
# class InStockView(generic.ListView):
#     template_name = 'sklad/in_stock.html'
#     model = Manufacturer
#     def get_queryset(self):
#         return Manufacturer.objects.all()

# class Manufacturers(generic.ListView):
#     template_name = 'sklad/manufacturer.html'
#     model = Manufacturer
#     def get_queryset(self):
#         return Manufacturer.objects.all()

# class ManufacturerCardView(viewsets.ModelViewSet):
#     serializer_class = ManufacturerCardSerializer
#     # model = Manufacturer
#     # permission_classes = [permissions.IsAuthenticated]
#     template_name = 'sklad/manufacturer_card.html'
#     # queryset = Manufacturer.objects.all()



# def flavour_form(request, manufacturer_id):
#     context = {'manufacturer_id': manufacturer_id}
#     return render(request, 'sklad/flavour_form.html', context)

# def flavour_add(request, manufacturer_id):
#     manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
#     flavour_name = request.POST['flavour_name']
#     in_stock = request.POST.get('in_stock', False)
#     manufacturer.flavour_set.create(flavour_name=flavour_name, in_stock=in_stock, add_time=timezone.now())
#     manufacturer.save()
#     return HttpResponseRedirect(reverse('sklad:manufacturer_card', args=(manufacturer_id,)))

# def manufacturer_form(request):
#     return render(request, 'sklad/manufacturer_form.html')

# def manufacturer_create(request):
#     name = request.POST['name'],
#     manufacturer = Manufacturer(name=name[0])
#     manufacturer.save()
#     return HttpResponseRedirect(reverse('sklad:manufacturers'))

# def manufacturer_delete(request, manufacturer_id):
#     manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
#     manufacturer.delete()
#     return HttpResponseRedirect(reverse('sklad:manufacturers'))

# class FlavourCard(viewsets.ModelViewSet):
#     manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
#     queryset = manufacturer.flavour_set.get(pk=flavour_id)

# def flavour_card(request, manufacturer_id, flavour_id):
#     try:
#         manufacturer = get_object_or_404(Manufacturer, pk=manufacturer_id)
#         flavour = manufacturer.flavour_set.get(pk=flavour_id)
#         context = {
#             'flavour': flavour,
#             'manufacturer': manufacturer
#         }
#         return render(request, 'sklad/flavour_card.html', context)
#     except Flavour.DoesNotExist:
#         raise Http404('Flavour does not exist')

# def flavour_delete(request, manufacturer_id, flavour_id ):
#     manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
#     flavour = manufacturer.flavour_set.filter(pk=flavour_id)
#     flavour.delete()
#     return HttpResponseRedirect(reverse('sklad:flavour_list', args=(manufacturer_id,)))





