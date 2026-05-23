import os

os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)
os.environ.pop("ALL_PROXY", None)

from dotenv import load_dotenv
from gigachat import GigaChat


load_dotenv()


def request_gigachat(prompt: str) -> str:

    credentials = os.getenv(
        'GIGACHAT_CREDENTIALS'
    )

    if not credentials:

        raise ValueError(
            'GIGACHAT_CREDENTIALS not found'
        )

    with GigaChat(
        credentials=credentials,
        verify_ssl_certs=False
    ) as giga:

        response = giga.chat(prompt)

        return response.choices[0].message.content