# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:50:00 2018

Funktionen zur Veranschaulichung des Inversion von Zeigern
plot_cplx_plane - Darstellung der komplexen Ebene
plot_cplx_number - Darstellung von komplexen Zahlen in der komplexen Ebene
plot_sum_cplx_number - Darstellung der Zeigersumme
plot_invers - Darstellung der inversen Richtung
plot_hline - Darstellung der Lotlinie
plot_tangente - Darstellung der Tangenten
plot_result - Darstellung der invertierten Zeigers

@author: Admin_1
@date: 16.01.2018
"""


import matplotlib.pyplot as plt
import numpy as np

def plot_cplx_plane_et(limits=[-5,5,-5,5], radius=1):
    """
    Darstellung der komplexen Ebene
    Parameter: 
        limits - Grenzen (default [-5,5,-5,5])
        radius - Radius des Inversionskreises
    Rückgabe:
        hw - Breite der Zeigerspitze
        hl - Länge der Zeigerspitze
    """
    # erzeugt neue Figur
    fig=plt.figure(1)
    #setzt die Größe der Figur
    plt.axis(limits)
    hw=(limits[1]-limits[0])/100
    hl=(limits[1]-limits[0])/50
    # Auswahl einer Teilfigur (111 ... ganze Figur)
    #ax=fig.add_subplot(1,1,1)

    # Einheitskreis erzeugen
    circ=plt.Circle((0,0), radius=radius, color='b', fill=False, ls='dashed')
    plt.arrow(limits[0], 0, 2*limits[1], 0, length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')
    plt.arrow(0, limits[2], 0, 2*limits[3], length_includes_head=True, head_width=hw, head_length=hl, fc='k', ec='k')

    # Objekte in Figur einbauen  
    #ax.add_patch(circ)
    plt.gcf().gca().add_artist(circ)

    # Gitternetz und Beschriftung
    plt.grid()
    plt.title('Komplexe Ebene')
    plt.xlabel('Realteil')
    plt.ylabel('j*Imaginärteil')

    return (hw, hl)

def plot_sum_cplx_number(data=[], limits=[-5,5,-5,5], radius=1):
    """
    Darstellung der Summe von komplexen Zahlen in der komplexen Ebene
    Aufruf:
        plot_cplx_number(data=[], limits=[-5,5,-5,5])
    Parameter: 
        data - Liste der darzustellenden komplexen Zahlen
        limits - Grenzen (default [-5,5,-5,5])
    Rückgabe:
        cn_real - Realteil des Summenzeigers
        cn_imag - Imaginärteil des Summenzeigers
        hl - Breite der Zeigerspitze
        hw - Länge der Zeigerspitze
    """
    # Erzeugen einer komplexen Ebene
    hw, hl = plot_cplx_plane_et(limits=limits,radius=radius)
    # Verabeitung aller komplexen Zahlen der Eingabeliste
    cn_real0 = data[0].real
    cn_imag0 = data[0].imag
    plt.arrow(0, 0, cn_real0, cn_imag0, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r', ls='dotted')
    for k in range(1, len(data)):
        cn_real = data[k].real
        cn_imag = data[k].imag
        if (abs(cn_real)+abs(cn_imag) != 0):
            plt.arrow(cn_real0, cn_imag0, cn_real, 
                           cn_imag, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r', ls='dotted')
        cn_real0 = cn_real0 + data[k].real
        cn_imag0 = cn_imag0 + data[k].imag
    plt.arrow(0, 0, cn_real0, 
                   cn_imag0, length_includes_head=True, head_width=hw, head_length=hl, fc='b', ec='b')
    return(cn_real0, cn_imag0, hl, hw)

def plot_invers(hl, hw, data=[], limits=[]):
    """
    Darstellung der Inversionsgeraden einer komplexen Zahlen in der komplexen Ebene
    Aufruf:
        plot_invers(data=[], fig)
    Parameter: 
        hl - Breite der Zeigerspitze
        hw - Länge der Zeigerspitze
        data - Liste der zu invertierende komplexen Zahlen
        limits - Grenzen (default [-5,5,-5,5])
    Rückgabe:
        fig    
    """
    m = - data[0].imag/data[0].real
    p1 = limits[0]
    p2 = m * limits[0]
    p3 = limits[1]
    p4 = m * limits[1]
    plt.plot([p1, p3], [p2, p4], ls='dotted')
    plt.arrow(0, 0, data[0].real, 
                   -data[0].imag, length_includes_head=True, head_width=hw, head_length=hl, fc='r', ec='r', ls='dotted')
    

def plot_hline(data=[], limits=[]):
    """
    Darstellung der senkrechten Hilfsgerade auf der Inversionsgeraden in der komplexen Ebene
    Aufruf:
        plot_line(fig, data=[], limits=[])
    Parameter: 
        data - zu invertierende komplexe Zahl
        limits - Grenzen der Darstellung
    Rückgabe:
        m, n - Parameter der Hilfsgeraden
    """
    m =  data[0].real/data[0].imag
    n =  - data[0].imag - m * data[0].real
    p1 = limits[0]
    p2 = m * limits[0] + n
    p3 = limits[1]
    p4 = m * limits[1] + n
    plt.plot([p1, p3], [p2, p4], ls='dotted')
    
    return(m, n)

def plot_tangente(m, n, radius=1, limits=[]):
    """
    Darstellung der Tangenten in der komplexen Ebene
    Aufruf:
        plot_tangente(fig, m, n, radius=radius, limits=limits)
    Parameter: 
        m, n - Parameter der Hilfsgeraden
        limits - Grenzen der Darstellung
        radius - Radius des Inversionskreises
    Rückgabe:
        fig, m1, n1    
    """
    x1 = 1/(1+m**2)*(-m*n + np.sqrt(m**2*n**2+(radius**2-n**2)*(1+m**2)))
    x2 = 1/(1+m**2)*(-m*n - np.sqrt(m**2*n**2+(radius**2-n**2)*(1+m**2)))
    y1 = m * x1 + n
    y2 = m * x2 + n
    m1 = -x1/y1
    m2 = -x2/y2
    n1 = y1 - m1 * x1
    n2 = y2 - m2 * x2
    p1 = limits[0]
    p21 = m1 * limits[0] + n1
    p3 = limits[1]
    p41 = m1 * limits[1] + n1
    p22 = m2 * limits[0] + n2
    p42 = m2 * limits[1] + n2
    plt.plot([p1, p3], [p21, p41], ls='--', color = 'k')
    plt.plot([p1, p3], [p22, p42], ls='--', color = 'k')

    return(m1, n1)

def plot_tangente_first(data=[], radius=1, limits=[]):
    """
    Darstellung der Tangenten in der komplexen Ebene
    Aufruf:
        plot_tangente_first(data[], radius=radius, limits=limits)
    Parameter: 
        data[] - zu invertierender Zeiger
        limits - Grenzen der Darstellung
        radius - Radius des Inversionskreises
    Rückgabe:
        fig, m1, n1    
    """
    x1 = data[0].real
    y1 = - data[0].imag         
    m1 = x1 * y1 /(x1**2 - radius**2) + np.sqrt((x1 * y1 /(x1**2 - radius**2))**2 - 
                          (y1**2 -radius**2)/(x1**2 - radius**2))
    n1 = y1 - m1 * x1

    m2 = x1 * y1 /(x1**2 - radius**2) - np.sqrt((x1 * y1 /(x1**2 - radius**2))**2 - 
                          (y1**2 -radius**2)/(x1**2 - radius**2))
    n2 = y1 - m2 * x1
    xt1 = - n1 / (m1 + 1/m1)
    xt2 = - n2 / (m2 + 1/m2)
    yt1 = m1 * xt1 + n1
    yt2 = m2 * xt2 + n2

    p1 = limits[0]
    p21 = m1 * limits[0] + n1
    p3 = limits[1]
    p41 = m1 * limits[1] + n1
    p22 = m2 * limits[0] + n2
    p42 = m2 * limits[1] + n2
    plt.plot([p1, p3], [p21, p41], ls='--', color = 'k')
    plt.plot([p1, p3], [p22, p42], ls='--', color = 'k')
    
    return(xt1, yt1, xt2, yt2)

def plot_hline_second(m, n, limits=[]):
    """
    Darstellung der senkrechten Hilfsgerade auf der Inversionsgeraden in der komplexen Ebene
    Aufruf:
        plot_line_second(m, n, limits=[])
    Parameter: 
        m, n - Parameter der Hilfslinie
        limits - Grenzen der Darstellung
    Rückgabe:
    """
    p1 = limits[0]
    p2 = m * limits[0] + n
    p3 = limits[1]
    p4 = m * limits[1] + n
    plt.plot([p1, p3], [p2, p4], ls='dotted')
    

def plot_result(m, n, hl, hw, data=[]):
    """
    Darstellung des invertierten Zeigers in der komplexen Ebene
    Aufruf:
        plot_result(m, n, hl, hw, data=[])
    Parameter: 
        m, n - Parameter der Tangente
        hl, hw - Daten für Zeigerspitzen
        data - zu invertierender Zeiger
    Rückgabe:
        fig    
    """
    mz = - data[0].imag/data[0].real
    xr = n/(mz -m)
    yr = mz * xr
    plt.arrow(0, 0, xr, 
                   yr, length_includes_head=True, head_width=hw, 
                   head_length=hl, fc='g', ec='g', ls='-', lw=2)
    
def test_numbers(radius, z1, z2):

    if z1.real == radius:
        r = z1.real + 0.001 * z1.real
        i = z1.imag
        z1 = complex(r,i)
    if z2.real == radius:
        r = z2.real + 0.001 * z2.real
        i = z2.imag
        z2 = complex(r,i)
    if z1.imag == radius:
        r = z1.real
        i = z1.imag + 0.001 * z1.imag
        z1 = complex(r,i)
    if z2.imag == radius:
        r = z2.real
        i = z2.imag + 0.001 * z2.imag
        z2 = complex(r,i)

    if z1.real == 0.5 * radius:
        r = z1.real + 0.001 * z1.real
        i = z1.imag
        z1 = complex(r,i)
    if z2.real == 0.5 * radius:
        r = z2.real + 0.001 * z2.real
        i = z2.imag
        z2 = complex(r,i)
    if z1.imag == 0.5 * radius:
        r = z1.real
        i = z1.imag + 0.001 * z1.imag
        z1 = complex(r,i)
    if z2.imag == 0.5 * radius:
        r = z2.real
        i = z2.imag + 0.001 * z2.imag
        z2 = complex(r,i)
    
    return(z1,z2)

