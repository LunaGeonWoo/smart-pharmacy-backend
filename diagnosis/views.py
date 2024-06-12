from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import NotFound
from openai import OpenAI
from .serializers import DiagnosisHistorySerializer
from .models import Diagnosis


class Diagnose(APIView):

    client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def chat_with_chatgpt(self, prompt, model="gpt-4o"):
        return self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You're a pharmacist who's there to help sick patients and recommend medications.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            model=model,
        )

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response(
                {"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        res = self.chat_with_chatgpt(prompt)
        result = res.choices[0].message.content
        Diagnosis.objects.create(
            prompt=prompt,
            result=result,
            user=request.user,
        )
        return Response({"result": result})


class DiagnoseHistory(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
            diagnosis_history = Diagnosis.objects.filter(user=request.user)[start:end]
            serializer = DiagnosisHistorySerializer(
                diagnosis_history,
                many=True,
            )
        except Exception as e:
            print(e)
            return redirect(f"{request.path}?page=1")
        return Response(serializer.data)
