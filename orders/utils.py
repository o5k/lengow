# coding=utf-8
from django.http import JsonResponse

import xml.etree.ElementTree as ET
import requests

from .models import Order


def parse_url(request):
    # url = "http://test.lengow.io/orders-test.xml"
    url = request.POST['url'].encode('ascii', 'ignore')
    if not url:
        return {'success': False, 'data': "Aucune URL n'a été spécifiée"}
    try:
        flux = requests.get(url)
        if flux.status_code != 200:
            return {'success': False, 'data': "URL invalide"}
        tree = ET.fromstring(flux.text.encode('ascii', 'ignore'))
        orders_to_save = []
        orders_invalid = []
        for child in tree.iter('order'):
            order = Order()
            order.marketplace = child.find('marketplace').text
            order.order_id = child.find('order_id').text
            order.order_purchase_date = child.find('order_purchase_date').text or '-'
            order.order_purchase_heure = child.find('order_purchase_heure').text or '-'
            order.order_amount = child.find('order_amount').text
            if order.marketplace is None or order.order_id is None or order.order_amount is None:
                orders_invalid.append(order)
            else:
                orders_to_save.append(order)
        return {
            'success': True,
            'orders_to_save': orders_to_save,
            'orders_invalid': orders_invalid
        }
    except:
        return {'success': False, 'data': "Veuillez spécifier une URL valide d'un flux XML"}
