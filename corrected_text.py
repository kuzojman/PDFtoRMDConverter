import requests

class corrected_text:

    def corect_text(text):
        url = "https://speller.yandex.net/services/spellservice.json/checkText"
        params = {"text": text}
        text = text
        response = requests.get(url, params=params)
        if response.status_code == 200:
            errors = response.json()
            corrected_text = text

            # Заменяем ошибки на первый предложенный вариант
            for error in errors:
                wrong_word = error["word"]  # Слово с ошибкой
                suggestion = error["s"][0]  # Первый предложенный вариант
                corrected_text = corrected_text.replace(wrong_word, suggestion)
            
            return corrected_text
        else:
            raise Exception(f"Ошибка подключения к API: {response.status_code}")