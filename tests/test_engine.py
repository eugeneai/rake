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
       "линейных диофантовых уравнений, строгих неравенств и "\
       "нестрогих неравенств. "\
       "Получены верхние пределы компонент минимального "\
       "множества решений и алгоритмы построения "\
       "минимальных образующих множеств решений для "\
       "всех типов систем. Эти критерии и соответствующие "\
       "алгоритмы построения минимального несущего множества "\
       "решений могут использоваться в "\
       "решении всех рассмотренных типов систем "\
       "и систем смешанного типа."
       }

#
# Manual keywords
#
# linear constraints, set of natural numbers, linear Diophantine equations,
# strict inequations, nonstrict inequations, upper bounds, minimal generating sets
#
# "en" stop words:
#
# ('minimal generating sets', 8.666666666666666),
# ('linear diophantine equations', 8.5),
# ('minimal supporting set', 7.666666666666666),
# ('minimal set', 4.666666666666666),
# ('linear constraints', 4.5),
# ('upper bounds', 4.0),
# ('nonstrict inequations', 4.0),
# ('strict inequations', 4.0),
# ('mixed types', 3.666666666666667),
# ('corresponding algorithms', 3.5),
# ('considered types', 3.166666666666667),
# ......
#
# TODO:
#
# Extending stop-word list https://cyberleninka.ru/article/n/predstavlenie-dokumentov-v-zadache-klasterizatsii-annotatsiy-nauchnyh-tekstov
#


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
