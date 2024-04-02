Grupo 1 - Escrito por Gonçalo Almeida e João Santos

---------------------------------Epic-------------------------

Autenticação

Como utilizador, quero criar ou iniciar sessão ou recuperar a palavra-passe da minha conta para criar, rever e resolver quizzes.

-----------------------------User Story-----------------------------


Como utilizador sem conta, quero poder criar uma conta para poder criar quizzes.

Testes

Cenário: O utilizador ainda não tem uma conta registada.

Casos de teste:
* Testar com email num formato errado
* Testar com email que já tenha sido registado
* Testar com email que não seja institucional
* Testar com password com número de carateres inferior a 8
* Testar com password sem pelo menos 1 número
* Testar com password sem pelo menos 1 carater especial
* Testar com link expirado

Resultado esperado: O sistema é capaz de identificar corretamente os erros no email/password inserido e informar o utilizador.

-----------------------------Caso de Uso-----------------------------


Caso de Uso 1: Registar uma conta
Ator Primário: Utilizador sem conta
Nível: Objetivo do utilizador
Stakeholders e Interesses:
     Utilizador sem conta - Quer poder criar uma conta para poder criar quizzes.
     Site - Obtém informação sobre o novo utilizador
Pré-condição: Estar na página de registo.
Garantia Mínima: Há acesso à página inicial do website, à de registo e à de login.
Garantia de Sucesso: Passa a haver acesso à página de criar e editar quiz.
Cenário Principal de Sucesso:
1. O utilizador carrega na opção de registar uma conta
2. O utilizador insere o seu mail
3. O utilizador insere uma password
4. O utilizador volta a inserir a sua password (para verificação)
5. O utilizador insere o seu nome e apelido
6. O sistema envia um link de confirmação para o email do utilizador 
7. O utilizador abre o link
8. O utilizador é redirecionado para a página de login
Extensões:
2a. O utilizador insere um email inválido (formato errado/já registado/não institucional)
  2a1. O sistema informa o utilizador que o email é inválido
  2a2. O utilizador vai inserindo emails até introduzir um válido
3a. O utilizador insere uma palavra-passe com um número de carateres inferior a 8 / sem pelo menos 1 número /  sem pelo menos 1 carater especial
  3a1. O sistema informa o utilizador que a palavra-passe é inválida e pede uma nova palavra-passe ao utilizador
  3a2. O utilizador vai inserindo palavra-passes até introduzir uma palavra-passe válida
4a. O utilizador insere uma palavra-passe diferente da primeira
  4a1. O sistema informa o utilizador que as palavras-passes são diferentes
  4a2. O utilizador vai inserindo palavra-passes até introduzir uma igual à primeira
7a. O utilizador abre o link após 15 minutos do envio do mesmo
  7a1. O sistema informa que o link já não encontra-se válido e que é necessário voltar a criar conta
