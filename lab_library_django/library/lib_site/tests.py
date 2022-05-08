from django.test import TestCase

from lab_library_django.library.lib_site.models import Module, Book


def setup():
    Module.objects.create(id=1, name='Some module name', editor='root', books=[])
    Book.objects.create(id=1, name="Some book name", author='Some author', description='Some description')


class ModuleTestCase(TestCase):

    def test_str(self):
        module = Module.objects.get(name='Some module name')
        book = Book.objects.get(name='Some book name')
        self.assertEqual(module.__str__(), 'Id: 1, Some module name')
        self.assertEqual(book.__str__(), 'name: Some book name, author: Some author, description: Some description')

# end
# Created: https://github.com/alwayswanna
