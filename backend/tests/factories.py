from factory import Factory, fuzzy

from backend.schemas.dummy_test import DummyTest


class DummyTestFactory(Factory):  # type: ignore[misc]
    class Meta:
        model = DummyTest

    attribute = fuzzy.FuzzyText(length=20)


class FilmeFactory(Factory):  # type: ignore[misc]
    class Meta:
        model = FilmeTest

    title = fuzzy.FuzzyText(length=20)
    director = fuzzy.FuzzyText(length=20)
