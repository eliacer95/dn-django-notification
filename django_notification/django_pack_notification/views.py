from django.http import HttpResponse
from django_notification.django_pack_notification.slack import StoreCreated, Error, UserCreated, send_slack

msg = "<html><body><h2>Se envió correctamnete</h2></body></html>"
msg_error = "<html><body><h2>No se pudo enviar</h2></body></html>"
message = ""
to_user = "everyone"

def MessageStore(request):
    store = "Admin"
    ruc = "20152345678"
    razon_social = "Inversiones Vasquez S.R.L"
    username = "Omelia432"
    email_store = "vasquez@gmail.com"

    data = StoreCreated(to_user, store, ruc, razon_social, username, email_store)
    message = send_slack(data)
    if message:
        return HttpResponse(msg)
    else:
        return HttpResponse(msg_error)


def MessageUser(request):
    full_name = "Eliacer Fernandez"
    email = "hola@gmail.com"
    user = "admin123"

    data = UserCreated(to_user, full_name, email, user)
    message = send_slack(data)
    if message:
        return HttpResponse(msg)
    else:
        return HttpResponse(msg_error)


def MessageError(request):
    title = "Registrar usuario:" # Title o place where the error has happened
    description = "dklwdkeoi,doied.,i" # Error Description
    schema = "adminla" # Schema

    data = Error(to_user, title, schema, description)
    message = send_slack(data)
    if message:
        return HttpResponse(msg)
    else:
        return HttpResponse(msg_error)