`Grupo 1 - Escrito por Andre Moreira`

# PERFIL DE UTILIZADOR

`User Story #13` - Como utilizador autenticado, quero poder aceder a uma página de perfil e utilizar as funções por ela disponibilizadas.

### Testes
	Cenário: Utilizador (com a sessão iniciada) quer aceder à sua página de perfil e utilizar as funções que a página contém.
 	Testar aceder à página de perfil
	Testar aceder à página de importar XML
	Testar aceder à página de exportar XML
	Testar aceder à página de Meus quizzes
	Testar a vericidade dos dados de revisão de quiz
	Testar a vericidade dos dados de Avaliação

_Resultado esperado:_ Sistema permite utilizar todas as funções corretamente.
---

`Caso de Uso #1-` Aceder página de perfil e utilizar uma função.

__Ator Primário:__ Utilizador autenticado

__Nível:__ Objetivo do utilizador

__Stakeholders e Interesses:__ Utilizador autenticado- poder ver a sua página de perfil e utilizar funções fornecidas pela página.

__Pré-condição:__ 
*   Estar autenticado
__Garantia Mínima:__ nenhuma

__Garantia de sucesso:__ O sistema apresenta a página de perfil e permite a utilização das suas funções.

__Cenário de Sucesso Principal:__
1. O utilizador clica no botão para ir para o seu perfil.
2. O utilizador é redirecionado para a sua página de perfil.
3. O Utilizador clica numa das funções fornecidas pela página.
4. O Utilizador é redirecionado para a página referente à função selecionada.

__Extensões:__ 

4.a O utilizador não tem as condições necessárias para aceder à página da função selecionada.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4.a.1 O sistema apresenta uma mensagem de erro. 
