`Grupo 4 - Escrito por Ricardo Guegan`

`User Story #11` - Como criador de testes, quero poder fazer testes com base em tags para os resolvedores poderem
resolver

### Testes

_Cenário:_ Utilizador com sessão iniciada, na página de criação de testes

1. Testar com uma Tag
2. Testar com múltiplas tags
3. Testar sem tags
4. Testar com uma grande pool de quizzes
5. Testar quando não há quizzes suficientes de uma tag
6. Testar quando não há quizzes disponíveis
7. Testar com uma titulo já existente

_Resultados esperados:_

* 1,2,4 - O teste é criado com sucesso
* 3 - O sistema notifica o utilizador da falta de uma tag
* 5 - O sistema cria com sucesso um teste, completando os quizzes em falta com quizzes de outra(s) tag(s)
* 6 - O sistema notifica o utilizador da falta de quizzes
* 7 - O sistema notifica o utilizador que o titulo já existe

`Caso de Uso #1 -`  Criação de testes

__Ator Primário:__ Criador de testes (role por definir)

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__

* Resolvedores: Querem resolver testes
* Criadores de testes: Querem uma interface para criar testes

__Pré-condição:__
* Está loged in
* Tem permissões de criador de testes

__Garantia de sucesso:__ Acede á interface de criação de testes

__Cenário Principal de Sucesso:__
 O criador entra página de criação de testes

1.  Utiliza uma barra de pesquisa onde insere as tags que quer para no teste
2.  Recebe um conjunto de 20 quizes distribuidos pelas tags selecionadas
3.  É mostrado o número de quizzes de cada tag
4. Insere o título do teste
5. Clica num botão para publicar o teste
6. Decrementa o uso dos quizzes utilizados
7. O teste fica disponível para todos os resolvedores

__Extenções__:
##### 2:
2.1- A distribuição dos quizzes pelas tags é feita de forma homogénea

2.2- Não existe quizzes de uma certa tag, distribui os quizzes em falta pelas outras tags

2.3- Não existe 20 quizzes com as tags selecionadas, o teste não é criado e é mostrado um aviso

##### 3:
3.1- Se o título esceder o limite de 200 caracteres recebe um aviso e deve renomear
#### 4:
4.1- Se o utilizador sair da página sem usar o botão subemeter o seu teste é esquecido 






