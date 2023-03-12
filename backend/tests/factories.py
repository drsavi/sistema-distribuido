from factory import Factory, fuzzy

from backend.schemas.filme_schema import FilmeTest

class FilmeFactory(Factory):  # type: ignore[misc]
    class Meta:
        model = FilmeTest

    title = fuzzy.FuzzyText(length=20)
    director = fuzzy.FuzzyText(length=20)
