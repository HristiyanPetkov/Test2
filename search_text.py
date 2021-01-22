def search_and_replace_text(search_sentence, text):
    
    
    if ''.join(search_sentence) not in text:
        return "N/A"
    elif len(search_sentence) < 2:
        return "N/A"
    
    text = text.split(' ')
    search_sentence = "".join(search_sentence)
    text.append(search_sentence)
    text = ' '.join(text)
    text = text.split(search_sentence)
    text.append(search_sentence)
    
    return "".join(text)
