# tdeProgramacaoConcorrente

Link do video no YouTube: 

Nome do Grupo: TDE2 20

Nome dos integrantes:
Eric Tan Hui Zhen
Guilherme Hoshino Rouver
Otávio Costa Dallo

Linguagem escolhida: Python

Instrução de execução do código do Jantar dos filósofos:

Para rodar com o deadlock:
1. entrar na pasta parte1-filosofos
2. cd .\JantarFilosofoDeadlock\
3. python main.py

Para rodar sem o deadlock:
1. entrar na pasta parte1-filosofos
2. cd .\JantarFilosofosSemDeadlock\
3. python main.py

Relatório curto Jantar dos filósofos:

A dinâmica do problema do jantar dos filósofos é baseada na premissa em que tem uma mesa de jantar com um prato grande de macarrão no centro da mesa, ao redor da mesa há 5 filósofos com pratos menores e 5 garfos.
Para eles conseguirem comer a condição é que eles peguem tanto o garfo posicionado em sua esquerda quanto o garfo da direita. E é nesse momento em que surge o impasse, como existem apenas 5 garfos, se todos pegarem
ao mesmo tempo por exemplo, o garfo da esquerda, não irá sobrar nenhum garfo na direita de ninguém, logo ninguém consegue comer e todos ficam esperando. A condição de Coffman que será negada na nossa solução proposta 
é a de condição de espera circular.

Fluxograma está dentro da pasta parte1-filosofos

Relatório Parte 2 

 A versão sem sincronização perde incrementos devido a Race Condition, já que a operação contador = temp + 1 não é atômica pois le o valor soma 1 e reescreve o valor, e devido a troca de contexto forçado pelo sleep no meio da seção crítica, vários threads leem o mesmo valor, dormem e quando acordam reescrevem o contador, trabalhando com dados desatualizados. 
 A versão com semáforo impede isso usando exclusão mútua, fazendo com que o thread necessite de autorização do semáforo para acessar o contador (semaforo.acquire()), se um thread tenta acessar o contador enquanto outra thread possui a permissão a thread é bloqueada e entra em uma fila até o contador estiver disponivel, sendo necessário que a thread devolva a autorização para o semáforo (semaforo.release()). Estes comandos protegem o acesso, agindo como uma barreira implícita de memória, tornando o contador visível imediamente para a proxima thread que consegue autorização. Devido a essa fila, o throughput é sacrificado, aumentando significativamente o tempo de execução, porém mantém integridade absoluta dos dados com 0 perdas.

 Logs Parte 2
 Sem semaforo:
 Esperado:  1600000  Obtido:  200140 Perdidos:  1399860 Tempo:  3.581686496734619
 Esperado:  1600000  Obtido:  200393 Perdidos:  1399607 Tempo:  3.5619845390319824
 Esperado:  1600000  Obtido:  200320 Perdidos:  1399680 Tempo:  3.7311270236968994

 Com semaforo: 
 Esperado:  1600000  Obtido:  1600000 Perdidos:  0 Tempo:  18.084654808044434
 Esperado:  1600000  Obtido:  1600000 Perdidos:  0 Tempo:  17.362584829330444
 Esperado:  1600000  Obtido:  1600000 Perdidos:  0 Tempo:  17.701602458953857