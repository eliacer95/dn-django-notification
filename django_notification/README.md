# django-pack-notification
This library allows you to send notifications from Django to Slack

### Requirements
* Create an app in your Slack group.
* Generate a Webhook URL for channel that you will send the notifications or messages.

### Installation 
```sh
$ pip install django-pack-notification
```
Add in settings.py the link
```py
# Url general Channel
SLACK_DEFAULT_URL = "https://hooks.slack.com/services/XXXXXXXXX/YYYYYYYY/OXbi63xBPrGeceUMsEsTngUA"
```
Here you can guide by this example:
```py
msg = "<html><body><h2>It sended succesfully.</h2></body></html>"
msg_error = "<html><body><h2>It couldn't send.</h2></body></html>"
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
```
The function StoreCreated() returns the data sended parse in JSON format According to a message style that will be displayed in Slack.
The functiont send_slack() will send the notification using a POST request.

### All functions:
* StoreCreated(to_user, store, ruc, razon_social, username, email_store)
* UserCreated(to_user, full_name, email, user)
* Error(to_user, title, schema, description)
* send_slack(data)

Until now, the parameters each function parse in JSON, are basic forms to send message from django to Slack.
