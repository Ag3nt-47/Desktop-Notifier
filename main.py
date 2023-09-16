from plyer import notification

notification_title = "Merhaba bu test başlığıdır."
notification_description = "Hmm bunu okuduğuna göre demekki kod çalışıyor.. niceee"

notification.notify(
    title = notification_title,
    message = notification_description,
    app_icon = "trojan.jpg",
    timeout = 5,
    toast = False
)
