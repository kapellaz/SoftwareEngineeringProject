`Grupo 3 - Escrito por David Moreira`

# User Story #9 
> Como utilizador, quero poder ver uma lista de solvers ordenada por número de _quizzes_ corretamente resolvidos para saber quem são os melhores solvers

__Testes:__

- Verificar que o primeiro lugar do _hall of fame_ pertence ao solver com o maior nº de quizzes corretamente resolvidos

- Verificar que os 10 solvers com mais quizzes resolvidos corretamente tem uma instância no hall of fame

- Verificar que, para um dado solver, o nº de testes corretamente resolvidos está certo

## Caso de Uso #1 - Ver o _hall of fame_ depois de terminar um teste  

__Ator primário:__ Solver autenticado

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Solver - Quer os seus dados atualizados no _hall of fame_

__Pré-condição:__
* Submeter um teste resolvido
* Acertar, pelo menos, um quiz

__Garantia mínima:__ O _hall of fame_ é apresentado por ordem descendente de número de quizzes corretamente resolvidos

__Garantia de sucesso:__ O _hall of fame_ é corretamente alterado com os novos valores

__Cenário Principal de Sucesso:__

1. O solver terminou um teste

2. O solver clica no botão para ver o _hall of fame_

3. O _hall of fame_ é atualizado com os novos valores e o solver verifica isso

__Extensões:__

3a. O nº de quizzes corretamente resolvidos é alterado de forma a que a posição do solver no _hall of fame_ é maior

3b. Um segundo solver obtem um maior número de quizzes corretamente resolvidos do que o solver atualmente autenticado, diminuindo a posição deste último

## Caso de Uso 2: Visitar a _hall of fame_

__Ator primário:__ Utilizador (logado ou não)

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Utilizador - Quer ver a _hall of fame_

__Pré-condição:__
* Ter acesso à _navigation bar_

__Garantia de sucesso:__ O _hall of fame_ é apresentado por ordem descendente de número de quizzes corretamente resolvidos

__Cenário Principal de Sucesso:__

1. O utilizador está a navegar pelo website

2. O utilizador clica no botão para aceder ao _hall of fame_

3. O utilizador consegue ver o _hall of fame_ e todos os solvers registados no mesmo

__Extensões:__

2a. O utilizador acede à página inicial onde consegue ver um _preview_ com o top 3 do _hall of fame_
    
2a1. O utilizador clica no botão para ver o _hall of fame_ completo

2a2. O utilizador escolhe ordenar o _hall of fame_ por número de quizzes corretamente resolvidos

2b. O utilizador clica no botão da _nav bar_ para aceder ao _hall of fame_

2b1. O utilizador escolhe ordenar o _hall of fame_ por número de quizzes corretamente resolvidos
