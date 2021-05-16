import pandas as pd
import numpy as np
from datetime import timedelta
import os

file_path=r'.\WHO-COVID-19-global-data_May16_db.csv'
file_path_vaccine=r'.\vaccination-data_May16_db.csv'




df1=pd.read_csv(file_path)
df1_vaccine=pd.read_csv(file_path_vaccine)
column_names=df1.columns.values
column_names_vaccine=df1_vaccine.columns.values
#print(column_names)



metric1=column_names[0] # date_reported
metric2=column_names[2] # Country
metric3=column_names[4] # New cases
metric4=column_names[5] # cumutaltive cases
metric5=column_names[6] # new deaths
metric6=column_names[7] # cumulative deaths

metric1_vaccine=column_names_vaccine[0] # Country

def countries_list():

    countires_list=df1[metric2].tolist()
    countires_list = list(dict.fromkeys(countires_list))

    return countires_list
    
    
def country_data(selected_country):
    df11=pd.DataFrame()
    country_name=[]
   
    
    country_name.append(selected_country)
    ctry_wise_df=df1[df1[metric2].isin(country_name)]

    tmp_x_axis_dates=df1[metric1].tolist()
    tmp_x_axis_dates1=set(tmp_x_axis_dates)
    x_axis_dates_today=sorted(tmp_x_axis_dates1)
    x_axis_dates=x_axis_dates_today[0:len(x_axis_dates_today)-1]
    c_day1=[]
    c_day1.append(x_axis_dates[-1])
    c_day1.append(x_axis_dates[-2])
    c_day1.append(x_axis_dates[-3])

   

    df11=ctry_wise_df[ctry_wise_df[metric1].isin(c_day1)]

   
    
    selected_country_data_for_html=[]

    if df11.shape[0]>1:
        tmp_rows=[]
        tmp_rows.append(df11.iloc[2].tolist())
        tmp_rows.append(df11.iloc[1].tolist())
        tmp_rows.append(df11.iloc[0].tolist())
    
        
        for i in tmp_rows:
            tmp_selected_country_data_for_html_row={'Date':i[0],'Country_Name':i[2],'New_Cases':f'{i[4]:,}','Cummulative_Cases':f'{i[5]:,}','New_Deaths':f'{i[6]:,}','Cummulative_Deaths':f'{i[7]:,}'}
            selected_country_data_for_html.append(tmp_selected_country_data_for_html_row)

    return selected_country_data_for_html
    
    
def vaccine_data(selected_country):
    df11_vaccine=pd.DataFrame()
    country_name_vaccine=[]
    vaccine_data_for_country={}
    
    country_name_vaccine.append(selected_country)
    ctry_wise_df_vaccine=df1_vaccine[df1_vaccine[metric1_vaccine].isin(country_name_vaccine)]
    if ctry_wise_df_vaccine.shape[0]>0:
        i=ctry_wise_df_vaccine.iloc[0].tolist()
        
        vaccine_data_for_country={'Reported Till Date':i[4],'Country Name ':i[0],'Total Vaccines Given: ':f'{i[5]:,}','Persons Vaccinated 1+ Dose':f'{i[6]:,}','Total Vaccination Per 100 People':i[7],'Total Vaccinations of 1+ Dose per 100 ':i[8],'Types of Vaccines Used':i[9]}
        
    return vaccine_data_for_country
    
