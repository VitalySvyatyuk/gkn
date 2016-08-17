from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from robokassa.forms import RobokassaForm
from .models import Order


def index(request, order_id=1):
    print 'dgdfg'
    order = get_object_or_404(Order, pk=order_id)

    form = RobokassaForm(initial={
               'OutSum': order.total,
               'InvId': order.id,
               'Desc': order.name,
               'Email': order.email,
               # 'IncCurrLabel': '',
               # 'Culture': 'ru'
           })

    return render(request, 'index.html', {'form': form})