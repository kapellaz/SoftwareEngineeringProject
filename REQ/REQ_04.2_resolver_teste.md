`Grupo 2 - Escrito por Emanuel Roque`
# RESOLVER TESTE
Epic responsável pela seleção do teste a resolver e pela sua resolução

`User Story #4` - Como resolvedor quero poder realizar um teste.

### Testes

_Cenário:_ Resolvedor esta na pagina no ultimo quiz do teste

_Casos de teste:_

Testar sair a meio de um teste sem ter acabado a sua resolução

Testar perder a conexão ao submeter as respostas

Testar cancelar e sair de um teste

Testar submeter as respostas de um teste mas não confirmar a submissão

_Resultado esperado:_ O sistema resolve os problemas como indicado nas extensões

---

`Caso de Uso #2-` Resolver um teste

__Ator Primário:__ Utilizador autenticado com permissão para resolver testes (resolvedor)

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Resolvedor - Quer poder escolher um teste para resolver

__Pré-condição:__ 
*   Estar autenticado
*   Ter selecionado um teste

__Garantia Mínima:__ nenhuma

__Garantia de sucesso:__ O resolvedor consegue consegue submeter as suas respostas

__Cenário de Sucesso Principal:__
1. O resolvedor chega ao ultimo quiz do teste
2. O resolvedor submete as suas respostas
3. O sistema apresenta forma de confirmar a submissão
4. O resolvedor confirma a submissão
5. O sistema regista as respostas
6. O sistema redireciona o utilizador para a página dos resultados do teste

__Extensões:__ 

1.a O resolvedor sai do website antes de terminar um teste.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.a.1 O sistema não regista as respostas

1.b O resolvedor seleciona a opção de cancelar e sair

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.b.1 O sistema apresenta forma de confirmar a opção de cancelar e sair ou voltar para a resolução do teste

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.b.2 O resolvedor confima a opção de cancelar e sair ou volta para a resolução do teste

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1.b.3 O sistema não regista as respostas e redireciona o resolvedor para a pagina de seleção de testes ou permite o resolvedor continuar o teste

4.a O resolvedor perde a conexão ao confirmar a submissão das respostas

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.1 O sistema não regista as respostas
