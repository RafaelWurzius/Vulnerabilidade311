O arquivo codigovulneravel.py exemplifica uma inserção e busca de dados de login e senha de usuários. Porém esses dados são transmitidos e gravados em texto limpo.

O arquivo codigoSeguro.py realiza a criptografia antes de inserir a senha no banco de dados. Foi utilizado a função de hash SHA-256, para criar uma representação criptografada da senha. 

O hash gerado por algoritmos de hash, como SHA-256, não é reversível. Portanto, não é possível descriptografar uma senha hash para recuperar a senha original. 
O que geralmente é feito, é comparar o hash da senha fornecida pelo usuário durante o login com o hash armazenado no banco de dados para ver se são iguais.
