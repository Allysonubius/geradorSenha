import hashlib

arquiveOne = 'a.txt'
arquiveTwo = 'b.txt'

hashOne = hashlib.new('ripemd160')

hashOne.update(open(arquiveOne, 'rb').read())

hashTwo = hashlib.new('ripemd160')

hashTwo.update(open(arquiveTwo, 'rb').read())

if hashOne.digest() != hashTwo.digest():
    print(f'O arquivo : {arquiveOne} é diferente do arquivo : {arquiveTwo}')
    print('O hash do arquivo a.txt : ', hashOne.hexdigest)
    print('O hash do arquivo b.txt : ', hashTwo.hexdigest)
else:
    print(f'O arquivo : {arquiveOne} e igual ao arquivo : {arquiveTwo}')
    print('O hash do arquivo a.txt : ', hashOne.hexdigest)
    print('O hash do arquivo b.txt : ', hashTwo.hexdigest)
    