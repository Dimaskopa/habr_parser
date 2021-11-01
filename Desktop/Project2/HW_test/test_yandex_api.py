from yandex_api import create_path, check_connect, check_path

class TestYandexApi:

# Проверка соединения с ресурсом
    def test_check_connect(self):
        assert check_connect() == 200

# Проверка создания новой папки (если ее нет)
    def test_create_path_new(self):
        assert create_path('sample3') == 201

#  Проверка наличия папки на диске
    def test_check_path(self):
        assert check_path('sample2') == 200



