import unittest
from timeit import timeit

from strings import search_text_sentences
from utils import algorithms


class Strings(unittest.TestCase):
    def test_search_text_with_keyword(self):
        for algo in algorithms(search_text_sentences):
            text = "Hello Moto."
            self.assertEqual(["Hello Moto."], algo(text, "hello"))

            text = "Hella Moto."
            self.assertEqual([], algo(text, "Hello"))

            text = """Early sales of Apple's new iPhones have lived up to high expectations.

                The strong sales mirror growing consumer demand for smartphones with bigger
                screens. IDC, a research firm, estimated that at least 20 percent of all
                smartphones shipped last year in China, the largest smartphone market in
                the world, were five inches or larger. It also predicted that manufacturers
                this year would ship more "phablets," or smartphones with screens measuring
                at least 5-point-5 diagonal inches, than laptops.

                The company on Monday said it sold more than 10 million of the iPhone 6 and
                6 Plus models in the first three days they were available in stores. That
                is higher than the nine million new iPhones it sold last year in their
                first weekend on sale. But some analysts, like Gene Munster of Piper
                Jaffray, wondered whether first-weekend sales were still a reliable measure
                for consumer demand.

                The iPhone sales were on the upper end of financial analysts' expectations,
                which ranged from 6 million to the "low teens" of millions of sales. 
            """

            self.assertEqual(4, len(algo(text, "iphone")))


            self.assertEqual(['It also predicted that manufacturers this year would ship more "phablets,"'
                              ' or smartphones with screens measuring at least 5-point-5 diagonal inches, '
                              'than laptops.'], algo(text, "pHaBlEts"))


if __name__ == '__main__':
    unittest.main()
