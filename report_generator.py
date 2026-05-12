import pandas as pd
from groq import Groq

# Read CSV
df = pd.read_csv("output/submission.csv")

# Summary statistics
summary = df.describe().to_string()

# Top products
top_products = (
    df.sort_values(by="Predicted FY26 Q2", ascending=False)
    .head(5)
    .to_string(index=False)
)

# AI Prompt
prompt = f"""
You are a Cisco sales analyst.

Analyze this forecast data and provide:

1. Key insights
2. Product trends
3. Business recommendations

Summary:
{summary}

Top Products:
{top_products}
"""

# Groq API
client = Groq(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

ai_report = response.choices[0].message.content

print(ai_report)

# Save report
with open("ai_report.txt", "w", encoding="utf-8") as f:
    f.write(ai_report)