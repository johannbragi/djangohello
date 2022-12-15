from django.contrib import admin
from hello_world.models import Author


class TestLink(Author):
    class Meta:
        proxy = True


@admin.register(TestLink)
class TestLinkAdmin(admin.ModelAdmin):
    actions = ["resend_orders"]
    ordering = ["-pk"]
    show_change_link = False
    list_display = [
        "first_name",
        # "created",
        # "order_link",
    ]
