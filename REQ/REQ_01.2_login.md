Grupo 1 - Escrito por André Moreira e João Pinto

---------------------------------Epic-------------------------

Autenticação

Como utilizador, quero criar ou iniciar sessão ou recuperar a palavra-passe da minha conta para criar, rever e resolver quizzes.

-----------User Story-----------------------------

Qualquer utilizador previamente registado poderá efetuar login para conseguir acesso às funcionalidades do website a que está permitido.

Testes

Cenário: O utilizador quer iniciar sessão

Casos de teste:
* Testar a combinação de todos os campos inseridos e não inseridos
* Testar com email sem estar confirmado o registo
* Testar com email que não tenha sido registado 
* Testar com email que não seja institucional
* Testar com password com número de carateres inferior a 8
* Testar com password sem pelo menos 1 número 
* Testar com password sem pelo menos 1 carater especial 
* Testar com os dados corretos

Resultado esperado: O sistema é capaz de identificar corretamente os erros

-------------Caso de uso--------------------

Caso de uso 1: Login
Ator Primário: Utilizador com conta
Nível: Objetivo do utilizador
Stakeholders e Interesses:
     Utilizador com conta - Quer poder iniciar sessão para aceder ao website.
Précondição: Estar na página de login.
Garantia Mínima: Há acesso à página inicial do website, à de registo e à de login.
Garantia de Sucesso: Pode aceder a todos os quizzes disponíveis e também criá-los.
Cenários Principais de Sucesso: 
1. O utilizador está com a página inicial do website aberta
2. O utilizador carrega na opção login
3. O utilizador insere o email
4. O utilizador insere a password
5. O utilizador entra na sua conta
6. O utilizador é redirecionado para a página onde se encontram quizzes e a opção para os criar
Extensões:
3a O utilizador insere um email inválido (formato errado/não registado/não institucional)
   3a1 O sistema informa que o utilizador inseriu credenciais erradas
4a O utilizador insere uma password não correspondente à conta referente ao email
   4a1 O sistema informa que o utilizador inseriu credenciais erradas   
