# -*- coding: utf-8 -*-

"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # lowercase text and split into list
    language_text = text.lower().split()
    # varible to hold common words
    common_words = []
    
    # Other variables to track language and common words count
    language = ""
    count = 0
    max_common_words_count = 0
    
    # Loop through each language
    # get the common words between the language and txt
    # return language with the highest common words
    for i in languages:
        common_words = set(i['common_words']) & set(language_text)
        count = len(common_words)
        if count > max_common_words_count:
            max_common_words_count = count;
            language = i['name']
    return language

        
        



    
    

