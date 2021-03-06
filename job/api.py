from .models import Job
from .serializers import JobSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

@api_view(['GET'])
def jobs_api(request):
    jobs = Job.objects.all()
    data = JobSerializer(jobs, many=True).data

    return Response({'data':data})


@api_view(['GET'])
def job_detail_api(request, id):
    job = Job.objects.get(id=id)
    data = JobSerializer(job).data

    return Response({'data':data})


class JobListApi(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'



