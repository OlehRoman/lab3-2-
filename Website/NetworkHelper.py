import requests

class NetworkHelper:
    BASE_URL = "http://localhost:8000/api/"  # Замість 'example.com' вкажіть URL сервера колеги

    @staticmethod
    def get_list(resource):
        """Отримати список елементів для вказаного ресурсу."""
        response = requests.get(f"{NetworkHelper.BASE_URL}{resource}/all")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_item(resource, item_id):
        """Отримати елемент за його ID."""
        response = requests.get(f"{NetworkHelper.BASE_URL}{resource}/{item_id}")
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_item(resource, item_id):
        """Видалити елемент за його ID."""
        response = requests.delete(f"{NetworkHelper.BASE_URL}{resource}/delete/{item_id}")
        response.raise_for_status()
        return response.status_code == 204  # Перевірка, чи запит завершився успішно
