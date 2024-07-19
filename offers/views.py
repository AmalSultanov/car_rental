from math import ceil

from django.db.models import Max, Min
from django.views.generic import ListView, DetailView

from offers.models import (CarsImageModel, CarModel, ServicesImageModel,
                           BrandModel, TypeModel, PowerModel, FuelModel,
                           DriveModel, ColorModel, YearModel,
                           TransmissionModel)


class ServicesListView(ListView):
    template_name = 'services.html'
    queryset = ServicesImageModel.objects.all()


class CarsListView(ListView):
    template_name = 'cars.html'
    paginate_by = 9

    def get_queryset(self):
        qs = CarModel.objects.order_by('-pk')
        q = self.request.GET.get('q')

        type = self.request.GET.get('type')
        brand = self.request.GET.get('brand')
        drive = self.request.GET.get('drive')
        fuel = self.request.GET.get('fuel')
        transmission = self.request.GET.get('transmission')
        color = self.request.GET.get('color')
        year = self.request.GET.get('year')
        power = self.request.GET.get('power')
        price = self.request.GET.get('price')

        if q:
            qs = qs.filter(title__icontains=q)

        if type:
            qs = qs.filter(type__id=type)

        if brand:
            qs = qs.filter(brand__id=brand)

        if drive:
            qs = qs.filter(drive__id=drive)

        if fuel:
            qs = qs.filter(fuel__id=fuel)

        if transmission:
            qs = qs.filter(transmission__id=transmission)

        if color:
            qs = qs.filter(color__id=color)

        if year:
            qs = qs.filter(year__id=year)

        if power:
            qs = qs.filter(power__id=power)

        if price:
            price = price.split(';')
            price_from, price_to = price
            qs = qs.filter(price__gte=price_from, price__lte=price_to)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = CarsImageModel.objects.all()
        context['types'] = TypeModel.objects.order_by('-pk')
        context['brands'] = BrandModel.objects.order_by('-pk')
        context['drive'] = DriveModel.objects.order_by('-pk')
        context['fuel'] = FuelModel.objects.order_by('-pk')
        context['transmissions'] = TransmissionModel.objects.order_by('-pk')
        context['colors'] = ColorModel.objects.order_by('-pk')
        context['years'] = YearModel.objects.order_by('-pk')
        context['power'] = PowerModel.objects.order_by('-pk')
        x = ceil(CarModel.objects.count() / self.paginate_by)
        context['page_count'] = range(x)

        max_price, min_price = CarModel.objects.aggregate(
            Max('price'), Min('price')).values()

        context['min_price'] = ceil(min_price)
        context['max_price'] = ceil(max_price)

        return context


class CarsDetailView(DetailView):
    template_name = 'car-detail.html'
    model = CarModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['bg_image'] = CarsImageModel.objects.all()

        return context
