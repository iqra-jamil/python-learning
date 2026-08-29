# Methods or functions provided by streamlit(without rendring HTML tags)
- st.title() - to display main /bold heading at the top of web page(at the top of app)
- st.header()- also use to display large /bold heading at the top section
- st.text()-to display plain text with fixed width 
- st.write()-its like all in one ,it can handle numbers,text,dataframes ,charts evrything
- st.selectbox()- to display dropdown
- st.sucess() - to display sucess msg
- st.dataframe() requires a oandas df or numpy array
# Explore more on : https://docs.streamlit.io/develop/api-reference/text

# Widgets- Interactive UI elements like button,slider,input field etc.
- Streamlit supports the icon names wrapped in :material/icon_name: syntax to display icons in your app.
- like :material/thumb_down:
practiced few 
# explore more at : https://docs.streamlit.io/develop/api-reference/widgets

# Layouts and containers :
- without layouts and containers ,elements will be stack vertcally
- streamlit's layouts and contaners help us to organize UI
- we can place elements side by side ,place them together ,tabs
- basiaclly streamlit's layouts and containers allow us to convert a simple app into production ready app
# explore more at : https://docs.streamlit.io/develop/api-reference/layout

#  why we use markdown
# differ between markdown and write
# why we use with statemnt
its a context manager 
we use to insert elments in to layout containers like sidebar,tabs,col etc


# Data elements
we can use stream lit with pandas or numpy for data handling
# explore more at : https://docs.streamlit.io/develop/api-reference/data