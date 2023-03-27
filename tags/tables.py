import django_tables2 as tables
from tags.models import Tag


class TagsTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'tag-detail\' record.id %}">&#128269;</a>', orderable=False,
                                 verbose_name="")
    get_count = tables.TemplateColumn("{{ record.get_count }}", verbose_name="Количество записей" , orderable=False)

    class Meta:
        model = Tag
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'tag_name', 'get_count')
