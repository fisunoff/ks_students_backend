import django_tables2 as tables
from interaction.models import Interaction


class InteractionTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'interaction-detail\' record.id %}">🛈</a>', orderable=False,
                                 verbose_name="")
    status = tables.Column(order_by="status__status_name")

    class Meta:
        model = Interaction
        template_name = "django_tables2/bootstrap.html"
        fields = ('edit', 'interaction_name', 'mentor', 'student', 'start_date', 'end_date', 'status', )
