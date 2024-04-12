from apps.models import Order


class NewOrderProxy(Order):
    class Meta:
        proxy = True
        verbose_name = 'yangi zakaz'
        verbose_name_plural = 'yangi zakazlar'


class CancelOrderProxy(Order):
    class Meta:
        proxy = True
        verbose_name = 'bekor qilingan zakaz'
        verbose_name_plural = 'bekor qilingan zakazlar'


class CompletedOrderProxy(Order):
    class Meta:
        proxy = True
        verbose_name = 'tugatilgan zakaz'
        verbose_name_plural = 'tugatilgan zakazlar'
