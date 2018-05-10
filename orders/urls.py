from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^create/$',views.order_create,name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/$',views.admin_order_detail,name='admin_order_detail'),

    url(r'^complete/$',views.order_complete,name='order_complete'),
    url(r'^create_ajax/$', views.OrderCreateAjaxView.as_view(), name='order_create_ajax'),
    url(r'^checkout/$', views.OrderCheckoutAjaxView.as_view(), name='order_checkout'),
    url(r'^validation/$', views.OrderImpAjaxView.as_view(), name='order_validation'),
]