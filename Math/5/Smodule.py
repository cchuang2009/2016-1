import numpy as np
from scipy.stats import t,norm
from ipy_table import make_table,apply_theme,set_cell_style,set_column_style,set_row_style
import ipywidgets as widgets
from IPython.display import clear_output, display
from tabulate import tabulate

def ordinalData(tabledata, category=['A','B','C','D','E']):
    n=len(tabledata)
    Span_data=np.array([])
    for k in range(n+1):
      if k==0:
         column_ex= np.append(np.array(['Y\X']),category)
         column_ex= np.append(column_ex,'Total')   
         #column_ex= np.append(np.array([' \ ']),category)   
         Span_data=np.append(Span_data,column_ex)
      else:
         Sdata=np.array([category[-k]])
         total=  np.sum(tabledata[-k]) 
         Sdata=np.append(Sdata,tabledata[-k])
         Sdata=np.append(Sdata,total)   
         Span_data=np.append(Span_data,Sdata)
    # sum for each pre-Category data        
    Span_data= np.append(Span_data,'Total')        
    Span_data= np.append(Span_data,np.sum(tabledata,axis=0))
    Span_data= np.append(Span_data,np.sum(tabledata))        
    Span_data=Span_data.reshape([n+2,n+2])
    
    return Span_data

def senssonRP(tabledata):
    AvgX=np.sum(tabledata,axis=0)
    AvgX=AvgX/sum(AvgX)
    AvgY=np.sum(tabledata,axis=1)
    AvgY=AvgY/sum(AvgY)
    CX=np.zeros(len(AvgX))
    for i in range(len(AvgX)-1):
        CX[len(AvgX)-i-1]=sum(AvgX[:len(AvgX)-i-1])
    CY=np.zeros(len(AvgY))
    for i in range(len(AvgY)-1):
        CY[len(AvgY)-i-1]=sum(AvgY[:len(AvgY)-i-1])
    RP=sum(AvgY*CX-AvgX*CY)
    
    return RP

def senssonRV(tabledata):
    
    n=len(tabledata[0])
    RX=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            RX[i][j]=np.sum(tabledata[:i][:n])+sum(tabledata[i][:j])+(1+tabledata[i][j])/2
    RY0=np.zeros([n,n])
    tabledata1=tabledata.transpose()
    for i in range(n):
        for j in range(n):
            RY0[i][j]=np.sum(tabledata1[:i][:n])+sum(tabledata1[i][:j])+(1+tabledata1[i][j])/2
    RY=RY0.transpose() 
    RV=np.sum((RX-RY)*(RX-RY)*tabledata)/np.sum(tabledata)**3*6
    return RV

def RPJackknife(tabledata):
    n=len(tabledata)
    tt=np.array([])
    for i in range(n):
        for j in range(n):
            tt=np.append(tt,senssonRP(np.delete(np.delete(tabledata,j,1),i,0)))
    return tt.reshape([n,n])      

def RVJackknife(tabledata):
    n=len(tabledata)
    tt=np.array([])
    for i in range(n):
        for j in range(n):
            tt=np.append(tt,senssonRV(np.delete(np.delete(tabledata,j,1),i,0)))
    return tt.reshape([n,n])      

