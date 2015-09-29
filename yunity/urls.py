
from django.conf.urls import include, url

import yunity.views.auth
import yunity.views.mappable
import yunity.views.chat


urlpatterns = [
    url(r'^login/', yunity.views.auth.LoginView.as_view()),
    url(r'^register/', yunity.views.auth.RegisterView.as_view()),
    url(r'^mappables/new', yunity.views.mappable.CreateMappableView.as_view()),
    url(r'^mappables/(?P<mappable_id>[0-9]+)', yunity.views.mappable.GetMappableView.as_view()),
    url(r'^msg/post', yunity.views.chat.post_chat_view),
    url(r'^msg/(?P<chatid>[0-9]+)', yunity.views.chat.GetChatView.as_view())
]