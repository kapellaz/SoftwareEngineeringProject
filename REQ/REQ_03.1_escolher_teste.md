`Grupo 2 - Escrito por Emanuel Roque, Gonçalo Senra, Guilherme Branco`
# RESOLVER TESTE
Epic responsável pela seleção do teste a resolver e pela sua resolução

`User Story #3` - Como utilizador autenticado com permissão para resolver testes, quero poder escolher um teste para resolver.

### Testes

_Cenário:_ estar autenticado com utilizador que não tem permissões para resolver e existir pelo menos 1 teste para escolher

_Casos de teste:_

Testar selecionar um Teste para resolver

_Resultado esperado:_ Sistema é capaz de identificar corretamente que utilizador não tem premissões suficientes e  de informar o utilizador

_Cenário:_ estar autenticado com utilizador que tem permissões para resolver e existir pelo menos 1 teste para escolher

_Casos de teste:_

Testar selecionar um teste e perder a ligação ao servidor

_Resultado esperado:_ Sistema redireciona o resolvedor para a página de seleção de testes sem guardar o estado

_Cenário:_ estar autenticado com utilizador que tem permissões para resolver e não existir testes para escolher

_Casos de teste:_

Testar aceder á pagina para seleção de testes

_Resultado esperado:_ Sistema apresenta uma mensagem “nenhum teste disponível” 

---

`Caso de Uso #1-` Selecionar um teste

__Ator Primário:__ Utilizador autenticado com permissão para resolver testes (resolvedor)

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Resolvedor - Quer poder escolher um teste para resolver

__Pré-condição:__ 
*   Estar autenticado
*   Estar na página de seleção de testes
*   Ter permissão para resolver teste (fez revisão de 3 quizzes)

__Garantia Mínima:__ nenhuma

__Garantia de sucesso:__ O sistema devolve o teste escolhido

__Cenário de Sucesso Principal:__
1. O sistema apresenta todos os testes disponíveis
2. O resolvedor seleciona um teste para resolver
3. O sistema redireciona o resolvedor para a página de resolução do teste

__Extensões:__ 

1.a Não existem testes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.a.1 Sistema apresenta uma mensagem “nenhum teste disponível”

2.a Utilizador que quer selecionar um teste no tem premissão para o fazer

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.a.1 Sistema informa que utilizador não possui premissões para selecionar um teste

2.b Falha na seleção de um teste.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.1 Sistema redireciona o resolvedor para a página de seleção de testes sem guardar o estado

