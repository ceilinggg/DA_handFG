import unittest
import scrapytest as prog

class TestMyProgram(unittest.TestCase) :

    def test_scrapy (self) :
        vios = prog.NewSpider()

if __name__ == '__main__':
    unittest.main()