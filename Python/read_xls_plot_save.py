# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


path = 'D:\DATA\GEOSPATIAL\ADHOC ANALYSIS\Papua\Concessions'
os.chdir(path)

papua = pd.ExcelFile('summary.xlsx')

p_summary = papua.parse('summary').drop(17)

def plot():
    fig, ax = plt.subplots(figsize=(9,6))
    barWidth = 0.8
    cc = ['#16280f', '#efffe5', '#007406', '#c8b400', '#16f00f', '#ff151b', '#95ff3f', '#ffff63', '#7c500e']
    pivot = p_summary.pivot_table(index='group', columns='class_variable', values='percentage', aggfunc='sum')
    pivot.plot(kind='bar', stacked=True, legend=False, ax=ax, zorder=10, color=cc, width=barWidth)
    
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y/100))) 
              
    ax.set_xlabel('')
    ax.set_xticklabels('')
    ax.tick_params(
            axis='both',
            which='both',
            bottom=False,
            top=False,
            left=False)
    ax.set_ylabel('Prosentase terhadap Papua Barat*')
    ax.set_yticks(ticks=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    
    # Change font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'
    
    ax.tick_params(axis='both', which='major', labelsize=12)

    # change the axis spines's style
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')

    # set the spines position
    ax.spines['bottom'].set_position(('axes', 0))
    ax.spines['left'].set_position(('axes', 0.015))
    ax.yaxis.grid(linestyle='-', color='#d9d9d9', zorder=1, alpha=0.5)
   
plot()
# save to a file
plt.savefig('summary.svg', format='svg')