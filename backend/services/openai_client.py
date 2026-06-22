import os

import requests


API_KEY = os.getenv(
    "OPENAI_API_KEY",
    ""
)

MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-5.5"
)


def request_openai(prompt):

    if not API_KEY:
        raise ValueError("OPENAI_API_KEY is not set")

    response = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": MODEL,
            "input": prompt
        },
        timeout=60
    )

    if response.status_code == 401:
        raise ValueError(
            "OpenAI API key is invalid"
        )

    if response.status_code == 429:
        error = response.json().get(
            "error",
            {}
        )

        if error.get("code") == "insufficient_quota":
            raise ValueError(
                "OpenAI API quota is unavailable. Check billing settings."
            )

    response.raise_for_status()

    data = response.json()

    for item in data.get("output", []):
        if item.get("type") != "message":
            continue

        for content in item.get("content", []):
            if content.get("type") == "output_text":
                return content.get("text", "")

    raise ValueError("OpenAI returned an empty response")