def SvenssonRPCIs(tabledata,p=0.95):
    RP=senssonRP(tabledata)
    RPJ=RPJackknife(tabledata)
    pp=norm.ppf((1+p)/2, loc=0)
    a=RP-pp*RPJ.std()/np.sqrt(len(tabledata[0])**2)
    b=RP+pp*RPJ.std()/np.sqrt(len(tabledata[0])**2)
    if int(p*100) == float(p*100):
       decimals = 0
    else:
       decimals = 1 # Assumes 2 decimal places for money

    print('{0:.{1}f}'.format(p*100, decimals),"% confidence interval of RP, ",'{0:.{1}f}'.format(RP, 3),":")
    print(" CIs:  (%.3f,%.3f)" %(a,b))
    print(O+'\n--[----------- ○ -----------]--'+W)
    print(" %.3f     %0.3f     %.3f " %(a,RP,b))
    if (RP<0):
        result="Toward the Lower A"
    else:
        result="Toward the Upper E"
    print("\nConclusion: %s" %result)

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[1;33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

T =  '\033[1;33;47m' #Title


def SvenssonRVCIs(tabledata,p=0.95):
    RV=senssonRV(tabledata)
    RVJ=RVJackknife(tabledata)
    pp=norm.ppf((1+p)/2, loc=0)
    a=RV-pp*RVJ.std()/np.sqrt(len(tabledata[0])**2)
    b=RV+pp*RVJ.std()/np.sqrt(len(tabledata[0])**2)
    if int(p*100) == float(p*100):
       decimals = 0
    else:
       decimals = 1 # Assumes 2 decimal places for money

    print(T+' {0:.{1}f}'.format(p*100, decimals),"% confidence interval of RV, ",'{0:.{1}f}'.format(RV, 3),":"+W)
    print(" CIs:  (%.3f,%.3f)" %(a,b))
    print(B+'\n--[----------- ○ -----------]--'+W)
    print(" %.3f       %0.3f       %.3f " %(a,RV,b))
    if (RV<0.2):
        result="Individual Variation is small"
    elif (RV<0.6):
        result="Individual Variation has to be concerned"
    else:
        result="Individual Variation is ver large"
    print("\nConclusion: %s" %result)    
    
def SvenssonTable(tabledata):
    Sdata=ordinalData(tabledata)
    n=len(tabledata)
    make_table(Sdata)

    apply_theme('basic_both')
    set_cell_style(0,0, thick_border='left,top')
    #set_cell_style(0, 0, color='lightblack')
    set_column_style(0, color='lightgray')
    for i in range(1,n+1):
        set_cell_style(i,n+1-i, thick_border='all',color="lightbrown")

    return set_cell_style(0, 0, color='orange')  

def InputData():
    import ipywidgets as widgets
    AA = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    AB = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    AC = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    AD = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    AE = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    BA = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    BB = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    BC = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    BD = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    BE = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    CA = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    CB = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    CC = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    CD = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    CE = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    DA = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    DB = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    DC = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    DD = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    DE = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    EA = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    EB = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    EC = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    ED = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)
    EE = widgets.IntText(value=0, layout=widgets.Layout(width='15%'), disabled=False)

    XY = widgets.Box([widgets.Label(value=' Y\X ')], layout=widgets.Layout(width='3%'))
    S  = widgets.Box([widgets.Label(value='  ')],   layout=widgets.Layout(width='7%')) 
    A0  = widgets.Box([widgets.Label(value=' A ')],   layout=widgets.Layout(width='15%')) 
    B0  = widgets.Box([widgets.Label(value=' B ')],   layout=widgets.Layout(width='15%'))
    C0  = widgets.Box([widgets.Label(value=' C ')],   layout=widgets.Layout(width='15%'))   
    D0  = widgets.Box([widgets.Label(value=' D ')],   layout=widgets.Layout(width='15%'))
    E0  = widgets.Box([widgets.Label(value=' E ')],   layout=widgets.Layout(width='15%'))
    A1  = widgets.Box([widgets.Label(value=' A ')],   layout=widgets.Layout(width='3%')) 
    B1  = widgets.Box([widgets.Label(value=' B ')],   layout=widgets.Layout(width='3%'))
    C1  = widgets.Box([widgets.Label(value=' C ')],   layout=widgets.Layout(width='3%'))   
    D1  = widgets.Box([widgets.Label(value=' D ')],   layout=widgets.Layout(width='3%'))
    E1  = widgets.Box([widgets.Label(value=' E ')],   layout=widgets.Layout(width='3%')) 
    
    alphaTitle = widgets.Box([widgets.Label(value=' α ')], layout=widgets.Layout(width='3%'))
    alphaVal= widgets.FloatText(value=0.95, layout=widgets.Layout(width='15%'), disabled=False)
    button1=widgets.Button(description='Submit',disabled=False,
          button_style='',tooltip='Calculate',icon='check')
    button1.style.button_color = 'lightblue'

    def on_button_clicked(b):
        tabledata=np.array([[AA.value,AB.value,AC.value,AD.value,AE.value],
                    [BA.value,BB.value,BC.value,BD.value,BE.value],
                    [CA.value,CB.value,CC.value,CD.value,CE.value],
                    [DA.value,DB.value,DC.value,DD.value,DE.value],
                    [EA.value,EB.value,EC.value,ED.value,EE.value]])
        #Sdata=ordinalData(tabledata)
        #print(tabulate(Sdata))    
        display(SvenssonTable(tabledata))
        SvenssonRPCIs(tabledata,p=alphaVal.value)
        SvenssonRVCIs(tabledata,p=alphaVal.value)
        clear_output(True)

    button1.on_click(on_button_clicked)

    return widgets.VBox(
             [widgets.HBox([XY,S,A0,B0,C0,D0,E0]),
              widgets.HBox([A1,AA,AB,AC,AD,AE]),widgets.HBox([B1,BA,BB,BC,BD,BE]),
              widgets.HBox([C1,CA,CB,CC,CD,CE]),widgets.HBox([D1,DA,DB,DC,DD,DE]),
              widgets.HBox([E1,EA,EB,EC,ED,EE]),
              widgets.HBox([alphaTitle, alphaVal, button1])
             ])