from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-6-luna", 
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)