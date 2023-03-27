import django_tables2 as tables
from ks_students.models import Student


class StudentTable(tables.Table):
    edit = tables.TemplateColumn('<a href="{% url \'student-detail\' record.id %}">&#128269;</a>', orderable=False,
                                 verbose_name="")

    class Meta:
        model = Student
        template_name = "django_tables2/bootstrap.html"
        fields = ("edit", 'surname', 'name', 'patronymic', 'mentor', )
