from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import exceptions, status
from .gpt_api import GPT4o
from .serializers import DiagnosisHistorySerializer, DiagnosisDetailSerializer
from .models import Diagnose, Query


class Diagnosis(APIView):
    permission_classes = [IsAuthenticated]
    gpt4o = GPT4o()

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response(
                {"prompt": ["이 필드는 필수 항목입니다."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        response = self.gpt4o.converse(prompt)
        result = response.choices[0].message.content
        diagnose = Diagnose.objects.create(user=request.user)
        Query.objects.create(
            prompt=prompt,
            result=result,
            diagnose=diagnose,
        )
        gpt_query = self.gpt4o.make_gpt_query(prompt, result)
        response = self.gpt4o.make_title_base_first_query(gpt_query)
        title = response.choices[0].message.content
        diagnose.title = title
        diagnose.save()
        return redirect("diagnosis:diagnose_detail", diagnose.id)


class DiagnoseDetail(APIView):
    permission_classes = [IsAuthenticated]
    gpt4o = GPT4o()

    def get_object(self, pk):
        try:
            return Diagnose.objects.get(pk=pk)
        except Diagnose.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        diagnose = self.get_object(pk)
        if diagnose.user != request.user:
            raise exceptions.PermissionDenied
        serializer = DiagnosisDetailSerializer(diagnose)
        return Response(serializer.data)

    def post(self, request, pk):
        diagnose = self.get_object(pk)
        if diagnose.user != request.user:
            raise exceptions.PermissionDenied
        prompt = request.data.get("prompt")
        if not prompt:
            return Response(
                {"prompt": ["이 필드는 필수 항목입니다."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        queries = Query.objects.filter(diagnose=diagnose)
        messages = []
        for query in queries:
            gpt_query = self.gpt4o.make_gpt_query(
                query.prompt,
                query.result,
            )
            messages.extend(gpt_query)
        response = self.gpt4o.converse(prompt, queries=messages)
        result = response.choices[0].message.content
        query = Query.objects.create(
            prompt=prompt,
            result=result,
            diagnose=diagnose,
        )
        return Response({"result": query.result})


class DiagnoseHistory(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
            diagnosis_history = Diagnose.objects.filter(user=request.user)[start:end]
            serializer = DiagnosisHistorySerializer(
                diagnosis_history,
                many=True,
            )
        except:
            raise ParseError
        return Response(serializer.data)
