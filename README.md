# Projeto-Automacao-Piano-Tiles
Essa é uma automação do jogo piano Tiles pra navegador link do jogo 
Foi usado como base o jogo Piano Tiles 2 do jogos360
https://www.jogos360.com.br/piano_tiles_2_online.html
monito na resolução 1280 por 720 
Por isso é importante mapear os pixels iniciais da sua tela e os pixels que serão tirados a screenshot
use o pyautogui.position() para pegar a posição do mouse.

# Como Funciona o Código
A ideia é mapear os pixels pretos da tela, tirando uma screenshot somente do jogo
Fazemos processos de tratamentos de imagens como: tons de cinza e binarização(ou é preto ou é branco)
Após isso usa-se bibliotecas de controle do mouse para clicar nos pixels correspondentes
