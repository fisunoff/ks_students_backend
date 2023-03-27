import django_tables2 as tables
from mentor.models import Profile


class MentorTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'mentor-detail\' record.id %}">&#128269;</a>', orderable=False,
                                 verbose_name="")

    class Meta:
        model = Profile
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'surname', 'name', 'patronymic', 'mentor', 'position')
