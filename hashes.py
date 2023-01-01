import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1,'rb').read())

hash2 = hashlib.new('ripemd160')
hash1.update(open(arquivo2,'rb').read())

if hash1.digest() == hash2.digest():
    print(f'O arquivo {arquivo1} é igual ao {arquivo2}')
    print(f'O hash do arquivo {arquivo1}: {hash1.hexdigest()} e do arquivo {arquivo2}: {hash2.hexdigest()}')
else:
    print('ambos são diferentes')
    print(f'O hash do arquivo {arquivo1}: {hash1.hexdigest()} e do arquivo {arquivo2}: {hash2.hexdigest()}')