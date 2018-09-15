import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import math
from pyx import *
from PIL import Image

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ("Arial", "10")

        sys.setrecursionlimit(100000)

        self.container1 = Frame(master, pady=5)
        self.container1.pack()

        self.containerRetas = Frame(master, pady=5)
        self.containerRetas.pack()

        #Inserir o valor de x1 e x2
        self.container2 = Frame(master, padx=20)
        self.container2.pack()

        # Inserir o valor de y1 e y2
        self.container3 = Frame(master, padx=20, pady=5)
        self.container3.pack()

        #Plotar Gráfico
        self.container4 = Frame(master, padx=30, pady=5)
        self.container4.pack()

        #Vetor (a,b)
        self.container5 = Frame(master, padx=10)
        self.container5.pack()

        #Vetor a
        self.container6 = Frame(master, pady=5)
        self.container6.pack()

        #Vetor b
        self.container7 = Frame(master)
        self.container7.pack()

        #Função Translação e Escala
        self.container8 = Frame(master, pady=10)
        self.container8.pack()

        #Função Rotação
        self.container9 = Frame(master, padx=20)
        self.container9.pack()

        self.container10 = Frame(master, pady=15)
        self.container10.pack()

        #Função Reflexão
        self.container11 = Frame(master, pady=1)
        self.container11.pack()

        self.container12 = Frame(master, pady=10)
        self.container12.pack()

        #Função Cisalhamento
        self.container13 = Frame(master, padx=20)
        self.container13.pack()

        self.container14 = Frame(master, pady=10)
        self.container14.pack()

        #Algoritmos
        self.container15 = Frame(master, pady=5, padx=2)
        self.container15.pack()

        # DDA & Breshman Algorithm
        self.container16 = Frame(master, pady=10, padx=10)
        self.container16.pack()

        #Janela
        self.container17 = Frame(master, pady=5)
        self.container17.pack()

        self.container18 = Frame(master, pady=10)
        self.container18.pack()

        self.container19 = Frame(master, pady=10)
        self.container19.pack()

        self.container20 = Frame(master, pady=10)
        self.container20.pack()

        # Demais operações
        self.container21 = Frame(master, pady=10)
        self.container21.pack()

        ################################# FIM CONTAINERS ##########################

        self.retas = Label(self.containerRetas, text="Retas", fg="blue", font=(self.fontePadrao, "11", "bold"))
        self.retas.pack(side=LEFT)

        #Entrada dos valores
        self.nomeLabel = Label(self.container2, text="Digite o x1", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT, padx=10)

        self.x = Entry(self.container2, font=self.fontePadrao)
        self.x["width"] = 5
        self.x.pack(side=LEFT)

        self.yLabel = Label(self.container2, text="Digite o y1", font=self.fontePadrao)
        self.yLabel.pack(side=LEFT, padx=10)

        self.y = Entry(self.container2, font=self.fontePadrao)
        self.y["width"] = 5
        self.y.pack(side=LEFT)

        self.x1Label = Label(self.container3, text="Digite o x2", font=self.fontePadrao)
        self.x1Label.pack(side=LEFT, padx=10)

        self.x2 = Entry(self.container3, font=self.fontePadrao)
        self.x2["width"] = 5
        self.x2.pack(side=LEFT)

        self.y2Label = Label(self.container3, text="Digite o y2", font=self.fontePadrao)
        self.y2Label.pack(side=LEFT, padx=10)

        self.y2 = Entry(self.container3, font=self.fontePadrao)
        self.y2["width"] = 5
        self.y2.pack(side=LEFT)

        self.plotarGrafico = Button(self.container4,text="Plotar Gráfico", command=self.plotaGrafico)
        self.plotarGrafico["font"] = ("Calibri", "9")
        self.plotarGrafico["width"] = 12
        self.plotarGrafico.pack()

        #Vetor T(a,b)
        self.mensagem = Label(self.container5, text="Aplique as transformações sob o vetor T(a,b)", font=(self.fontePadrao, "11"))
        self.mensagem.pack()

        self.enterA = Label(self.container6, text="a ", font=self.fontePadrao)
        self.enterA.pack(side=LEFT)

        self.a = Entry(self.container6, font=self.fontePadrao)
        self.a["width"] = 5
        self.a.pack(side=LEFT)

        self.enterB = Label(self.container7, text="b ", font=self.fontePadrao)
        self.enterB.pack(side=LEFT)

        self.b = Entry(self.container7, font=self.fontePadrao)
        self.b["width"] = 5
        self.b.pack(side=LEFT)

        #Função Translação
        self.transladar = Button(self.container8, text="Translação", command=self.aplicaTranslacao)
        self.transladar["font"] = ("Calibri", "9")
        self.transladar["width"] = 12
        self.transladar.pack(side=LEFT, padx=10)

        #Função Escala
        self.escala = Button(self.container8, text="Escala", command=self.aplicaEscala)
        self.escala["font"] = ("Calibri", "9")
        self.escala["width"] = 12
        self.escala.pack(side=RIGHT)

        #Função Rotação
        self.labelAngulo = Label(self.container9, text="Digite o ângulo em graus", font=(self.fontePadrao, "11"))
        self.labelAngulo.pack()

        self.angulo = Entry(self.container10, font=self.fontePadrao)
        self.angulo["width"] = 5
        self.angulo.pack(side=LEFT)

        self.grau = Label(self.container10, text=" º", font=self.fontePadrao)
        self.grau.pack(side=LEFT)

        self.rotacao = Button(self.container10, text="Rotacão", command=self.aplicaRotacao)
        self.rotacao["font"] = ("Calibri", "9")
        self.rotacao["width"] = 12
        self.rotacao.pack(side=RIGHT, padx=10)

        # Reflexão
        self.labelRotaciona = Label(self.container11, text="Selecione um dos eixos para aplicar Reflexão", font=(self.fontePadrao, "11"))
        self.labelRotaciona.pack()

        self.eixoX = Button(self.container12, text="Eixo X", command=lambda: self.aplicaReflexao('x'))
        self.eixoX["font"] = ("Calibri", "9")
        self.eixoX.pack(side=LEFT)

        self.eixoY = Button(self.container12, text="Eixo Y", command=lambda: self.aplicaReflexao('y'))
        self.eixoY["font"] = ("Calibri", "9")
        self.eixoY.pack(side=LEFT, padx=5)

        self.origem = Button(self.container12, text="Origem", command=lambda: self.aplicaReflexao('origem'))
        self.origem["font"] = ("Calibri", "9")
        self.origem.pack(side=LEFT)

        # Cisalhamento
        self.labelForca = Label(self.container13, text="Digite a força que deseja aplicar sobre os eixos", font=(self.fontePadrao, "11"))
        self.labelForca.pack()

        self.inputCisalhamento = Entry(self.container14, font=self.fontePadrao, width=5)
        self.inputCisalhamento.pack(side=LEFT)

        self.cisaEixoX = Button(self.container14, text= "Eixo X", command=lambda: self.aplicaCisalhamento('x'))
        self.cisaEixoX["font"] = ("Calibri", "9")
        self.cisaEixoX.pack(side=LEFT, padx=5)

        self.cisaEixoY = Button(self.container14, text="Eixo Y", command=lambda: self.aplicaCisalhamento('y'))
        self.cisaEixoY["font"] = ("Calibri", "9")
        self.cisaEixoY.pack(side=LEFT)


        #Algoritmos
        self.mensagem3 = Label(self.container15, text="Aplique os seguintes algoritmos", font=(self.fontePadrao, "11"))
        self.mensagem3.pack()

        #DDA Algorithm
        self.dda = Button(self.container16, text="DDA", command=lambda: self.aplicaDDA('reta', 0,0,0,0))
        self.dda["font"] = ("Calibri", "9")
        self.dda["width"] = 10
        self.dda.pack(side=LEFT)

        #Breshman Algorithm
        self.bres = Button(self.container16, text="Bresenham", command=self.aplicaBresenham)
        self.bres["font"] = ("Calibri", "9")
        self.bres["width"] = 10
        self.bres.pack(side=RIGHT)

        # Janela
        self.window = Label(self.container17, font=(self.fontePadrao, "11"), text="Digite os valores limites da janela")
        self.window.pack()

        self.inputXSup = Label(self.container18, font=self.fontePadrao, text="X Máx")
        self.inputXSup.pack(side=LEFT)
        self.xSup = Entry(self.container18, font=self.fontePadrao, width=5)
        self.xSup.pack(side=LEFT)

        self.inputYSup = Label(self.container18, font=self.fontePadrao, text="Y Máx")
        self.inputYSup.pack(side=LEFT)
        self.ySup = Entry(self.container18, font=self.fontePadrao, width=5)
        self.ySup.pack(side=LEFT)

        self.inputXInf = Label(self.container19, font=self.fontePadrao, text="X Mín")
        self.inputXInf.pack(side=LEFT)
        self.xInf = Entry(self.container19, font=self.fontePadrao, width=5)
        self.xInf.pack(side=LEFT)

        self.inputYInf = Label(self.container19, font=self.fontePadrao, text="Y Mín")
        self.inputYInf.pack(side=LEFT)
        self.yInf = Entry(self.container19, font=self.fontePadrao, width=5)
        self.yInf.pack(side=LEFT)

        self.cohen = Button(self.container20, text="Cohen-Sutherland", command=self.aplicaCohen, width=20, font=("Calibri", "9"))
        self.cohen.pack(side=LEFT)

        self.cohen = Button(self.container20, text="Liang-Barksy", command=self.aplicaLiangBarksy, width=20,
                            font=("Calibri", "9"))
        self.cohen.pack(side=LEFT, padx=5)

        self.demais = Button(self.container21, text="Demais operações", command=self.chamaJanelaePreenchimento,
                             font=("Calibri", "12", "bold"), fg="red", width=20)
        self.demais.pack()


    def plotaGrafico(self):
        x = [float(self.x.get()), float(self.x2.get())]
        y = [float(self.y.get()), float(self.y2.get())]

        plt.plot(x, y, label="Original")
        plt.axis('off')
        plt.legend()
        plt.show()

    def aplicaBresenham(self):
        x1 = float(self.x.get())
        x2 = float(self.x2.get())
        y1 = float(self.y.get())
        y2 = float(self.y2.get())

        dx = x2 - x1
        dy = y2 - y1

        im = Image.new("RGB", (255, 255))
        im.putpixel((int(x1), int(y1)), (255, 0, 0))

        if dx < 0:
            dx = -dx
            xIncr = -1
        else:
            xIncr = 1

        if dy < 0:
            dy = -dy
            yIncr = -1
        else:
            yIncr = 1

        if dx > dy:
            p = 2 * dy - dx
            const1 = 2*dy
            const2 = 2 * (dy - dx)

            for i in range(int(dx)):
                x1 += xIncr
                if p < 0:
                    p += const1
                else:
                    y1 += yIncr
                    p += const2

                im.putpixel((int(x1), int(y1)), (255, 0, 0))
        else:
            p = 2 * dx - dy
            const1 = 2 * dx
            const2 = 2 * (dx - dy)
            for i in range(int(dy)):
                y1 += yIncr
                if p < 0:
                    p += const1
                else:
                    p += const2
                    x1 += xIncr

                im.putpixel((int(x1), int(y1)), (255, 0, 0))
        im.show()

    def aplicaDDA(self, tipo, x1, y1, x2, y2):

        if(tipo == "reta"):
            x1 = float(self.x.get())
            x2 = float(self.x2.get())
            y1 = float(self.y.get())
            y2 = float(self.y2.get())

        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            passos = abs(dx)
        else:
            passos = abs(dy)

        xIncr = dx/passos
        yIncr = dy/passos

        im = Image.new("RGB", (255, 255))
        im.putpixel((round(x1), round(y1)), (255, 0, 0))

        for i in range(int(passos)):
            x1 += xIncr
            y1 += yIncr

            im.putpixel((round(x1), round(y1)), (255, 0, 0))

        im.show()

    def aplicaRotacao(self):
        alpha = np.radians(float(self.angulo.get()))

        x = np.array([float(self.x.get()), float(self.x2.get())])
        y = np.array([float(self.y.get()), float(self.y2.get())])

        xCos = x * np.cos(alpha)
        xSen = x * np.sin(alpha)

        yCos = y * np.cos(alpha)
        ySen = y * np.sin(alpha)

        novoX = xCos - ySen
        novoY = xSen + yCos

        plt.plot(novoX, novoY, label="Rotação")
        plt.title("Gráfico Rotação", fontsize=18)
        plt.legend()
        plt.axis('off')
        plt.show()

    def aplicaTranslacao(self):
        a = float(self.a.get())
        b = float(self.b.get())

        x = np.array([float(self.x.get()), float(self.x2.get())])
        y = np.array([float(self.y.get()), float(self.y2.get())])

        novoX = x + a
        novoY = y + b

        plt.plot(novoX, novoY, label="Translação")
        plt.title("Gráfico Translação", fontsize=18)
        plt.legend()
        plt.axis('off')
        plt.show()

    def aplicaEscala(self):
        a = float(self.a.get())
        b = float(self.b.get())

        x = np.array([float(self.x.get()), float(self.x2.get())])
        y = np.array([float(self.y.get()), float(self.y2.get())])

        novoX = x * a
        novoY = y * b

        plt.plot(novoX, novoY, label="Escala")
        # plt.plot(x, y, label="Original")
        plt.title("Gráfico Escala", fontsize=18)
        plt.legend()
        plt.axis('off')
        plt.show()

    def aplicaReflexao(self, eixo):

        x = np.array([float(self.x.get()), float(self.x2.get())])
        y = np.array([float(self.y.get()), float(self.y2.get())])

        if(eixo == 'x'):

            novoY = -y
            plt.plot(np.round(x), np.round(novoY), label="Reflexão eixo X")

        elif(eixo == 'y'):

            novoX = -x
            plt.plot(np.round(novoX), np.round(y), label="Reflexão eixo Y")

        elif(eixo == 'origem'):
            novoX = -x
            novoY = -y

            plt.plot(np.round(novoX), np.round(novoY), label="Reflexão origem")

        plt.title("Gráfico Reflexão", fontsize=18)
        plt.axis('off')
        plt.legend()
        plt.show()

    def aplicaCisalhamento(self, eixo):

        forca = float(self.inputCisalhamento.get())
        x = np.array([float(self.x.get()), float(self.x2.get())])
        y = np.array([float(self.y.get()), float(self.y2.get())])

        if(eixo == 'x'):
            novoX = x + forca * y
            plt.plot(novoX, y, label="Cisalhamento eixo X")
        elif(eixo== 'y'):
            novoY = y + x * forca
            plt.plot(x, novoY, label="Cisalhamento eixo Y")

        plt.legend()
        plt.axis('off')
        plt.show()

    def aplicaCohen(self):
        x1 = float(self.x.get())
        x2 = float(self.x2.get())
        y1 = float(self.y.get())
        y2 = float(self.y2.get())

        xMin = float(self.xInf.get())
        yMin = float(self.yInf.get())
        xMax = float(self.xSup.get())
        yMax = float(self.ySup.get())

        aceito = False
        feito = False
        xInt = 0
        yInt = 0

        while(not feito):
            cod1 = self.obtemCodigo(x1, y1)
            cod2 = self.obtemCodigo(x2, y2)

            if(cod1 == 0 and cod2 == 0):
                aceito = True
                feito = True

            # se ambas estão fora da janela
            elif ((cod1 & cod2) != 0) : feito = True
            else:
                if(cod1 != 0): cfora = cod1
                else: cfora = cod2

                #Antes da esquerda
                if(self.verificaBit(cfora, 0) == 1):
                    xInt = xMin
                    yInt = y1 + (y2 - y1) * ((xMin - x1)/(x2-x1))
                elif(self.verificaBit(cfora, 1) == 1):
                    xInt = xMax
                    YInt = y1 + (y2 - y1) * ((xMax - x1)/(x2 - x1))
                elif(self.verificaBit(cfora, 2) == 1):
                    yInt = yMin
                    XInt = x1 + (x2 - x1) * ((yMin - y1)/(y2 - y1))
                elif(self.verificaBit(cfora, 3) == 1):
                    yInt = yMax
                    xInt = x1 + (x2 - x1) * ((yMax - y1)/ (y2 - y1))

                if(cfora == cod1):
                    x1 = xInt
                    y1 = yInt
                else:
                    x2 = xInt
                    y2 = yInt
        if(aceito):
            self.aplicaDDA("janela", round(x1), round(y1), round(x2), round(y2))

    def obtemCodigo(self, x, y):
        xMin = float(self.xInf.get())
        yMin = float(self.yInf.get())
        xMax = float(self.xSup.get())
        yMax = float(self.ySup.get())

        cod = 0
        if(x < xMin): cod += 1
        if(x > xMax): cod += 2
        if(y < yMin): cod += 4
        if(y > yMax): cod += 8

        return cod

    def verificaBit(self, cfora, bit):

        if(bit == 0):
            if(cfora == 9 or cfora == 1 or cfora == 5):
                return 1
            else: return 0
        if(bit == 1):
            if(cfora == 10 or cfora == 2 or cfora == 6):
                return 1
            else: return 0
        if(bit == 2):
            if(cfora == 5 or cfora == 4 or cfora == 6):
                return 1
            else: return 0
        if(bit == 3):
            if(cfora ==9 or cfora == 8 or cfora == 10):
                return 1
            else: return 0

    def aplicaLiangBarksy(self):
        x1 = float(self.x.get())
        x2 = float(self.x2.get())
        y1 = float(self.y.get())
        y2 = float(self.y2.get())

        xMin = float(self.xInf.get())
        yMin = float(self.yInf.get())
        xMax = float(self.xSup.get())
        yMax = float(self.ySup.get())

        self.u1 = 0
        self.u2 = 1
        dx = x2 - x1
        dy = y2 - y1

        if(self.cliptest(-dx, x1 - xMin)):
            if(self.cliptest(dx, xMax - x1)):
                if(self.cliptest(-dy, y1 - yMin)):
                    if(self.cliptest(dy, yMax - y1)):
                        if(self.u2 < 1):
                            x2 = x1 + dx * self.u2
                            y2 = y1 + dy * self.u2
                        if(self.u1 > 0):
                            x1 = x1 + dx * self.u1
                            y1 = y1 + dy * self.u1
                        self.aplicaDDA("janela", round(x1), round(y1), round(x2), round(y2))

    def cliptest(self, p, q):
        result = True
        if(p < 0):
            u = q/p
            if(u > self.u2): result = False #Fora da janela
            elif(u > self.u1): self.u1 = u
        elif(p > 0):
            u = q/p
            if(u < self.u1): result = False #Fora da janela
            elif(u < self.u2): self.u2 = u
        return result

    def chamaJanelaePreenchimento(self):
        window = Tk()
        window.resizable(width=False, height=False)
        Outros(window)


