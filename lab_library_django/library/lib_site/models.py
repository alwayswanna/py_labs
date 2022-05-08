from django.db import models


class Module(models.Model):
    editor = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    name = models.CharField(max_length=150)

    books = models.ManyToManyField('Book', blank=True, related_name='books')

    def __str__(self):
        return "Id: {%s}, {%s}" % (self.editor, self.name)


class Book(models.Model):
    name = models.CharField(max_length=150)

    author = models.CharField(max_length=100)

    description = models.TextField()

    module_fk = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return "name: {%s}, author: {%s}, description: {%s}" % (self.name, self.author, self.description)

# end
# Created: https://github.com/alwayswanna
