from YaFolder import YaFolder
import pytest


with open('ya_token.txt', encoding='utf-8') as file:
    ya_token = file.readline().strip()
token_ = ya_token
fixture = [
    (token_, 'new_test', 201),
    (token_, 'new_test', 409),
    (token_ + 'd', 'new_test', 401)
]


@pytest.mark.parametrize('token, folder_name, result', fixture)
def test_ya_create_folder(token, folder_name, result):
    person = YaFolder(token)
    res = person.create_folder(folder_name)
    assert res == result
    if res == 409:
        person.delete_folder(folder_name)


if __name__ == '__main__':
    test_ya_create_folder()