class Outros:
    def __init__(self,  master):
        self.fontePadrao = ("Arial", "10")
        self.colors = np.zeros(shape=(50, 50))

        canvas_width = 700
        canvas_height = 300

        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="#ffffff")
        self.canvas.pack()
        self.canvas.configure(scrollregion=(-600,-2400,400,100))

        self.container0= Frame(master, padx=150)
        self.container0.pack()

        self.limpar = Button(self.container0, text="Limpar", width=12, command=self.clear)
        self.limpar.pack(side=RIGHT)

        # Circunferencia
        self.container1 = Frame(master, pady=10)
        self.container1.pack()

        self.container2 = Frame(master, pady=10)
        self.container2.pack()

        self.container3 = Frame(master, pady=10)
        self.container3.pack()

        ####### FIM CONTAINER #######

        #Circunferencia
        self.circun = Label(self.container1, text="Circunferências", fg="blue", font=(self.fontePadrao, "11", "bold"))
        self.circun.pack(side=LEFT)

        self.inputXCircun = Label(self.container2, text="Centro    a ")
        self.inputXCircun.pack(side=LEFT)

        self.xCircun = Entry(self.container2, font=self.fontePadrao, width=5)
        self.xCircun.pack(side=LEFT)

        self.inputYCircun = Label(self.container2, text="b ")
        self.inputYCircun.pack(side=LEFT)

        self.yCircun = Entry(self.container2, font=self.fontePadrao, width=5)
        self.yCircun.pack(side=LEFT)

        self.inputRaioCircun = Label(self.container2, text="raio ")
        self.inputRaioCircun.pack(side=LEFT)

        self.raioCircun = Entry(self.container2, font=self.fontePadrao, width=5)
        self.raioCircun.pack(side=LEFT)

        self.bres = Button(self.container3, text="Bresenham", command=self.aplicaBresenhamCircun, font=("Calibri", "9"), width=10)
        self.bres.pack(side=LEFT)

        self.preenche1 = Button(self.container3, text="Boundary Fill",
                                command=lambda: self.boundaryFill4(self.xCircun.get(), self.yCircun.get(), 1, 3), font=("Calibri", "9"), width=14)
        self.preenche1.pack(side=LEFT, padx=5)

        self.preenche2 = Button(self.container3, text="Flood-Fill", font=("Calibri", "9"), width=14,
                                command=lambda: self.flood4(self.xCircun.get(), self.yCircun.get(), 0, 3))
        self.preenche2.pack(side=LEFT, padx=5)

    def aplicaBresenhamCircun(self):
        x1 = int(self.xCircun.get())
        y1 = int(self.yCircun.get())
        raio = int(self.raioCircun.get())

        x = 0
        y = raio
        p = 3 - 2 * raio
        self.plotaSimetricos(x, y, x1, y1)

        while (x < y):
            if (p < 0):
                p += 4 * x + 6
            else:
                p += 4 * (x - y) + 10
                y = y - 1
            x = x + 1
            self.plotaSimetricos(int(x), int(y), x1, y1)

    def plotaSimetricos(self, a, b, xc, yc):
        self.canvas.create_text((xc + a, yc + b), text=".", tag="line")
        self.canvas.create_text((xc + a, yc - b), text=".", tag="line")
        self.canvas.create_text((xc - a, yc + b), text=".", tag="line")
        self.canvas.create_text((xc - a, yc - b), text=".", tag="line")
        self.canvas.create_text((xc + b, yc + a), text=".", tag="line")
        self.canvas.create_text((xc + b, yc - a), text=".", tag="line")
        self.canvas.create_text((xc - b, yc + a), text=".", tag="line")
        self.canvas.create_text((xc - b, yc - a), text=".", tag="line")

    def boundaryFill4(self, x, y, corBorda, corNova):
        # Color black = 1
        # Color white = 0
        # Color green = 3

        x1 = int(self.xCircun.get())
        y1 = int(self.yCircun.get())
        raio = int(self.raioCircun.get())

        #Converte x e y para inteiros
        x = int(x)
        y = int(y)

        corAtual = self.obtemCor(x, y, x1, y1, raio)

        if(corAtual != corBorda and corAtual != corNova):
            self.canvas.create_text(x, y, text=".", tag="line", fill="#000fff000")
            self.colors[x][y] = 3
            self.boundaryFill4(x + 1, y, corBorda, corNova)
            self.boundaryFill4(x - 1, y, corBorda, corNova)
            self.boundaryFill4(x, y + 1, corBorda, corNova)
            self.boundaryFill4(x, y - 1, corBorda, corNova)

    def obtemCor(self, x, y, x1, y1, raio):

        if ((math.pow(x - x1, 2) + math.pow(y - y1, 2)) >= math.pow(raio, 2)):
            self.colors[x][y] = 1

        return self.colors[x][y]

    def flood4(self, x, y, colorAntiga, colorNova):
        # Color black = 1
        # Color white = 0
        # Color green = 3

        x1 = int(self.xCircun.get())
        y1 = int(self.yCircun.get())
        raio = int(self.raioCircun.get())

        # Converte x e y para inteiros
        x = int(x)
        y = int(y)

        colorAtual = self.obtemCor(x,y,x1, y1, raio)

        if(colorAtual == colorAntiga):
            self.colors[x][y] = colorNova
            self.canvas.create_text(x, y, text=".", tag="line", fill="#000fff000")
            self.flood4(x+1, y, colorAntiga, colorNova)
            self.flood4(x -1, y, colorAntiga, colorNova)
            self.flood4(x, y+1, colorAntiga, colorNova)
            self.flood4(x, y-1, colorAntiga, colorNova)

    def clear(self):
        self.canvas.delete(ALL)
        self.colors = np.zeros(shape=(50, 50))

root = Tk()
root.title("Computação Gráfica")
root.resizable(0,0)
Application(root)
root.mainloop()





