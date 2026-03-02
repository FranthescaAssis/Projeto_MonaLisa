# Projeto_MonaLisa
# Processamento de Imagem com OpenCV – Remoção de Canais de Cor

## Descrição

Este projeto em Python utiliza a biblioteca OpenCV para manipular os canais de cor de uma imagem. O programa carrega uma imagem chamada `entrada.jpg`, cria três cópias e remove individualmente os canais Azul, Verde e Vermelho.

Ao final da execução, são geradas três novas imagens com um dos canais de cor removido em cada uma delas.

---

## Tecnologias Utilizadas

- Python 3  
- OpenCV (cv2)  
- NumPy  

---

## Como Funciona

1. A imagem é carregada utilizando `cv2.imread()`.
2. São criadas três cópias da imagem original para evitar alterações diretas nela.
3. Cada canal de cor é manipulado separadamente.

No OpenCV, a ordem dos canais é:

- Canal 0: Azul  
- Canal 1: Verde  
- Canal 2: Vermelho  

Exemplo de remoção de canal:

```python
azul_zerado[:, :, 0] = 0
```

4. As imagens resultantes são salvas utilizando `cv2.imwrite()`.

---

## Como Executar

1. Instale as dependências:

```bash
pip install opencv-python numpy
```

2. Coloque a imagem desejada na mesma pasta do script com o nome `entrada.jpg`.

3. Execute o script:

```bash
python script.py
```

---

## Arquivos Gerados

Após a execução, serão criados os seguintes arquivos:

- `monalisa_sem_azul.jpg`
- `monalisa_sem_verde.jpg`
- `monalisa_sem_vermelho.jpg`

---

## Objetivo

Este projeto tem como objetivo demonstrar conceitos básicos de:

- Manipulação de matrizes com NumPy  
- Estrutura de cores no padrão BGR  
- Processamento digital de imagens utilizando OpenCV
