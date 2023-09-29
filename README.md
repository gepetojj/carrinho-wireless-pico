# Carrinho Wireless Pico

> Carrinho de controle remoto utilizando o Raspberry Pi Pico W.

## Objetivo

Implementar um carrinho de controle remoto utilizando o Raspberry Pi Pico W como microcontrolador e Thonny como IDE e gerenciador de projeto.

## Materiais

* Raspberry Pi Pico W (x1)
* Motor DC (x2)
* Sensor ultrassônico de distância (x2)

## Funcionamento

Assim que o Raspberry Pi Pico W é conectado em uma fonte de energia, verificará se já foi conectado em algum WiFi, se sim tentará conectar-se novamente a este, se não, abrirá automaticamente uma página para o usuário inserir a conexão WiFi desejada.  
Após o fim da configuração, o carrinho estará pronto para ser controlado, bastando apenas o acesso à sua página web. O projeto conta com sensores que informam ao usuário pela página web a distância do carrinho até o próximo obstáculo.