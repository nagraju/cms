from import_export import resources
from mbts.models import Students

class StudentsResource(resources.ModelResource):

    class Meta:
        model = Students
        import_id_fields = ('pin',)
        fields = ["pin", "sname", "fname", "phno","polycetrank"]