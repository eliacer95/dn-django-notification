from datetime import date

import requests
import json

from django.conf import settings

format = {'Content-Type': 'application/json'}


def StoreCreated(to_user, store, ruc, razon_social, username, email_store):
    title = "Datos de la tienda:"
    pretext = "*@ %s* Se ha agregado un nueva tienda:" % (to_user)
    text = "*Tienda:* %s \n*Ruc:* %s\n*Razón Social:* %s \n*Usuario:* %s \n*Email:* %s" % (
    store, ruc, razon_social, username, email_store)
    data = {"attachments": [
        {"title": title, "pretext": pretext, "text": text, "color": "#7CD197", "mrkdwn_in": ["text", "pretext"]}]}

    return data


def UserCreated(to_user, full_name, email, user):
    title = "Datos del usuario:"
    pretext = "*@ %s* Se ha agregado un nuevo usuario:" % (to_user)
    text = "*Nombre:* %s \n*Fecha:* %s\n*Correo:* %s \n*Usuario:* %s" %(full_name, date.today(), email, user)
    data = {"attachments": [{"title": title, "pretext": pretext, "text": text, "color": "#7CD197", "mrkdwn_in": ["text", "pretext"]}]}

    return data


def Error(to_user, title, schema, description):
    pretext = "*@ %s* Mensaje de error:" % (to_user)
    schema_ = "Esquema: %s \n %s" %(schema, title)
    text = "```\n%s\n```" % (description)
    data = {"attachments": [{"title": schema_, "pretext": pretext, "text": text, "color": "#F02742", "mrkdwn_in": ["text", "pretext"]}]}

    return data


def send_slack(data):
    r = requests.post(settings.SLACK_DEFAULT_URL, data=json.dumps(data), headers=format)
    if r.status_code == 200:
        return True
    else:
        return False
