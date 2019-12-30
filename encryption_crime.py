ch_z = ord('z')
ch_a = ord('a')


def encrypt(word):
  word = word.lower()
  arr = [0] * len(word)
  len_of_alph = ch_z - ch_a + 1
  
  for i, ch in enumerate(word):
    if ord(ch) < 97 or ord(ch) > 122:
      return 'Incorrect string'
    arr[i] = ord(ch)
  
  for i in range(len(arr)):
    if i  == 0:
      arr[i] = arr[i] + 1
    else:
      arr[i] = arr[i] + arr[i - 1] 
  
  for i in range(len(arr)):
    if arr[i] < ch_a or arr[i] > 122:
      arr[i] = ch_a + ((arr[i] - ch_a) % len_of_alph)
  
  return ''.join([chr(a) for a in arr])
  

def decrypt(word):
  if not word:
    return ''
  new_word = ''
  len_of_alph = 26

  prev = 1  
  for i in range(len(word)):
    new_letter = ord(word[i]) - prev
    while new_letter < ch_a:
      new_letter += len_of_alph
    prev += new_letter
    new_word += chr(new_letter)
  return new_word
    
  
assert(decrypt(encrypt('crime')) == 'crime')
assert(encrypt('crime') != 'crime')
