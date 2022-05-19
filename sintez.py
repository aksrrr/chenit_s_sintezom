import requests
import re

token = "t1.9euelZqVlZrHnsqWkJbHnpuPlZmJle3rnpWanI7IxpvNzJ6NnZyXlMeZyJPl8_ctS2Vr-e8YSAVX_t3z9215Ymv57xhIBVf-.Jp51VCS1-VAzDdSagc3livxjSwf7SQs1LA_MiugWOwpdVLNCY9Dq8pPbM0B2u3VCwUlERYnqy4xBHUdRnksqCQ"
folder_id = "b1gap88d08l35fj9vh1u"
text = input("Введите текст для синтеза")
text1 = re.sub(r'^\s+|\n|\r|\s+$', '', text)
output = "audio_13.ogg"


def synthesize(folder_id, iam_token, text1):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + iam_token,
    }

    data = {
        'text': text1,
        'lang': 'ru-RU',
        'voice': 'jane',
        'folderId': folder_id,
        'speed': '1.0',
         'emotion': 'good',
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk

with open(output, "wb") as f:
    for audio_content in synthesize(folder_id, token, text1):
        f.write(audio_content)
