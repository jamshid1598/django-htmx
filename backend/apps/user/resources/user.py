from import_export import (
    resources,
    fields,
)
from import_export.widgets import (
    BooleanWidget,
    DateTimeWidget,
)
from ..models import (
    User,
)

class UserResource(resources.ModelResource):
    id           = fields.Field(attribute="id", column_name="id")
    username     = fields.Field(attribute="username", column_name="(username)")

    is_active    = fields.Field(attribute="is_active", column_name="Fa'ol User", widget=BooleanWidget())
    is_staff     = fields.Field(attribute="is_staff", column_name="Kichchik Admin", widget=BooleanWidget())
    is_superuser = fields.Field(attribute="is_superuser", column_name="Super Admin", widget=BooleanWidget())
    
    last_login = fields.Field(attribute="last_login", column_name="Oxirgi Fa'olik", widget=DateTimeWidget("%d-%m-%Y %H:%M:%S"))
    updated_at = fields.Field(attribute="updated_at", column_name="O\'zgartirish kiritilgan vaqti", widget=DateTimeWidget("%d-%m-%Y %H:%M:%S"))
    created_at = fields.Field(attribute="created_at", column_name="Yaratilgan vaqti", widget=DateTimeWidget("%d-%m-%Y %H:%M:%S"))

    class Meta:
        model = User
        fields = (
            "id", "username",
            "is_active", "is_staff", "is_superuser",
            "last_login", "updated_at", "created_at",
        )
        export_order = (
            "id", "username",
            "is_active", "is_staff", "is_superuser",
            "last_login", "updated_at", "created_at",
        )
        exclude = (
            "image", "change_pw", "groups", "user_permissions",
        )
