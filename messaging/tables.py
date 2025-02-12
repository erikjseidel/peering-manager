import django_tables2 as tables

from messaging.models import Contact, ContactAssignment, ContactRole, Email
from utils.tables import (
    BaseTable,
    BooleanColumn,
    ButtonsColumn,
    ContentTypeColumn,
    SelectColumn,
    TagColumn,
    linkify_phone,
)

__all__ = ("ContactTable", "ContactRoleTable")


class ContactRoleTable(BaseTable):
    pk = SelectColumn()
    name = tables.Column(linkify=True)
    actions = ButtonsColumn(ContactRole, buttons=("edit", "delete"))

    class Meta(BaseTable.Meta):
        model = ContactRole
        fields = ("pk", "name", "slug", "description", "actions")
        default_columns = ("pk", "name", "description", "actions")


class ContactTable(BaseTable):
    pk = SelectColumn()
    name = tables.Column(linkify=True)
    phone = tables.Column(linkify=linkify_phone)
    assignment_count = tables.Column(verbose_name="Assignments")
    tags = TagColumn(url_name="messaging:contact_list")
    actions = ButtonsColumn(Contact, buttons=("edit", "delete"))

    class Meta(BaseTable.Meta):
        model = Contact
        fields = (
            "pk",
            "name",
            "title",
            "phone",
            "email",
            "address",
            "comments",
            "assignment_count",
            "tags",
        )
        default_columns = (
            "pk",
            "name",
            "assignment_count",
            "title",
            "phone",
            "email",
            "actions",
        )


class ContactAssignmentTable(BaseTable):
    content_type = ContentTypeColumn(verbose_name="Object Type")
    object = tables.Column(linkify=True, orderable=False)
    contact = tables.Column(linkify=True)
    role = tables.Column(linkify=True)
    actions = ButtonsColumn(model=ContactAssignment, buttons=("edit", "delete"))

    class Meta(BaseTable.Meta):
        model = ContactAssignment
        fields = ("content_type", "object", "contact", "role", "actions")
        default_columns = ("content_type", "object", "contact", "role", "actions")


class EmailTable(BaseTable):
    pk = SelectColumn()
    name = tables.Column(linkify=True)
    jinja2_trim = BooleanColumn(verbose_name="Trim")
    jinja2_lstrip = BooleanColumn(verbose_name="Lstrip")
    tags = TagColumn(url_name="devices:configuration_list")
    actions = ButtonsColumn(Email)

    class Meta(BaseTable.Meta):
        model = Email
        fields = (
            "pk",
            "name",
            "subject",
            "jinja2_trim",
            "jinja2_lstrip",
            "updated",
            "tags",
            "actions",
        )
        default_columns = ("pk", "name", "updated", "actions")
