from unittest import TestCase, expectedFailure
from main import YandexDisk


token_yandex = ''
yandex_session = YandexDisk(token_yandex)
path = 'test_folder'

class TestYandex(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.status_code_create = yandex_session.create_folder(path)

    def test1_correct_response_code(self) -> None:
        self.assertEqual(self.status_code_create, 201)

    def test2_metainfo_exists(self) -> None:
        metainfo = yandex_session.file_folder_metainfo(path)
        status_code_meta = metainfo.status_code
        self.assertEqual(status_code_meta, 200)

    def test3_correct_meta_type(self) -> None:
        metainfo = yandex_session.file_folder_metainfo(path).json()
        self.assertEqual(metainfo['type'], 'dir')

    @expectedFailure
    def test4_folder_created_multiple_times(self) -> None:
        status_code_mult = yandex_session.create_folder(path)
        self.assertEqual(status_code_mult, 201)

    @classmethod
    def tearDownClass(self) -> None:
        yandex_session.delete_file_folder(path)


import pytest

class TestPyYandex(TestCase):
    @classmethod
    def setUpClass(self) -> None:
        self.status_code_create = yandex_session.create_folder(path)

    def test1_correct_response_code(self) -> None:
        assert self.status_code_create == 201

    def test2_metainfo_exists(self) -> None:
        metainfo = yandex_session.file_folder_metainfo(path)
        status_code_meta = metainfo.status_code
        assert status_code_meta == 200

    def test3_correct_meta_type(self) -> None:
        metainfo = yandex_session.file_folder_metainfo(path).json()
        assert metainfo['type'] == 'dir'

    @expectedFailure
    def test4_folder_created_multiple_times(self) -> None:
        status_code_mult = yandex_session.create_folder(path)
        assert status_code_mult == 201

    @classmethod
    def tearDownClass(self) -> None:
        yandex_session.delete_file_folder(path)