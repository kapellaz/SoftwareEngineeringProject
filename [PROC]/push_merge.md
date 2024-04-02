# Práticas de pushing_merging
**Qualquer alteração feita num ficheiro comum deve ser avisado no Discord em "aviso-mudanças-de-código" utilizando @everyone**

## Branch a usar

### Branch main
* Atualização de profiles
* Atualização de Requisitos
* features que já tenham sido testadas no branch dev e aprovadas são adicionadas no final de cada sprint

### Branch dev
* features que já tenham sido testadas individualmente no respetivo branch e aprovadas pelo deployer do grupo
* outros ficheiros não relacionados com codigo

### Branch [feature/Nome] ex:"feature/register"
* deriva do branch dev
* criado para desenvolver uma determinada feature
* deve ser trabalhado apenas pelo(s) desenvolvedor(es) (excepto raras exceções)
* apagado quando a feature passa nos testes e é incorporada no branch dev


## Merge request 
* Colocar um membro do próprio grupo responsável por rever o código como revisor (geralmente será o deployer) 
* Fazer um resumo das alterações em português
* Resumo escrito de forma sucinta e objetiva

* Usar o pipeline para verificação (feito pelo reviewer) 

 Será recusado o merge se a documentação não for clara ou se falhar em qualquer teste ou nas metricas definidas