from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI


class GPT4o:
    client = OpenAI()
    messages = [
        {
            "role": "system",
            "content": "You're a pharmacist who's there to help sick patients and recommend medications.",
        },
    ]

    def reset(self):
        self.messages = [
            {
                "role": "system",
                "content": "You're a pharmacist who's there to help sick patients and recommend medications.",
            },
        ]
        completion = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": "Write the symptoms you are experiencing",
                },
            ],
        )


class Diagnosis(APIView):

    def post(self, request):
        prompt = request.data.get("prompt")
        if not prompt:
            return Response(
                {"error": "No prompt provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        }
        data = {
            "model": "gpt-4-0613",
            "prompt": prompt,
            "max_tokens": 100,
        }

        response = requests.post(
            "https://api.openai.com/v1/completions", headers=headers, json=data
        )
        if response.status_code != 200:
            return Response(
                {"error": "Failed to get response from GPT API"},
                status=response.status_code,
            )

        return Response(response.json(), status=status.HTTP_200_OK)
