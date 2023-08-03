# pip install spellchecker    , PY module
# import spellchecker
# Rather above, use -   pip install pyspellchecker ,  pip install indexer

from spellchecker import SpellChecker

# spl = spellchecker.SpellChecker()
spl = SpellChecker()
word = input("Enter the word which you think is misspelled : ")
crct_word = spl.correction(word)
print("Corrected word : ", crct_word)