from rest_framework import serializers

from .models import Deal, Csv


class DealSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='customer')
    spent_money = serializers.IntegerField()
    gems = serializers.SerializerMethodField()

    class Meta:
        model = Deal
        fields = ('username', 'spent_money', 'gems')

    def get_gems(self, obj):
        """ Returns all gems for the client. """
        queryset = Deal.objects.values('item').filter(customer=obj['customer'])
        gems = []
        for gem in queryset:
            gems.append(gem['item'])
        return set(gems)


class CsvSerializer(serializers.ModelSerializer):

    class Meta:
        model = Csv
        fields = ("file",)
