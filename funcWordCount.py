def words(phrase):
  ret = {}
  for word in phrase.split():
      try:
        int(word)
        word = int(word)
      except Exception as e:
        pass
    
      if ret.get(word):
      
        ret[word] += 1
      else:
        ret[word] = 1
  
  return ret