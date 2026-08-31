import requests

jelcrap = "https://jellyfin.crapcraft.nz"

response = requests.get(jelcrap, timeout=30)

print("Status:", response.status_code)