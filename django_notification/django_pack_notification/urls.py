from django.conf.urls import url

from django_notification.django_pack_notification.views import MessageStore, MessageUser, MessageError

urlpatterns = [
    url(r'^user/registered$', MessageUser),
    url(r'^store/created$', MessageStore),
    url(r'^notification/error$', MessageError),
]
