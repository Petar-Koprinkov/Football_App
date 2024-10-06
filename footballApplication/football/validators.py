from typing import List

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadLanguageValidator:
    def __init__(self, words: List, message=None):
        self.words = words
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if not value:
            self.__message = 'You entered a bad language'
        else:
            self.__message = value

    def __call__(self, value):
        for word in self.words:
            if word.lower() in value.lower():
                raise ValidationError(self.message)


