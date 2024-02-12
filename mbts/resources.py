from import_export import resources
from core.models import Students

class StudentsResource(resources.ModelResource):

    class Meta:
        model = Students