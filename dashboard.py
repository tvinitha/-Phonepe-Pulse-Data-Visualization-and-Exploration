import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
# from PIL import Image

 # Connect to MySQL server    
mydb = sql.connect(host="localhost",
                   user="root",
                   password="*****",
                   database= "Phonepe"
                  )
mycursor = mydb.cursor(buffered=True)

st.set_page_config(page_title= "Phonepe Pulse Data Visualization |by vinitha",
                   
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *vinitha*!
                                        Data has been cloned from Phonepe Pulse Github Repository"""})


# Display a title
st.markdown(f'<h1 style="text-align: center;">PhonePe Pulse Data Visualization and Exploration</h1>', unsafe_allow_html=True)
# Creating option menu in the side bar

selected = option_menu( options=["Home","Data Overview","Top Charts","Explore Data","About"], 
                icons=["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                menu_title=None,
                default_index=0,
                orientation="horizontal",
                styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px"},
                         "nav-link-selected": {"background-color": "purple"}                         }
)
     
        
if selected == "Home":
    col1,col2 = st.columns(2,gap= 'medium')
    col1.markdown("## :blue[Domain] : Fintech")
    col1.markdown("## :blue[Technologies used] : Github Cloning, Python, Pandas, MySQL,mysql-connector-python, Streamlit, and Plotly")
    col1.markdown("## :clipboard: Problem Statement:")
    col1.markdown("### :The Phonepe pulse Github repository contains a large amount of data related to various metrics and statistics. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.")
    col2.markdown("#   ")
    col2.markdown("#   ")
    col2.markdown("#   ")

if selected == "Data Overview":
        st.write('')
        st.header('PhonePe Pulse Data: Insights for India')
        st.write('')

        st.subheader('Key Dimensions:')
        st.write('- State - All States in India')
        st.write('- Year -  2018 to 2022')
        st.write('- Year -  2018 to 2023')
        st.write('- Quarter - Q1 (Jan to Mar), Q2 (Apr to June), Q3 (July to Sep), Q4 (Oct to Dec)')

        st.subheader('Aggregated Transaction:')
        st.write('Transaction data broken down by type of payments at state level.')
        st.write('- Recharge & bill payments')
        st.write('- Peer-to-peer payments')
        st.write('- Merchant payments')
        st.write('- Financial Services')
        st.write('- Others')
        st.subheader('Aggregated User:')
        st.write('Users data broken down by devices at state level.')
        col1,col2,col3,col4, col5, col6 = st.columns(6)
        with col1:
                st.write(':small_blue_diamond: Apple')
                st.write(':small_blue_diamond: Asus')
                st.write(':small_blue_diamond: Coolpad')
                st.write(':small_blue_diamond: Gionee')
                st.write(':small_blue_diamond: HMD Global')
        with col2:
                st.write(':small_blue_diamond: Huawei')
                st.write(':small_blue_diamond: Infinix')
                st.write(':small_blue_diamond: Lava')
                st.write(':small_blue_diamond: Lenovo')
                st.write(':small_blue_diamond: Lyf')
        with col3:
                st.write(':small_blue_diamond: Micromax')
                st.write(':small_blue_diamond: Motorola')
                st.write(':small_blue_diamond: OnePlus')
                st.write(':small_blue_diamond: Oppo')
                st.write(':small_blue_diamond: Realme')
        with col4:
                st.write(':small_blue_diamond: Samsung')
                st.write(':small_blue_diamond: Tecno')
                st.write(':small_blue_diamond: Vivo')
                st.write(':small_blue_diamond: Xiaomi')
                st.write(':small_blue_diamond: Others')
        st.subheader('Map Transaction:')
        st.write('- Total number of transactions at the state / district level.')
        st.write('- Total value of all transactions at the state / district level.')
        st.subheader('Map User:')
        st.write('- Total number of registered users at the state / district level.')
        st.write('- Total number of app opens by these registered users at the state / district level.')
        st.subheader('Top Transaction:')
        st.write('Explore the most number of the transactions happened for a selected Year-Quarter combination')
        st.write('- Top 10 States')
        st.write('- Top 10 Districts')
        st.write('- Top 10 Pincodes')
        st.subheader('Top User:')
        st.write('Explore the most number of registered users for a selected Year-Quarter combination')
        st.write('- Top 10 States')
        st.write('- Top 10 Districts')
        st.write('- Top 10 Pincodes')
         
# TOP CHARTS
if selected == "Top Charts":
    st.markdown("## :green[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    with colum1:
        Year=st.selectbox('**Year**',('2018','2019','2020','2021','2022'))
        Quarter=st.selectbox('**Quarter**',('1','2','3','4'))
        # Year = st.slider("**Year**", min_value=2018, max_value=2022)
        # Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with colum2:
        st.info(
                """
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )       
        
    # Top Charts - TRANSACTIONS    
    if Type == "Transactions":
        col1,col2,col3 = st.columns([1,1,1],gap="small")
        
        with col1:
            st.markdown("### :green[Top 10 State]")
            mycursor.execute(f"select state, sum(transaction_count) as Total_Transactions_Count, sum(transaction_amount) as Total from aggregated_transaction where year = {Year} and quater= {Quarter} group by state order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['state', 'transactions_Count','transaction_amount'])
            fig = px.pie(df, values='transaction_amount',
                             names='state',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Viridis,
                             hover_data=['transactions_Count'],
                             labels={'transactions_Count':'transactions_Count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col2:
            st.markdown("### :green[Top 10 District]")
            mycursor.execute(f"select district , sum(transaction_count) as Total_Count, sum(transaction_amount) as Total from map_transaction where year = {Year} and quater = {Quarter} group by district order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['district', 'transactions_count','transaction_amount'])

            fig = px.pie(df, values='transaction_amount',
                             names='district',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['transactions_count'],
                             labels={'transactions_count':'transactions_count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col3:
            st.markdown("### :green[Top 10 Pincode]")
            mycursor.execute(f"select pincode, sum(transaction_count) as Total_Transactions_Count, sum(transaction_amount) as Total from top_transaction where year = {Year} and quater= {Quarter} group by pincode order by Total desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['pincode', 'transactions_count','transaction_amount'])
            fig = px.pie(df, values='transaction_amount',
                             names='pincode',
                            #  title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Viridis,
                             hover_data=['transactions_count'],
                             labels={'transactions_count':'transactions_count'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

    # Top Charts - USERS          
    if Type == "Users":
        col1,col2,col3,col4 = st.columns([2,2,2,2],gap="small")
        
        with col1:
            st.markdown("### :green[Brands]")
            if Year == 2022 and Quarter in [2,3,4]:
                st.markdown("#### Sorry No Data to Display for 2022 Qtr 2,3,4")
            else:
                mycursor.execute(f"SELECT user_brand, SUM(user_count) AS total_user_count, AVG(user_percentage) * 100 AS avg_user_percentage FROM aggregated_user WHERE year = {Year} AND quater = {Quarter} GROUP BY user_brand ORDER BY total_user_count DESC LIMIT 10")
                df = pd.DataFrame(mycursor.fetchall(), columns=['user_brand', 'total_user_count', 'avg_user_percentage'])

                import plotly.express as px
                fig = px.bar(
                    df,
                    title='Top 10 User Brands',
                    x="total_user_count",
                    y="user_brand",
                    orientation='h',
                    color='avg_user_percentage',
                    color_discrete_sequence=px.colors.sequential.Viridis)

                fig.update_layout(xaxis_title='Total User Count', yaxis_title='User Brand')
                st.plotly_chart(fig, use_container_width=True)
   
    
        with col2:
            st.markdown("### :green[District]")
            mycursor.execute(f"select district, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user where year = {Year} and quater= {Quarter} group by district,registered_user order by Total_Users  desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['district', 'registered_user','app_opens'])
            df.registered_user = df.registered_user.astype(float)
            fig = px.bar(df,
                         title='Top 10',
                         x="registered_user",
                         y="district",
                         orientation='h',
                         color='registered_user',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
              
        with col3:
            st.markdown("### :green[Pincode]")
            mycursor.execute(f"select pincode, sum(registered_user) as Total_Users from top_user where year = {Year} and quater= {Quarter} group by pincode order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['pincode', 'registered_user'])
            fig = px.pie(df,
                         values='registered_user',
                         names='pincode',
                         title='Top 10',
                         color_discrete_sequence=px.colors.sequential.Viridis,
                         hover_data=['registered_user'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
        with col4:
            st.markdown("### :green[State]")
            mycursor.execute(f"select state, sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user where year = {Year} and quater= {Quarter} group by state order by Total_Users desc limit 10")
            df = pd.DataFrame(mycursor.fetchall(), columns=['state', 'registered_user','app_opens'])
            fig = px.pie(df, values='registered_user',
                             names='state',
                             title='Top 10',
                             color_discrete_sequence=px.colors.sequential.Agsunset,
                             hover_data=['app_opens'],
                             labels={'app_opens':'app_opens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
            
            
# EXPLORE DATA
if selected == "Explore Data":
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    colum1,colum2= st.columns([1,1.5],gap="large")
    
    Year = st.sidebar.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    
    col1,col2= st.columns(2)   
     #EXPLORE DATA - Transactions   
    if Type == "Transactions":     
        # Overall State Data - TRANSACTIONS AMOUNT - INDIA MAP 
        with col1:
            st.markdown("## :violet[Overall State Data - Transactions Amount]")
            mycursor.execute(f"select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction where year = {Year} and quater= {Quarter} group by state order by state")
            df1 = pd.DataFrame(mycursor.fetchall(),columns= ['state', 'Total_Transactions', 'Total_amount'])
            df2 = pd.read_csv('state_names.csv')
            # df1.transaction_amount = df1.transaction_amount.astype(int )
            df1['state'] = df2['state']
            
            
            fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='state',
                        color='Total_amount',
                        color_continuous_scale='sunset')

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig,use_container_width=True)
            
            with col2:
            
                st.markdown("## :violet[Overall State Data - Transactions count]")
                mycursor.execute(f"select state, sum(transaction_count) as Total_Transactions, sum(transaction_amount) as Total_amount from map_transaction where year = {Year} and quater= {Quarter} group by state order by state")
                df1 = pd.DataFrame(mycursor.fetchall(),columns= ['state', 'Total_Transactions', 'Total_amount'])
                df2 = pd.read_csv('state_names.csv')
                # df1.transaction_count = df1.transaction_count.astype(int )
                df1['state'] = df2['state']
                
                
                fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='state',
                            color='Total_Transactions',
                            color_continuous_scale='sunset')

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig,use_container_width=True)
                
               
            # BAR CHART - TOP PAYMENT TYPE
            st.markdown("## :violet[Top Payment Type]")
            mycursor.execute(f"select transaction_type, sum(transaction_count) as Total_Transactions_count, sum(transaction_amount) as Total_Transactions_amount from aggregated_transaction where year= {Year} and quater = {Quarter} group by transaction_type order by Transaction_type")
            df = pd.DataFrame(mycursor.fetchall(), columns=['transaction_type', 'Total_Transactions_count','Total_Transactions_amount'])

            fig = px.bar(df,
                        title='Transaction Types vs Total_Transactions',
                        x="transaction_type",
                        y="Total_Transactions_count",
                        orientation='v',
                        color='Total_Transactions_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=False) 
            
            # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
            st.markdown("# ")
            st.markdown("# ")
            st.markdown("# ")
            st.markdown("## :violet[Select any State to explore more]")
            selected_state = st.selectbox("",
                                ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
            
            mycursor.execute(f"select state, district,year,quater, sum(transaction_count) as Total_Transactions_count, sum(transaction_amount) as Total_transaction_amount from map_transaction where year = {Year} and quater = {Quarter} and state = '{selected_state}' group by state, district,year,quater order by state,district")
            
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['state','district','year','quater',
                                                            'Total_Transactions_count','Total_transaction_amount'])
            fig = px.bar(df1,
                        title=selected_state,
                        x="district",
                        y="Total_Transactions_count",
                        orientation='v',
                        color='Total_transaction_amount',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
        
    
    # EXPLORE DATA - USERS      
    if Type == "Users":
        
        # Create a Streamlit title
            st.markdown("## :violet[Overall State Data - User App Opening Frequency]")            
            mycursor.execute(f"SELECT state, SUM(registered_user) AS Total_Users, SUM(app_opens) AS Total_Appopens FROM map_user WHERE year = {Year} AND quater = {Quarter} GROUP BY state ORDER BY state")
            df1 = pd.DataFrame(mycursor.fetchall(), columns=['state', 'Total_Users', 'Total_Appopens'])
            df2 = pd.read_csv('state_names.csv')   
            df1['Total_Appopens'] = df1['Total_Appopens'].astype(float)
            df1['state'] = df2['state']
            fig = px.choropleth(
                df1,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM',
                locations='state',
                color='Total_Appopens',
                color_continuous_scale='sunset'
            )
            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)
            
            # BAR CHART TOTAL UERS - DISTRICT WISE DATA 
            st.markdown("## :violet[Select any State to explore more]")
            selected_state = st.selectbox("",
                                ('andaman-&-nicobar-islands','andhra-pradesh','arunachal-pradesh','assam','bihar',
                                'chandigarh','chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu','delhi','goa','gujarat','haryana',
                                'himachal-pradesh','jammu-&-kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep',
                                'madhya-pradesh','maharashtra','manipur','meghalaya','mizoram',
                                'nagaland','odisha','puducherry','punjab','rajasthan','sikkim',
                                'tamil-nadu','telangana','tripura','uttar-pradesh','uttarakhand','west-bengal'),index=30)
                
            mycursor.execute(f"select state,year,quater,district,sum(registered_user) as Total_Users, sum(app_opens) as Total_Appopens from map_user where year = {Year} and quater = {Quarter} and state = '{selected_state}' group by state, district,year,quater order by state,district")
            
            df = pd.DataFrame(mycursor.fetchall(), columns=['State','year', 'quater', 'district', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(int)
            
            fig = px.bar(df,
                        title=selected_state,
                        x="district",
                        y="Total_Users",
                        orientation='v',
                        color='Total_Users',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)

    
 
# MENU 4 - ABOUT
if selected == "About":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[About PhonePe Pulse:] ")
        st.write("##### BENGALURU, India, On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")
        
        st.write("##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")
        
        st.markdown("### :violet[About PhonePe:] ")
        st.write("##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")
        
        st.write("**:violet[My Project GitHub link]** ⬇️")
        st.write("https://github.com/tvinitha/-Phonepe-Pulse-Data-Visualization-and-Exploration.git")
              
    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")                

        
        


