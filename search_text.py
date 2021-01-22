def search_and_replace_text(search_sentence, text):
    
    
    if ''.join(search_sentence) not in text:
        return "N/A"
    
    search_sentence = "".join(search_sentence)
    text = text.replace(search_sentence, '')
    text += search_sentence
    
    return text
