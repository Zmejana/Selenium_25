import time
import pytest
import math
from selenium.webdriver.common.by import By

# Проверка что успешно зашли на страницу
def test_auth_ok(autorized):
    time.sleep(2)
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
# Проверка количества питомцев в счетчике и строк в таблице
def test_count_mypets(autorized):
    time.sleep(2)
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    time.sleep(2)
    count_pet = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1])
    count_row = len(pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr"))
    assert count_pet == count_row

# Проверка что у всех питомцев заполнено имя, порода и возраст
def test_get_name(autorized):
    time.sleep(2)
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
    names = pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr/td[1]")
    breed = pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr/td[2]")
    age = pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr/td[3]")
    #    print(name)
    # print(names[0].text)
    # print(len(age))
    assert len(names) == len(breed) and len(names) == len(age)

# Проверка на разные имена
def test_diff_names(autorized):
    time.sleep(2)
    count_pet = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1])
    names = pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr/td[1]")
    array = []
    for n in range(0, (count_pet)):
        array.append(names[n].text)

    counter = {}
    for elem in array:
        counter[elem] = counter.get(elem, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    assert len(doubles) == 0

# Проверка на количество фото питомцев
def test_photo(autorized):
    time.sleep(2)
    photos = pytest.driver.find_elements(By.XPATH, "//*[@class= 'table table-hover']/tbody/tr/th/img")
    m = 0
    for i in photos:
        if i.get_attribute('src') !="":
            m+=1
    count_pet = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1])
    l = math.ceil(count_pet/2)
    assert m >= l



