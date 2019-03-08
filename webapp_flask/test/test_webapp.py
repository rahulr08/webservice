import unittest
import sys
sys.path.insert(0, '/home/ubuntu/webapp_flask/webapp')
from webapp import *
 
class TestAnagram(unittest.TestCase):
    def is_anagram(self,a_word, b_word):
      print sorted(a_word)
      print sorted(b_word)
      return sorted(a_word) == sorted(b_word)
 
    def test_anagram(self):
        anagrams_list = (word_list_anagram("word"))
        for i in anagrams_list:
          self.assertTrue(  self.is_anagram("word", i) )

if __name__ == '__main__':
  unittest.main()     
