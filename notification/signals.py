import django.dispatch

forum_answered = django.dispatch.Signal(providing_args=["ask", "answer", "author"])
forum_ask_updated  = django.dispatch.Signal(providing_args=["ask"])

post_comment = django.dispatch.Signal(providing_args=["post", "comment", "author"])

wiki_request_checked = django.dispatch.Signal(providing_args=["request"])
wiki_request_created = django.dispatch.Signal(providing_args=["request"])