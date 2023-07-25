from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Time

# Create your views here.
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Time.objects.all()
# Create your views here.
