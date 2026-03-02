from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, FAQ


@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    model = Users

    list_display = (
        "id",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )

    search_fields = ("email",)
    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),

        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),

        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_superuser",
                "is_active",
            ),
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "created_at")
    search_fields = ("question",)
    ordering = ("-created_at",)