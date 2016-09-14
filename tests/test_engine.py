from nose.tools import raises
from rake import Rake
from pkg_resources import resource_filename

TEXTS = {
    "en": \
       "Compatibility of systems of linear constraints "\
       "over the set of natural numbers. "\
       "Criteria of compatibility of a system of "\
       "linear Diophantine equations, strict inequations, "\
       "and nonstrict inequations are considered. "\
       "Upper bounds for components of a minimal set "\
       "of solutions and algorithms of construction "\
       "of minimal generating sets of solutions for "\
       "all types of systems are given. These criteria "\
       "and the corresponding algorithms for constructing "\
       "a minimal supporting set of solutions can be used "\
       "in solving all the considered types of systems "\
       "and systems of mixed types.",
    "ru":
       "Совместимость системы линейных ограничений "\
       "над множеством натуральных чисел. "\
       "Рассмотрены критерии совместимости системы "\
       "линейных диофантовых уравнений. "\
       "Получены верхние пределы компонент минимального "\
       "множества решений и алгоритмы построения "\
       "минимальных образующих множеств решений для "\
       "всех типов систем. Эти критерии и соответствующие "\
       "алгоритмы построения минимального несущего множества "\
       "решений могут использоваться в "\
       "решении всех рассмотренных типов систем "\
       "и систем смешанного типа."
       }


class TestBasic:
    @raises(ValueError)
    def test(self):
        Rake()


class TestEngineEnglishFromStopWordLibrary:
    def setUp(self):
        self.lang = "en"
        self.rake = Rake(lang=self.lang)

    def tearDown(self):
        pass

    def test_run(self):
        keywords = self.rake.run(TEXTS[self.lang])
        print(keywords)


class TestEngineRussianFromStopWordLibrary:
    def setUp(self):
        self.lang = "ru"
        self.rake = Rake(lang=self.lang)

    def tearDown(self):
        pass

    def test_run(self):
        keywords = self.rake.run(TEXTS[self.lang])
        print(keywords)


class TestEngineEnglishFromFile:
    def setUp(self):
        stop_word_file_path = resource_filename(
            "rake", "../tests/data/FoxStoplist.txt")
        print(stop_word_file_path)
        self.rake = Rake(stop_word_file_path)

    def tearDown(self):
        pass

    def test_run(self):
        keywords = self.rake.run(TEXTS["en"])
        print(keywords)
