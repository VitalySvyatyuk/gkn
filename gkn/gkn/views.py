from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from robokassa.forms import RobokassaForm
from .models import Order


def index(request):
    return render(request, 'index.html')


# @login_required
def pay_with_robokassa(request, order_id=1):
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

    return render(request, 'pay_with_robokassa.html', {'form': form})