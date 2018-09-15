# Algoritmos Computação Gráfica

## Configuração

Para funcionamento do programa em ambientes Linux é necessário a instalação do python 3

```
sudo apt-get update
sudo apt-get install python3
```

Verifique se a versão do python está correta: `python --version`.

Baixe as dependências através do pip

```
apt install python-pip
pip install -r requirements.txt
```

## Rodar
Para rodar os algoritmos, basta estar dentro da pasta com o código e aplicar no terminal:

```
python computacaoGrafica.py
```

## Estrutura 
O código contém duas classes: Application e Outros. A classe Application contém os algoritmos/transformações aplicavéis em uma reta e a janela de visualização. A classe Outros contém os algoritmos de preenchimento e os aplicavéis em uma circunferência. 

Ambos são estruturados com containers no ínicio, que representam o bloco aonde ficará a informação na interface. Após os containers, configura-se cada 'Label' e 'Button'. E por fim, as funções.

## Manual do Usuário

Para mais informações, abra o ManualUsuario.pdf

Para ver o programa funcionando, abra o arquivo Video_Interface_Funcionando.mp4


