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
