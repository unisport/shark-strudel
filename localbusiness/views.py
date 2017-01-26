from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from .models import LocalBusiness, OpeningHours
from .forms import LocalBusinessForm

import sys
import json


class IndexView(generic.ListView):
    template_name = 'localbusiness/index.html'
    context_object_name = 'localbusiness_list'

    def get_queryset(self):
        """Return the list of localbusiness"""
        return LocalBusiness.objects.order_by('name')


def create_view(request):
    form = LocalBusinessForm

    if request.method == 'POST':
        form = LocalBusinessForm(request.POST)
        if form.is_valid():
            lb = form.save(commit=False)
            lb.save()

            return redirect('/localbusiness/{0}/edit'.format(lb.pk))

    return render(request, 'localbusiness/form.html', {'form': form})


def edit_view(request, lb_pk):
    lb = LocalBusiness.objects.get(pk=lb_pk)
    form = LocalBusinessForm(instance=lb)

    if request.method == 'POST':
        form = LocalBusinessForm(request.POST, instance=lb)
        if form.is_valid():
            lb = form.save(commit=False)
            lb.save()

            return redirect('/localbusiness/')

    return render(request, 'localbusiness/form.html', {'form': form, 'lb': lb})


@csrf_exempt
def add_opening_hours(request, lb_pk):
    lb = LocalBusiness.objects.get(pk=lb_pk)
    if request.is_ajax():
        try:
            json_data = json.loads(request.body)
            try:
                """ Updating """
                pk = json_data['oh_pk']
                opening_hours = OpeningHours.objects.get(pk=int(pk))
                opening_hours.display_order = json_data['oh_display_order']
                opening_hours.opening_hours = json_data['oh_opening']
                opening_hours.save()

                return JsonResponse({'opening_hours_pk': opening_hours.pk,
                    'oh_display_order': opening_hours.display_order,
                    'oh_opening': opening_hours.opening_hours})
            except KeyError:
                """ Creating """
                opening_hours = OpeningHours(opening_hours=json_data['oh_opening'],
                        display_order=json_data['oh_display_order'], localbusiness=lb)
                opening_hours.save()

            """FIXME: UnboundLocalError: local variable 'opening_hours' referenced before assignment"""
            return JsonResponse({'opening_hours_pk': opening_hours.pk,
                'display_order': opening_hours.display_order})

        except ValueError:
            return JsonResponse({'error': 'bollogs'})


@csrf_exempt
def remove_opening_hours(request, oh_pk):
    if request.is_ajax():
        print >>sys.stderr, request.body
        try:
            json_data = json.loads(request.body)
            opening_hours = OpeningHours.objects.get(pk=json_data['opening_hours_pk'])
            opening_hours.delete()

            return JsonResponse({'deleted': json_data['opening_hours_pk']})

        except ValueError:
            return JsonResponse({'error': 'bollogs'})
