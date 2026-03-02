# ninth
import requests
from django.conf import settings


def check_virustotal(file_hash):
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"

    headers = {
        "x-apikey": settings.VIRUSTOTAL_API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"vt_available": False}

    data = response.json()

    stats = data["data"]["attributes"]["last_analysis_stats"]

    malicious = stats.get("malicious", 0)

    return {
        "vt_available": True,
        "malicious_votes": malicious
    }