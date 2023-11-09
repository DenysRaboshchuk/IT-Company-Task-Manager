from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from manager.models import Worker, Position, TaskType, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = ("username", "email", "position", "first_name", "last_name", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "position")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2", "position", "first_name", "last_name"),
            },
        ),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    search_fields = ("name", )



@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    search_fields = ("name", )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "is_completed","priority", "deadline", "task_type")
    search_fields = ("name", )

admin.site.unregister(Group)