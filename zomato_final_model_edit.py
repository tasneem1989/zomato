import pandas as pd
import numpy as np
import joblib
import streamlit as st
import sklearn
import base64

model = joblib.load('zomato_pipeline_pipeline_test1.pkl')
def predict_Target(name, online_order, book_table,rate, votes,
       location, rest_type,cuisines,cost,
       listed_type, listed_city):
    
    prediction = model.predict(pd.DataFrame({'online_order':online_order,
                                             'book_table':book_table,'rate':rate,
                                             'votes':votes,'location':location,
                                             'rest_type':rest_type,
                                             'cuisines':cuisines,
                                             'cost':cost,
                                             'listed_type':listed_type,
                                             'listed_city':listed_city}))
    label=['succsses','not succsses']
        
    return  label[prediction[0]]
    
def main():
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
            )
    #add_bg_from_local("C:\\Users\\tasne\\Downloads\\On.jpg")    
      
    st.title('succsess Prediction')
   
    html_temp = """
        
        <div style='background-color:white'>
        <h2 style="color:red;text-align:center;">resturants succsess</h2>
        </div>
                  """
    
    st.markdown(html_temp,unsafe_allow_html=True)
   
    name=st.text_input('name','name')
    online_order = st.selectbox('online_order',['Yes','No'])
    book_table = st.selectbox('book_table',['Yes','No'])
    rate=st.slider('rate',0,5)
    votes = st.text_input('votes','votes')
    location = st.text_input('location','location')
    rest_type=st.text_input('rest_type','rest_type')
    cuisines = st.text_input('cuisines','cuisines')
    cost=st.slider('cost',100,3000)
    listed_type = st.text_input('listed_type','listed_type')
    listed_city=st.text_input('listed_city','listed_city')               
    result = ""
    if st.button('predict'):
       result = predict_Target(name, online_order, book_table,rate, votes,
                location, rest_type,cuisines, cost,
                listed_type, listed_city)
    st.success('The Target is {} '.format(result)) 

    

if __name__ =='__main__':
    main()
        
