Grupo 1 - Escrito por Lucas Anjo e Eduardo Carvalho

---------------------------------Epic-------------------------

Autenticação

Como utilizador, quero criar ou iniciar sessão ou recuperar a password da minha conta para criar, rever e resolver quizzes.

---------------------------------User Story-------------------------

Como utilizador que se esqueceu da password, quero recupera-la e definir uma nova.

Testes

Cenário:O utilizador quer recuperar a password

* Testar com link expirado.   
* Testar pedir novo link de recuperação.        
* Testar o envio para o email do DEI.
* Testar o envio para o email da UC.
* Testar sem a password inserida
* Testar sem a confirmação da password inserida
* Testar sem a password e a confirmação da password inseridas
* Testar com nova password com número de carateres inferior a 8
* Testar com nova password com menos de 1 letra
* Testar com nova password sem pelo menos 1 número
* Testar com nova password sem pelo menos 1 carater especial
* Testar com a password e a confirmação da password diferentes
* Testar com os dados corretos
* Testar sem o email inserido.
* Testar com email sem conta registada.
* Testar com email sem conta confirmada.
* Testar com dados corretos.

Resultado esperado: O sistema é capaz de identificar os erros no email/código/password inseridos e informar o utilizador

-----------------------------Caso de Uso-----------------------------


Caso de Uso 1: Recuperar a password
Ator Primário: Utilizador que se esqueceu da password
Nível: Objetivo do utilizador
Stakeholders e Interesses:
     Utilizador não sabe a password - Quer poder mudar a password.
     sistema - Evita que haja utilizadores inativos, devido à impossibilidade de entrar na sua conta
Pré-condição: Estar registado no sistema.
Garantia Mínima: Há acesso à página inicial do sistema, à de registo e à de login e à de recuperação de password.
Garantia de Sucesso: Passa a ter acesso à página como se tivesse dado login.

Cenário Principal de Sucesso:
1. O utilizador erra a inserir a password
2. O utilizador clica no botão de recuperação de password
3. O Sistema reencaminha o utilizador para a pagina de recuperação da password
4. O utilizador insere o email da conta
5. O sistema envia um link de confirmação para o email do utilizador 
6. O utilizador abre o link
7. O utilizador é redirecionado para a página de alteração da password
8. O utilizador insere a nova password
9. O utilizador confirma a nova password introduzida
10. A password do utilizador é alterada

Extensões:
4a. O utilizador insere um email inválido (formato errado/já registado/não institucional)
  4a1. O sistema informa o utilizador que o email é inválido
  4a2. O utilizador vai inserindo emails até introduzir um válido
7a. O utilizador abre o link após 15 minutos do envio do mesmo
  7a1. O sistema informa que o link já não encontra-se válido e que é necessário voltar a criar conta
8a. O utilizador insere uma password com um número de carateres inferior a 8 / sem pelo menos 1 número /  sem pelo menos 1 carater especial
  8a1. O sistema informa o utilizador que a password é inválida e pede uma nova password ao utilizador
  8a2. O utilizador vai inserindo passwords até introduzir uma password válida
9a. O utilizador insere uma password diferente da primeira
  9a1. O sistema informa o utilizador que as passwords são diferentes
  9a2. O utilizador vai inserindo password até introduzir uma igual à primeira

