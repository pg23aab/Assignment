#!/usr/bin/env python3

# Importing the required libraries and modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading the data using pandas
df = pd.read_csv('final_2014_pred.csv')
lenCountries = len(df.country)

def teamSort(match):
    '''
    This function sorts the team based on request (semi/ quarter)

    Parameters
    ----------
    match : "semi/ quarter".

    Returns
    -------
    teamList : Final teams list.

    '''
    teamList = []
    for i in range (0, len(df.country)):
        if int(df[match][i]) == 1:
            teamList.append(df.country[i])
    return teamList

def SPI(country):
    
    '''
    This function returns the SPI of the countries requested to.
    
    Parameters
    ----------
    country : countries we need to extract the spi data from.

    Returns
    -------
    spi : total soccer prediction index of the country.
    spiOff : Offensive soccer prediction index of the country.
    spiDef : Defensive soccer prediction index of the country.

    '''
    spi = []
    spiOff = []
    spiDef = []
    for i in range (0, lenCountries - 1):
        for j in range (0, (len(country))):
            if df.country[i] == country[j]:
                spi.append(df.spi[i])
                spiOff.append(df.spi_offence[i])
                spiDef.append(df.spi_defence[i])
    return spi, spiOff, spiDef

def barPlotSpi(country, X, Y1, Y2):
    '''
    This function plots the bar plot of the data.

    Parameters
    ----------
    country : Countries we need to plot the Bar plot.
    X : spi value of the respective countries.
    Y1 : offensive spi value of the respective countries.
    Y2 : defensive spi value of the respective countries.

    Returns
    -------
    None.

    '''
    fig, ax = plt.subplots(figsize =(10, 7))
    xAxis = np.arange(len(country))  
    plt.bar(xAxis - 0.15, Y1, 0.3, label = 'Spi offence') 
    plt.bar(xAxis + 0.15, Y2, 0.3, label = 'Spi Defence')
    plt.xticks(xAxis, country) 
    plt.xlabel("Country") 
    plt.ylabel("SPI(Soccer Prediction Index)") 
    plt.title("offence and defence SPI for Quarter finalist 2014 world cup") 
    plt.legend() 
    plt.show()
    
def linePlotSPI(X, Y):
    '''
    This function plots the Line plot of the data.

    Parameters
    ----------
    X : Countries that we are using the SPI.
    Y : spi value of the respective countries.

    Returns
    -------
    None.

    '''
    plt.plot(X, Y, label = "SPI", linewidth = "4") 
    plt.xlabel("Country Team")
    plt.ylabel ("Soccer Prediction Index (SPI)")
    plt.title("SPI for Semi finalist 2014 world cup") 
    plt.legend() 
    plt.show()
    
def pieChart(X, Y):
    '''
    This function plots the Pie chart of the data.

    Parameters
    ----------
    X : Countries that we are using the SPI.
    Y : spi value of the respective countries.

    Returns
    -------
    None.

    '''
    explode = (0.05, 0.0, 0.2, 0.02)
    colors = ("orange", "cyan", "blue", "yellow") 
    wedge = {'linewidth' : 1,'edgecolor' : "red" }
    fig, ax = plt.subplots(figsize =(10, 7))
    plt.pie(Y, labels = Y, explode = explode,wedgeprops = wedge,shadow = True, colors = colors)
    plt.legend(X, title = "Teams", loc = "right")
    plt.title("Semi Finalists Prediction visualisation using SPI")
    plt.show()
    
# We now sort the team based on Semi Finalist and Quarter Finalist
semiFinalist = teamSort("semi")
quarterFinalist = teamSort("quarter")

# Now we find the SPI for Quarter and Semi finalist
spiQuar, spioffenceQuar, spidefenceQuar = SPI(quarterFinalist)
spiSemi, spioffenceSemi, spidefenceSemi = SPI(semiFinalist)

# Bar plot visualisation
barPlotSpi(quarterFinalist, spiQuar, spioffenceQuar, spidefenceQuar)

# Line plot visualisation
linePlotSPI(semiFinalist, spiSemi)

# Pie chart Graph visualisation
pieChart(semiFinalist, spiSemi)
