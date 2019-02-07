# -*- coding: utf-8 -*-

#import tools as st
import xlrd
import numpy as np
from scipy import integrate
import pylab as pl
from scipy import signal
import tkinter
from tkinter.filedialog import FileDialog
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import math as math
import xlsxwriter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import MouseEvent
from matplotlib.figure import Figure
from biosppy import storage
from biosppy.signals import ecg

def xlread(xls, planilha):
    """
    Gerador que le arquivo .xls
    """
    # Para i de zero ao numero de linhas da planilha
    for i in range(planilha.nrows):
        # Lê os valores nas linhas da planilha
        if i == 8000:
            break
        yield planilha.row_values(i)

# Função para marcação dos pontos no ECG
def onclickx(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))
    if click[0] != 0:
        pontos.append(int(event.xdata))
    click[0] += 1

def onclicky(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))
    if click[0] != 0:
        pontos.append(int(event.xdata))
    click[0] += 1

def onclickz(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))
    if click[0] != 0:
        pontos.append(int(event.xdata))
    click[0] += 1

arq = open('pacientes.txt', 'r')
texto = arq.readlines()

def xlwrite(worksheet, pmtr):
    for i in range(5):
        worksheet.write(i, 1, pmtr[i])

for paciente in texto:
    paciente = paciente[:len(paciente)-1]

    # Abre o arquivo
    workbook = xlsxwriter.Workbook("Parametros_Frank_"+paciente+".xlsx")
    # Abre planilha
    worksheet = workbook.add_worksheet()
    # Classificação das colunas
    worksheet.write('A1', 'SM_QRS_Tangle')
    worksheet.write('A2', 'SP_QRS_Tangle')
    worksheet.write('A3', 'elevation_angle_P')
    worksheet.write('A4', 'azimuth_angle P')
    worksheet.write('A5', 'SVG')

    # Abre o arquivo
    xls = xlrd.open_workbook(paciente+".xlsx")
    # Pega a primeira planilha do arquivo
    planilha = xls.sheets()[0]

    click = [0]*1
    pontos = []
    planx = []
    plany = []
    planz = []

    for linha in xlread(xls, planilha):
        planx.append(float(linha[12]))
        plany.append(float(linha[13]))
        planz.append(float(linha[14]))
    """
    b, a = signal.butter(4, 0.2)
    vectorx = signal.lfilter(b,a,planx)
    vectory = signal.lfilter(b,a,plany)
    vectorz = signal.lfilter(b,a,planz)

    b, a = signal.butter(2, 0.2, 'lowpass')
    #vectorx = signal.lfilter(b,a,planx)
    #vectory = signal.lfilter(b,a,plany)
    vectorz = signal.lfilter(b,a,planz)

    b, a = signal.butter(2, 0.00134, 'highpass')
    vectorx = signal.lfilter(b,a,planx)
    vectory = signal.lfilter(b,a,plany)
    vectorz = signal.lfilter(b,a,planz)

    b, a = signal.butter(4, [0.1, 0.134], 'bandstop')
    vectorx = signal.lfilter(b,a,vectorx)
    vectory = signal.lfilter(b,a,vectory)
    vectorz = signal.lfilter(b,a,vectorz)

    b, a = signal.butter(2, [0.001, 0.11], 'bandpass') # frequência da função = 2*f(hz)/fs
    #vectorx = signal.lfilter(b,a,planx)
    vectory = signal.lfilter(b,a,plany)
    #vectorz = signal.lfilter(b,a,planx)

    b, a = signal.butter(2, [0.001, 0.2], 'bandpass')
    vectorx = signal.lfilter(b,a,planx)

    b, a = signal.butter(2, [0.0005, 0.2], 'bandpass')
    vectorz = signal.lfilter(b,a,planz)

    b, a = signal.butter(4, [0.1, 0.134], 'bandstop')
    vectorx = signal.lfilter(b,a,vectorx)
    vectory = signal.lfilter(b,a,vectory)
    vectorz = signal.lfilter(b,a,vectorz)

    b, a = signal.butter(10, [0.014, 0.02], 'bandstop')
    vectorx = signal.lfilter(b,a,vectorx)
    vectory = signal.lfilter(b,a,vectory)
    vectorz = signal.lfilter(b,a,vectorz)
    """
    vectorx = ecg.ecg(planx, 1000)
    vectory = ecg.ecg(plany, 1000)
    vectorz = ecg.ecg(planz, 1000)

    """
    planx = np.array(planx)
    plany = np.array(plany)
    planz = np.array(planz)

    sampling_rate = float(1000)

    # filter signal
    order = int(0.3 * sampling_rate)
    vectorx, _, _ = st.filter_signal(signal=planx,ftype='FIR',band='bandpass',order=order,frequency=[3, 45],sampling_rate=sampling_rate)
    """
    N = len(vectorx[1]) # Salva em N o tamanho do sinal ECG

    # Salvando as derivacoes em listas - Fim

    # Marcação dos Pontos ECG - Começo

    print("\nVetor X de Frank:\n")

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ts = np.linspace(0, 8000, N, endpoint=False)
    aux = list(ts)
    ax.plot(ts,vectorx[1],lw=2)

    cid = fig.canvas.mpl_connect('button_press_event', onclickx)

    plt.grid()
    plt.ylim(-3,3)
    plt.show()
    fig.canvas.mpl_disconnect(cid)

        # vectory

    print("\nVetor Y de Frank:\n")

    click = [0]*1

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ts = np.linspace(0, 8000, N, endpoint=False)
    aux = list(ts)
    ax.plot(ts,vectory[1],lw=2)

    cid = fig.canvas.mpl_connect('button_press_event', onclicky)

    plt.grid()
    plt.ylim(-3,3)
    plt.show()
    fig.canvas.mpl_disconnect(cid)

        # vectorz

    print("\nVetor Z de Frank:\n")

    click = [0]*1

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ts = np.linspace(0, 8000, N, endpoint=False)
    aux = list(ts)
    ax.plot(ts,vectorz[1],lw=2)

    cid = fig.canvas.mpl_connect('button_press_event', onclickz)

    plt.grid()
    plt.ylim(-3,3)
    plt.show()
    fig.canvas.mpl_disconnect(cid)

    vetorx = []
    vetory = []
    vetorz = []
    ondaPx = []
    ondaPy = []
    ondaPz = []
    QRSx = []
    QRSy = []
    QRSy1 = []
    QRSz = []
    QRSz1 = []
    ondaTx = []
    ondaTy = []
    ondaTy1 = []
    ondaTz = []
    ondaTz1 = []

    k = min(pontos)-100

    while k<=max(pontos)+50:
        vetorx.append(vectorx[1][k])
        vetory.append(vectory[1][k])
        vetorz.append(vectorz[1][k])
        if k < pontos[0]:
            ondaPx.append(vectorx[1][k])
            ondaPy.append(vectory[1][k])
            ondaPz.append(vectorz[1][k])
        if k >= pontos[0] and k <= pontos[2]:
            QRSx.append(vectorx[1][k])
            QRSy1.append(vectory[1][k])
            QRSz1.append(vectorz[1][k])
        if k >= pontos[3] and k <= pontos[5]:
            ondaTx.append(vectorx[1][k])
            ondaTy1.append(vectory[1][k])
            ondaTz1.append(vectorz[1][k])
        if k >= pontos[6] and k <= pontos[8]:
            QRSy.append(vectory[1][k])
        if k >= pontos[9] and k <= pontos[11]:
            ondaTy.append(vectory[1][k])
        if k >= pontos[12] and k <= pontos[14]:
            QRSz.append(vectorz[1][k])
        if k >= pontos[15] and k <= pontos[17]:
            ondaTz.append(vectorz[1][k])

        k += 1

    # Marcação dos Pontos ECG - Fim

    # Plotagem do Vector - Começo

    #pontoMedioX = int((pontos[5]+pontos[0])/2) #Alterado!!
    #pontoMedioY = int((pontos[11]+pontos[6])/2)
    #pontoMedioZ = int((pontos[17]+pontos[12])/2)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(vetorz, vetorx, vetory, color='Black', markersize=10)
    ax.plot(ondaPz, ondaPx, ondaPy, color='Green', label='Onda P', markersize=10)
    ax.plot(QRSz1, QRSx, QRSy1, color='Red', label='QRS', markersize=10)
    ax.plot(ondaTz1, ondaTx, ondaTy1, color='Blue', label='Onda T', markersize=10)
    #ax.scatter(vectorz[1][pontoMedioZ], vectorx[1][pontoMedioX], vectory[1][pontoMedioY], color='Orange', marker='X')

    ax.set_xlabel("Z - vectorz")
    ax.set_ylabel("X - Vectorx")
    ax.set_zlabel("Y - Vectory")

    ax.set_xlim3d(max(vectorz[1]), min(vectorz[1]))
    ax.set_ylim3d(min(vectorx[1]), max(vectorx[1]))
    ax.set_zlim3d(max(vectory[1]), min(vectory[1]))

    ax.legend()
    plt.show()
    
    # Plotagem do Vector - Fim

    # Plotagem dos planos - Começo

    # xy:

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(vetorx,vetory,lw=2, color='Blue')
    #ax.plot(ondaPx, ondaPy, color='Green', label='P Wave', markersize=10)
    #ax.plot(QRSx, QRSy1, color='Red', label='QRS', markersize=10)
    #ax.plot(ondaTx, ondaTy1, color='Blue', label='T Wave', markersize=10)

    ax.legend()
    ax.set_xlabel("Vx")
    ax.set_ylabel("Vy")
    plt.grid()
    plt.ylim(min(vetory)-2,max(vetory)+2)
    plt.show()

    # xz:

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(vetorx,vetorz,lw=2, color='Blue')
    #ax.plot(ondaPx, ondaPz, color='Green', label='P Wave', markersize=10)
    #ax.plot(QRSx, QRSz1, color='Red', label='QRS', markersize=10)
    #ax.plot(ondaTx, ondaTz1, color='Blue', label='T Wave', markersize=10)

    ax.legend()
    ax.set_xlabel("Vx")
    ax.set_ylabel("Vz")
    plt.grid()
    plt.ylim(min(vetorz)-2,max(vetorz)+2)
    plt.show()

    # yz:

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(vetory,vetorz,lw=2, color='Blue')
    #ax.plot(ondaPy, ondaPz, color='Green', label='P Wave', markersize=10)
    #ax.plot(QRSy1, QRSz1, color='Red', label='QRS', markersize=10)
    #ax.plot(ondaTy1, ondaTz1, color='Blue', label='T Wave', markersize=10)

    ax.legend()
    ax.set_xlabel("Vy")
    ax.set_ylabel("Vz")
    plt.grid()
    plt.ylim(min(vetorz)-2,max(vetorz)+2)
    plt.show()

    # Plotagem dos planos - Fim

    # Vetores QRS e T - Começo

    ts1 = np.linspace(0, QRSx[len(QRSx)-1], len(QRSx), endpoint=False)
    ts2 = np.linspace(0, QRSy[len(QRSy)-1], len(QRSy), endpoint=False)
    ts3 = np.linspace(0, QRSz[len(QRSz)-1], len(QRSz), endpoint=False)
    ts4 = np.linspace(0, ondaTx[len(ondaTx)-1], len(ondaTx), endpoint=False)
    ts5 = np.linspace(0, ondaTy[len(ondaTy)-1], len(ondaTy), endpoint=False)
    ts6 = np.linspace(0, ondaTz[len(ondaTz)-1], len(ondaTz), endpoint=False)

    Area_QRSx = integrate.simps(QRSx, ts1, 'avg')
    Area_QRSy = integrate.simps(QRSy, ts2, 'avg')
    Area_QRSz = integrate.simps(QRSz, ts3, 'avg')

    Area_ondaTx = integrate.simps(ondaTx, ts4, 'avg')
    Area_ondaTy = integrate.simps(ondaTy, ts5, 'avg')
    Area_ondaTz = integrate.simps(ondaTz, ts6, 'avg')

    """
    Area_QRSx = 0
    Area_QRSy = 0
    Area_QRSz = 0
    Area_ondaTx = 0
    Area_ondaTy = 0
    Area_ondaTz = 0

    for i in range(len(QRSx)):
            Area_QRSx = Area_QRSx + QRSx[i]
            Area_QRSy = Area_QRSy + QRSy[i]
            Area_QRSz = Area_QRSz + QRSz[i]
    for i in range(len(ondaTx)):
            Area_ondaTx = Area_ondaTx + ondaTx[i]
            Area_ondaTy = Area_ondaTy + ondaTy[i]
            Area_ondaTz = Area_ondaTz + ondaTz[i]
    """

    moduloQRS = math.sqrt(Area_QRSx**2+Area_QRSy**2+Area_QRSz**2)
    moduloT = math.sqrt(Area_ondaTx**2+Area_ondaTy**2+Area_ondaTz**2)

    SM_QRS_Tangle = math.acos((Area_QRSx*Area_ondaTx + Area_QRSy*Area_ondaTy + Area_QRSz*Area_ondaTz)/(moduloQRS*moduloT))*180/math.pi
    SVGm = math.sqrt((Area_QRSx+Area_ondaTx)**2+(Area_QRSy+Area_ondaTy)**2+(Area_QRSz+Area_ondaTz)**2)
    """
    pontoMedioX = int((pontos[1]+pontos[4])/2) #Alterado!!
    pontoMedioY = int((pontos[7]+pontos[10])/2)
    pontoMedioZ = int((pontos[13]+pontos[16])/2)
    """
    RPx = vectorx[1][pontos[1]]#-vectorx[1][pontoMedioX] #Alterado!!
    RPy = vectory[1][pontos[7]]#-vectory[1][pontoMedioY]
    RPz = vectorz[1][pontos[13]]#-vectorz[1][pontoMedioZ]
    TPx = vectorx[1][pontos[4]]#-vectorx[1][pontoMedioX]
    TPy = vectory[1][pontos[10]]#-vectory[1][pontoMedioY]
    TPz = vectorz[1][pontos[16]]#-vectorz[1][pontoMedioZ]

    moduloRP = math.sqrt(RPx**2+RPy**2+RPz**2)
    moduloTP = math.sqrt(TPx**2+TPy**2+TPz**2)

    SP_QRS_Tangle = math.acos((RPx*TPx+RPy*TPy+RPz*TPz)/(moduloRP*moduloTP))*180/math.pi
    projectionSVG = math.sqrt((Area_QRSx+Area_ondaTx)**2+(Area_QRSz+Area_ondaTz)**2)
    elevation_angleP = math.acos(((Area_QRSx+Area_ondaTx)**2+(Area_QRSz+Area_ondaTz)**2)/(SVGm*projectionSVG))*180/math.pi
    azimuth_angleP = 180-math.acos(((Area_QRSx+Area_ondaTx)**2)/((Area_QRSx+Area_ondaTx)*projectionSVG))*180/math.pi #Alterado!!

    pmtr = []
    pmtr.append(SM_QRS_Tangle); pmtr.append(SP_QRS_Tangle); pmtr.append(elevation_angleP); pmtr.append(azimuth_angleP); pmtr.append(SVGm);
    xlwrite(worksheet, pmtr)

    # Novos Parâmetros Tereshchenko - Começo
    """
    moduloVector = math.sqrt(Vectorx**2+Vectory**2+Vectorz**2)
    PI = moduloVector/moduloQRS

    QRSMAXx = vectorx[pontos[4]] - vectorx[pontos[3]]
    QRSMAXy = vectory[pontos[13]] - vectorx[pontos[12]]
    QRSMAXz = vectorz[pontos[22]] - vectorx[pontos[21]]

    moduloQRSMAX = moduloVector = math.sqrt(QRSMAXx**2+QRSMAXy**2+QRSMAXz**2)

    RI = moduloQRS/moduloQRSMAX
    """
        # Novos Parâmetros Tereshchenko - Fim

    print('\nSM_QRS_Tangle = %f°\n' %SM_QRS_Tangle)
    print('SP_QRS_Tangle = %f°\n' %SP_QRS_Tangle)
    print('elevation_angle_P = %f°\n' %elevation_angleP)
    print('azimuth_angle P = %f°\n' %azimuth_angleP)
    print('SVG = %f mV\n' %SVGm)
    #print('PI = %f \n' %PI)
    #print('RI = %f \n' %RI)

    # Vetores QRS e T - Fim

    workbook.close()
