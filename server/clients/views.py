import csv
from rest_framework import viewsets
from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response

from .serializers import DealSerializer, CsvSerializer
from .models import Deal, Csv
from .forms import CsvModelForm


class DealsViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.values('customer').annotate(spent_money=Sum('total')).order_by('-spent_money')[:5]
    serializer_class = DealSerializer

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return CsvSerializer

    def list(self, request, *args, **kwargs):
        """ Displays top 5 clients """
        serializer = self.serializer_class(self.queryset, many=True)

        all_gems = []
        for client in serializer.data:
            all_gems += (client['gems'])

        for i, client in enumerate(serializer.data):
            gems = []
            for gem in client['gems']:
                if all_gems.count(gem) > 1:
                    gems.append(gem)
            serializer.data[i]['gems'] = gems

        return Response({
            'response': serializer.data
        })

    def create(self, request, *args, **kwargs):
        """ Creates models derived from a .csv file """
        form = CsvModelForm(request.POST or None, request.FILES or None)

        if not form.is_valid():
            return Response(
                data=form.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            form.save()
            obj = Csv.objects.get(activated=False)
            obj.activated = True
            obj.save()
            with open(obj.file.path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if i == 0:
                        pass
                    else:
                        Deal.objects.create(
                            customer=row[0],
                            item=row[1],
                            total=row[2],
                            quantity=row[3],
                            date=row[4]
                        )
        return Response(data='File upload', status=status.HTTP_201_CREATED)
