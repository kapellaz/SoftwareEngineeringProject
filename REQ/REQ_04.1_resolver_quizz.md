`Grupo 2 - Escrito por Emanuel Roque, Henrique Costa, João Coelho, Miguel Pedroso`
# RESOLVER TESTE
Epic responsável pela seleção do teste a resolver e pela sua resolução

`User Story #4` - Como resolvedor quero poder realizar um teste.

### Testes

_Cenário:_ Resolvedor está na pagina do primeiro quiz do teste

_Casos de teste:_

Testar seleção de várias opções de resposta numa pergunta

Testar não selecionar nenhuma resposta num quiz

Testar cancelar e sair de um teste

Testar regressar ao quiz anterior

_Resultado esperado:_ O sistema resolve os problemas como indicado nas extensões

---

`Caso de Uso #1-` Resolver um quiz(1 pergunta de um teste)

__Ator Primário:__ Utilizador autenticado com permissão para resolver testes (resolvedor)

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Resolvedor - Quer resolver um quiz

__Pré-condição:__ 
*   Estar autenticado
*   Ter selecionado um teste
*   Estar na página do quiz em questão

__Garantia Mínima:__ nenhuma

__Garantia de sucesso:__ O resolvedor consegue avançar para o próximo quiz(caso exista) ou terminar o teste

__Cenário de Sucesso Principal:__
1. O sistema apresenta a pergunta e as várias opções
2. O resolvedor seleciona a opção de resposta que considera correta ou não seleciona nenhuma
3. O resolvedor escolhe

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3a. avançar para o próximo quiz (no caso de existir)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3b. regressar ao quiz anterior(no caso de existir)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3c. terminar o teste

4. O sistema  redireciona o resolvedor

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4a. para a página do próximo quiz (existe pelo menos mais um quiz por resolver)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4b. para a página do quiz anterior (existe pelo menos mais que um quiz anterior)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4c. para uma página na qual pode ver os seus resultados e sair da resolução do teste (último quiz do teste)

__Extensões:__ 

2.a O resolvedor seleciona mais do que uma opção correta em quizzes de escolha múltipla.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.a.1 O sistema apaga a seleção anterior

2.b O resolvedor não seleciona nenhuma opção em quizzes de escolha múltipla.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.1 O sistema permite avançar para o próximo quiz

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.2 O resolvedor avança para o próximo quiz

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2.b.3 O sistema considera a pergunta como errada (caso esteja em branco na submissão do teste)

3.a O resolvedor seleciona a opção de voltar ao quiz anterior(apenas disponivel se existir)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3.a.1 O sistema redireciona o resolvedor para a pagina do quiz anterior

4.a O resolvedor seleciona a opção de cancelar e sair

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.1 O sistema apresenta forma de confirmar a opção de cancelar e sair ou de voltar para a resolução do teste

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.2 O resolvedor confima a opção de cancelar e sair ou volta para a resolução do teste

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.3 O sistema não regista as respostas e redireciona o resolvedor para a pagina de seleção de testes ou permite o resolvedor continuar o teste




