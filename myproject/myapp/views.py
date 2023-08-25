from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
from .serializers import PredictionSerializer

class PredictPrice(APIView):

    def post(self, request):
        serializer = PredictionSerializer(data=request.data)

        if serializer.is_valid():
            # Load Random Forest model
            model = joblib.load('/Users/goli/Documents/random_forest_modelCars.joblib')

            # Prepare input data
            data = [serializer.validated_data['departement'], serializer.validated_data['annee'], 
                    serializer.validated_data['kilometrage'], serializer.validated_data['Gear'],
                    serializer.validated_data['Energy'], serializer.validated_data['Brand'], 
                    serializer.validated_data['Model']]

            # Make prediction
            prediction = model.predict([data])

            # Add the prediction to the validated data
            serializer.validated_data['predicted_price'] = prediction[0]

            return Response(serializer.validated_data)

        return Response(serializer.errors, status=400)
