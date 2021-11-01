import pytest
from HW_func import people, shelf, add, add_shelf, move, delete_doc

class TestHwFunc:
    # Проверка поиска человека по номеру документа
    def test_people_positive(self):
        assert people('11-2') == 'Геннадий Покемонов'
    def test_people_negative(self):
        assert people('11-3') == None

    # Проверка поиска полки по номеру документа
    def test_shelf_positive(self):
        assert shelf('11-2') == '1'
    def test_shelf_negative(self):
        assert shelf('11-3') == 'Такого документа не существует!'

    # Проверка добавление нового документа
    def test_add_positive(self):
        assert add('1', 'passport', '2507 929520', 'Медведев Дмитрий') == 'Медведев Дмитрий добавлен'

    # Проверка наличия добавленного документа
    def test_people_positive_add(self):
        assert people('2507 929520') == 'Медведев Дмитрий'

    # Проверка добавление документа на не существующую полку
    def test_add_negative(self):
        assert add('4', 'passport', '2502 929521', 'Медведев Сергей') == 'Такой полки не существует!'

    # Проверка отсутствия документа после попытки добавления на не существующую полку
    def test_people_negative_add(self):
        assert people('2502 929521') == None

    # Проверка переноса документа с существующей полки на целевую.
    def test_move_positive(self):
        assert move('10006', '1')
    def test_shelf_positive_move(self):
        assert shelf('10006') == '1'

    # Проверка на удаление документа
    def test_delete_doc(self):
        assert delete_doc('11-2') == 'Документ удален'

    # Проверка удалился ли документ с директории и полки
    def test_people_positive_del(self):
        assert people('11-2') == None
    def test_shelf_negative_del(self):
        assert shelf('11-2') == 'Такого документа не существует!'

    # Проверка создания новой полки
    def test_add_shelf_negative(self):
        assert add_shelf('1') == 'Такая полка уже существует'

    def test_add_shelf_positive(self):
        assert add_shelf('4') == 'Полка номер 4 добавлена'

    #  Проверка перемещения документа на новую полку.
    def test_move_positive_new_shelf(self):
        assert move('10006', '4')
    def test_shelf_positive_move_on_new_shelf(self):
        assert shelf('10006') == f'4'