from openai import OpenAI


class Summarizer:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def summarize(self, content):
        completion = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Sumiraj sledeci tekst u 2-3 recenice: {content}"
                }
            ]
        )
        return completion.choices[0].message.content.strip()
