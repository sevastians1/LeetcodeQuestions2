def make_latin(word, make_pig_latin):
  vowel_object=['a', 'e', 'i', 'o', 'u']
  if make_pig_latin: ##is true means temp_word[0] is vowel
    # print(word)
    word.append("ay")
    return word
  else:##if false
    new_word=[]
    temp_list=[]
    append_if_true=False
    for letter in word:
      # print(append_if_true, letter)
      if (letter in vowel_object):
        append_if_true=True
      if append_if_true:
        new_word.append(letter)
      else:
        temp_list.append(letter)
    # print(temp_list, new_word)
    for x in temp_list:
        new_word.append(x)
    new_word.append("ay")
    return new_word


def translate(word_or_phrase):
  answer=[]
  vowel_object=['a', 'e', 'i', 'o', 'u']
  list_of_words=word_or_phrase.split("\n")
  split_list_of_words=[]
  for x in list_of_words:
    x=x.split(" ")
    split_list_of_words.append(x)
  list_of_words=[]
  for x in split_list_of_words:
    for y in x:
      list_of_words.append(y)
  #split based on spaces and \n
  # print(list_of_words)
  for word in list_of_words:
    temp_word=[]
    list_of_punctuation=[]
    remove_first=0
    remove_last=0
    capital=False
    for count, letter in enumerate(word):
      # print(letter, count)
      if letter.isalnum():
        if letter ==letter.lower():
          temp_word.append(letter)
        else:
          capital=True
          temp_word.append(letter.lower())
          list_of_punctuation.append([count, letter])
      else:
        if count==0:
            remove_first=letter
            # print("remove first")
            list_of_punctuation.append([count, letter])
        elif count==len(word)-1:
            remove_last=letter
            # print("remove last")
            list_of_punctuation.append([count, letter])
          ##later if alphanumeric we perform the replace function
        else:
            temp_word.append(letter.lower())
    make_pig_latin=False
    # print(temp_word)
    quick_word=[]
    for count, x in enumerate(temp_word):
      if x=='q' and temp_word[count+1]=="u":
        quick_word.append("qu")
        del temp_word[count+1]
      else:
        quick_word.append(x)
    # print(quick_word)
    if (quick_word[0] in vowel_object):
      make_pig_latin=True
    new_word=make_latin(quick_word, make_pig_latin)
    # print(new_word, "spacer", list_of_punctuation, make_pig_latin, temp_word, remove_last)
    # ## returns modified word
    final_word=[]
    if remove_first:
        final_word.append(remove_first)
    for x in new_word:
      if x.isalnum():
        if capital:
          final_word.append(x.upper())
          capital=False
        else:
          final_word.append(x)
      else:
        final_word.append(x)
    if remove_last:
      final_word.append(remove_last)
    final_word="".join(final_word)
    # print(final_word)
    answer.append(final_word)
  # print(answer)
  print(" ".join(answer))
  return " ".join(answer)
    #   final_word.append(remove_first)
    # for x in new_word:
    #   new_word.append(x)
    # if remove_last:
    #   final_word.append(remove_last)
    # # print(final_word)
    # # answer.append(final_word)
    


  


translate('the quick brown fox')
