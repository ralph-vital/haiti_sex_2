import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import re
# import snowflake.connector
# import streamlit_option_menu
# from streamlit_option_menu import option_menu

# clean data
sex_df = pd.read_csv('sex_intercourse_subnational_clean.csv', header=0)
sex_df = sex_df[['Location',  'indicateur', 'periode',  'sex','year','Value']]
print(sex_df.head())

text = """The DHS Program Application Programming Interface (API) provides software developers 
          access to aggregated indicator data from The Demographic and Health Surveys (DHS) Program. 
          The API can be used to create various applications to help analyze, visualize, explore and disseminate 
          data on population, health, HIV, and nutrition from more than 90 countries. """


# t1.image('haiti-flag-square.jpg', width=120)
st.title("Sexual Intercourse Indicators in Haiti")
st.markdown(" **tel:** 509 36055983 **| email:** mailto:vitalralph@hotmail.com")
st.markdown(" **data source:** Demographic and Health and Surveys (DHS)")

# disable = False
with st.sidebar:
    st.write('Parameters: ')
    d_option = st.selectbox(
        "Choose a Location",
       list(sex_df['Location'].unique()),
       disabled=True
    )
    # if d_option == 'all':
    #     disable = True
    # else:
    #     disable = False
    #     select_department = price_df[price_df['admin1'] == d_option]
    #     current_data = select_department.sort_values(by=['date'])
    #     select_market_df = select_department['market'].unique()
    #     all_market = select_market_df

    ind_option = st.selectbox(
        "Choose an indicator",
        tuple(sex_df['indicateur'].unique()),
      
    )
    sex_df_ind = sex_df[sex_df['indicateur']==ind_option]
    sex_df_sex = sex_df[sex_df['indicateur']==ind_option]

    sub_option = st.selectbox(
        "Choose a sub indicator",
        tuple(sex_df_ind['periode'].unique()),
    )

    if sub_option is not np.nan:
        sex_flag = False
    else :
        sex_flag = True

    sex_option = st.selectbox(
        "Choose a sex ",
        tuple(sex_df['sex'].unique()),
        disabled=sex_flag
      
    )
    
    year_option = st.selectbox(
        "Choose an indicator",
        tuple(sex_df['year'].unique()),
      
    )


df_200 = sex_df.query('indicateur==@ind_option and year==@year_option')

print(df_200.head())
df_2000 = sex_df.query('periode==@sub_option and year==@year_option')

print(df_2000.head())




if sub_option is not np.nan:
    st.header(f" {ind_option} {sub_option} in {year_option} ")
    data_df = sex_df.query('indicateur==@ind_option and year==@year_option and periode==@sub_option')
    st.bar_chart(data_df, x="Location", y="Value", color="sex", stack=False)        
    print("------")
    print(sub_option)
if sub_option is np.nan:
    st.header(f" {ind_option}  in {year_option} ")
    data_df_2 = sex_df.query('indicateur==@ind_option and year==@year_option')
    st.bar_chart(data_df_2, x="Location", y="Value", stack=False)
# if d_option in all_departement:

#     # Create a row layout
#     c1, c2 = st.columns(2)
#     c3, c4 = st.columns(2)

#    # with st.container():
#    #     c1.write("c1")
#    #     c2.write("c2")

#    # with st.container():
#    #     c3.write("c3")
#    #     c4.write("c4")
#     if p_option == 'HTG':
#         y = "price"
#     else:
#         y = "usdprice"
#     with c1:
#         mais_data = current_data[current_data['commodity']
#                                  == 'Maize meal (local)']
#         unit = mais_data['unit'].unique()[0] if len(
#             mais_data['unit'].unique()) else None
#         c_fig = px.line(mais_data, x='date', y=y,
#                         title=f'Maize meal (local) in {p_option} ({unit})')
#         st.plotly_chart(c_fig)

#     with c4:
#         rice_data = current_data[current_data['commodity']
#                                  == 'Rice (imported)']
#         unit = rice_data['unit'].unique()[0] if len(
#             rice_data['unit'].unique()) else None
#         r_fig = px.line(rice_data, x='date', y=y,
#                         title=f'Rice (imported) in {p_option} ({unit})')
#         st.plotly_chart(r_fig)

#     with c3:
#         wheat_data = current_data[current_data['commodity']
#                                   == 'Rice (local)']
#         unit = wheat_data['unit'].unique()[0] if len(
#             wheat_data['unit'].unique()) else None
#         w_fig = px.line(wheat_data, x='date', y=y,
#                         title=f'Rice (local) in {p_option} ({unit})')
#         st.plotly_chart(w_fig)

#     with c2:
#         m_i_data = current_data[current_data['commodity']
#                                 == 'Maize meal (imported)']
#         unit = m_i_data['unit'].unique()[0] if len(
#             m_i_data['unit'].unique()) else None
#         mi_fig = px.line(m_i_data, x='date', y=y,
#                          title=f'Maize meal (imported) in {p_option} ({unit})')
#         st.plotly_chart(mi_fig)

# st.write("1 marmite ~ 1.1lbs")
# fig_m = px.line(malaria_df, x='YEAR (DISPLAY)', y="Numeric", title=m_title)

# Contact Form

# with st.expander("Contact us", expanded=True):
#     with st.form(key='contact', clear_on_submit=True):

#         email = st.text_input('Contact Email')
#         text = st.text_area(
#             "Query", "Please fill in all the information or we may not be able to process your request")

#         submit_button = st.form_submit_button(label='Send Information')

# if submit_button:
#     st.write(f"{email}")
