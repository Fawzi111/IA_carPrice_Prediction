from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    departement = serializers.CharField()
    annee = serializers.IntegerField()
    kilometrage = serializers.IntegerField()
    Gear = serializers.CharField()
    Energy = serializers.CharField()
    Brand = serializers.CharField()
    Model = serializers.CharField()
    predicted_price = serializers.FloatField(required=False)  # Output
