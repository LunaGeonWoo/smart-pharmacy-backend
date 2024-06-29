from openai import OpenAI
from collections.abc import Iterable
from django.conf import settings


class GPT4o:
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    model = "gpt-4o"

    def make_gpt_query(self, prompt, result):
        return (
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "assistant",
                "content": result,
            },
        )

    def converse(self, prompt, queries=[]):
        role = "You're a pharmacist who's there to help sick patients and recommend medications."
        messages = [
            {
                "role": "system",
                "content": role,
            },
        ]
        messages.extend(queries)
        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )
        return self.client.chat.completions.create(
            messages=messages,
            model=self.model,
        )

    def make_title_base_first_query(self, query) -> str:
        role = "You are an assistant who creates titles for conversations based on your conversations with users, in the form of nouns of 50 characters or less."
        messages = [
            {
                "role": "system",
                "content": role,
            },
        ]
        messages.extend(query)
        return self.client.chat.completions.create(
            messages=messages,
            model=self.model,
        )
