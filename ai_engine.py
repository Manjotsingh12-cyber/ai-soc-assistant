import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_alert(data):
    alert_text = str(data)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a SOC security analyst."},
            {"role": "user", "content": f"Analyze this security alert:\n{alert_text}"}
        ]
    )

    return {
        "summary": response.choices[0].message.content
    }
    }
