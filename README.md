<h1 align="center">
  Radar de trânsito com semáforo 
</h1>
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/65405310/168210955-d2b4467a-f7ba-4845-98c5-1b999076e00a.jpeg" style="width:50%;height:auto;">
</p>
                                                                                                                           
<h2>Objetivos </h2>

Familiarizar com as metodologias de aplicação para o desenvolvimento de sistemas de tempo real com uma aplicação,  implementado em sistemas computacionais simples (SCS), com tarefas periódicas, aperiódicas e requisitos temporais. Empregando então, os métodos a um projeto de radar de trânsito que detecta a passagem de de carros por sensores e aplica a multa caso ocorra alguma infração. 

Também como objetivo do trabalho temos a formação de	espírito	crítico	para a 	
avaliação	 de um sistem computacional de tempo real em relação ao seu desempenho,	 propiciando	
assim,	melhorias	na	compreensão	do	funcionando	destes	tipos	de	sistemas.

<h2>Métodos </h2>
<h4>Radar de trânsito com botão para passagem de pedestre</h4>
O projeto consiste em um radar de trânsito com uma câmera, integrado a um semáforo. O semáforo possui duas condições, vermelho ou verde, quando está no estado de sinal verde (aberto para carros), o radar detecta a passagem de carros por meio de três sensores e calcula sua velocidade,  se a velocidade for superior a permitida é feita a fotografia do carro e sua velocidade é exibida por meio de um display. Quando o semáforo está em estado vermelho (fechado para carros), o radar de trânsito apenas detecta a passagem de carros e faz a fotografia do veículo.

<br>
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/65405310/168212085-d854ed8c-9ac4-4718-8d5b-b1ca0a38c022.png" style="width:20%;height:auto;">
</p>


<h4>Condições do projeto</h4>
O projeto é baseado em duas condições. A primeira trata-se de:

* Semáforo aberto:

O radar faz a fotografia do veículo baseado na condição da verificação da velocidade. Quando o sinal está aberto a leitura dos sensores calcula e informa a velocidade do carro para o display. Caso a velocidade seja superior a permitida, a câmera será acionada.

<br>
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/65405310/168211918-01fa6c07-af9d-4487-a975-799f377811fa.jpeg" style="width:30%;height:auto;">
</p>

* Semáforo fechado: O radar faz a fotografia do veículo baseado na condição de Ultrapassagem do sinal vermelho. Quando o sinal está fechado a leitura dos sensores verifica se houve a passagem de algum automóvel. Caso algum carro passe, a câmera é acionada.
<p align="center"> 
  <img src="https://user-images.githubusercontent.com/65405310/168211941-d00edf45-b241-497d-bfdc-261560caffa2.jpeg" style="width:30%;height:auto;">
</p>

<h2> Simulação </h2>
Escolhemos simular o projeto em um simulador de rôbos CoppeliaSim. Que usa um mecanismo de cinemática para cálculos de cinemática direta e inversa e várias bibliotecas de simulação de física  para realizar simulação de corpo rígido. Para programar as tarefas usamos uma API remota em python, que possibilita o controle dos processos 
