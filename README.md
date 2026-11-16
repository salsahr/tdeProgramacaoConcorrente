# tdeProgramacaoConcorrente

Link do video no YouTube: https://www.youtube.com/watch?v=4HiIAR7BqXQ

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

Instrução de execução do código da Parte 2:

Para rodar com o semaforo:
1. entrar na pasta parte2-semaforo
2. python pt2_com_semaforo.py


Para rodar sem o semaforo:
1. entrar na pasta parte2-semaforo
2. python pt2_sem_semaforo.py

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





Relatório Parte 3

Instrução de execução do código do Deadlock:

Para rodar com o deadlock:
1. entrar na pasta parte3-deadlock
2. python pt3errofinal.py

Para rodar sem o deadlock:
1. entrar na pasta parte3-deadlock
2. python pt3semerrofinal.py

 Nesse código temos duas threads e dois locks, o LOCK_A e o LOCK_B. A Thread 1 pega o LOCK_A e depois tenta pegar o LOCK_B, já a Thread 2 pega o LOCK_B e depois tenta pegar o LOCK_A. Colocamos um time.sleep(0.5) entre as duas aquisições para garantir que as duas threads peguem o primeiro lock antes de pedir o segundo, porque sem ele às vezes uma thread termina antes da outra começar e o deadlock não aparece. Como cada thread fica segurando um lock e esperando o outro, nenhuma delas anda e o programa nunca termina.
 As quatro condições de Coffman aparecem nesse exemplo. A exclusão mútua é o próprio Lock, que só pode ser usado por uma thread por vez. O manter e esperar acontece porque cada thread segura um lock e pede o outro. A não preempção é porque nenhuma thread consegue tirar o lock da outra, ele só é liberado por quem pegou. E a espera circular é a T1 esperando o LOCK_B que está com a T2, enquanto a T2 espera o LOCK_A que está com a T1.
 Para corrigir usamos a hierarquia de recursos, fazendo todas as threads pegarem sempre o LOCK_A antes do LOCK_B. Assim, se a T1 pega o LOCK_A primeiro, a T2 fica esperando o LOCK_A sem segurar nenhum lock, a T1 termina e libera os dois, e só depois a T2 executa. A condição de Coffman que foi quebrada é a espera circular, já que com a ordem fixa não dá mais pra formar um ciclo de espera.

 Logs Parte 3
 Com deadlock:


 T1 pegou LOCK_A


 T2 pegou LOCK_B


 T1 aguardando LOCK_B


 T2 aguardando LOCK_A



 Sem deadlock:


 T1 pegou LOCK_A


 T1 aguardando LOCK_B


 T1 pegou LOCK_B


 T1 concluiu


 T2 pegou LOCK_A


 T2 aguardando LOCK_B


 T2 pegou LOCK_B


 T2 concluiu


 FIM