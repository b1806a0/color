import os
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
import streamlit as st
#import japanize_matplotlib

def app():

    #日本語文字化け対策でフォント指定　　-！! Web表示すると効かないエラー
    #sns.set(font='Yu Gothic')
    #plt.rcParams['font.family'] = "Yu Gothic"

    st.title("トレーニング結果 | Training Result")

    #streamlitでの表示データのフィルタリング（まだ未装。とりあえず１を手動で作成。集計→表示を自動化できないと辛い。）
    choose_id = st.selectbox("表示するデータを選択して下さい", (
        "ALL", "2022", "2023"))

    #choose_id = st.selectbox('Choose ID', df2, help = 'Filter report to show only one')
    if choose_id == '2023':
        st.write('2023年の結果を表示')
    if choose_id == '2022':
        st.write('2022年の結果を表示')
    if choose_id == 'ALL':
        st.write('ALLの結果を表示')


    #kwd個別に切り出して可視化していく
    
    #streamlit表示
    st.header("Q1：愛らしい| Lovely)")

    #streamlitで選択色トップ５を表示
    st.subheader("上位選択色 | Top Colors")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q1-1', '#FFB8E6')
        st.write(color)

    with col2:
        color = st.color_picker('Q1-2', '#FFE8F6')
        st.write(color)

    with col3:
        color = st.color_picker('Q1-3', '#FF88D5')
        st.write(color)

    with col4:
        color = st.color_picker('Q1-4', '#FFB9B8')
        st.write(color)

    with col5:
        color = st.color_picker('Q1-5', '#FF58C4')
        st.write(color)
            
    #PBIで作成したツリーマップの画像
    st.subheader("トレーニング参加者全体の選択色 | All")
    st.image("airashii.treemap.bmp")
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
    
    #streamlit表示
    st.header("Q2：楽しい(fun)")
    
    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        color = st.color_picker('Q2-1', '#FFFF26')
        st.write(color)

    with col2:
        color = st.color_picker('Q2-2', '#FFFF00')
        st.write(color)

    with col3:
        color = st.color_picker('Q2-3', '#FF6100')
        st.write(color)

    with col4:
        color = st.color_picker('Q2-4', '#FFB954')
        st.write(color)
    with col5:
        color = st.color_picker('Q2-5', '#FF7F1A')
        st.write(color)
    with col6:
        color = st.color_picker('Q2-6', '#FFA511')
        st.write(color)
    with col7:
        color = st.color_picker('Q2-7', '#FF0000')
        st.write(color)       
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料） 
    st.subheader("トレーニング参加者全体の選択色")
    st.image("tanoshii.treemap.png")  
   

    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")



    st.header("Q3：豪華な(gorgeous)")

    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)


    with col1:
        color = st.color_picker('Q3-1', '#FF0000')
        st.write(color)
    with col2:
        color = st.color_picker('Q3-2', '#FFFF00')
        st.write(color)
    with col3:
        color = st.color_picker('Q3-3', '#FF00A2')
        st.write(color)
    with col4:
        color = st.color_picker('Q3-4', '#000000')
        st.write(color)
    with col5:
        color = st.color_picker('Q3-5', '#FFFF26')
        st.write(color)       
    with col6:
        color = st.color_picker('Q4-6', '#FF2A22')
        st.write(color)
    with col7:
        color = st.color_picker('Q4-7', '#D30000')
        st.write(color)   
        
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("goukana.treemap.bmp")        
        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")



    st.header("Q4：素朴な(simple)")

    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q4-1', '#DBDBDB')
        st.write(color)
    with col2:
        color = st.color_picker('Q4-2', '#463700')
        st.write(color)
    with col3:
        color = st.color_picker('Q4-3', '#FFF1E7')
        st.write(color)
    with col4:
        color = st.color_picker('Q4-4', '#FFFFFF')
        st.write(color)
    with col5:
        color = st.color_picker('Q4-5', '#656565')
        st.write(color)
        
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q4-6', '#FFD4B7')
        st.write(color)
    with col2:
        color = st.color_picker('Q4-7', '#FFF1B6')
        st.write(color)
    with col3:
        color = st.color_picker('Q4-8', '#EAFFB6')
        st.write(color)
    with col4:
        color = st.color_picker('Q4-9', '#B2B2B2')
        st.write(color)       
    with col5:
        color = st.color_picker('Q4-10', '#656565')
        st.write(color)
    with col6:
        color = st.color_picker('Q4-11', '#656500')
        st.write(color)
     
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")    
    st.image("sobokuna.treemap.bmp")   
    
 
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

        

    st.header("Q5：味わい深い(tasteful)")

    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q5-1', '#656565')
        st.write(color)
    with col2:
        color = st.color_picker('Q5-2', '#A2A300')
        st.write(color)
    with col3:
        color = st.color_picker('Q5-3', '#D35000')
        st.write(color)
    with col4:
        color = st.color_picker('Q5-4', '#D37600')
        st.write(color)
    with col5:
        color = st.color_picker('Q5-5', '#003232')
        st.write(color)
        
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        color = st.color_picker('Q5-1', '#A43E00')
        st.write(color)
    with col2:
        color = st.color_picker('Q5-2', '#A38000')
        st.write(color)
    with col3:
        color = st.color_picker('Q5-3', '#650000')
        st.write(color)
    with col4:
        color = st.color_picker('Q5-4', '#003232')
        st.write(color)
 
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料） 
    st.subheader("トレーニング参加者全体の選択色")
    st.image("ajiwai.treemap.bmp")        

                   
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

                   
                   
                   

    st.header("Q6：格調のある(dignified)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q6-1', '#FFFF00')
        st.write(color)
    with col2:
        color = st.color_picker('Q6-2', '#D1D300')
        st.write(color)
    with col3:
        color = st.color_picker('Q6-3', '#650000')
        st.write(color)
    with col4:
        color = st.color_picker('Q6-4', '#D30000')
        st.write(color)
    with col5:
        color = st.color_picker('Q6-5', '#A40000')
        st.write(color)        
    with col6:
        color = st.color_picker('Q6-6', '#750000')
        st.write(color)
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("kakucho.treemap.bmp")        
        

    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

                   
                   


    st.header("Q7：優雅な(graceful)")
 

    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        color = st.color_picker('Q7-1', '#A40066')
        st.write(color)
    with col2:
        color = st.color_picker('Q7-2', '#FFFFFF')
        st.write(color)
    with col3:
        color = st.color_picker('Q7-3', '#E4B7FF')
        st.write(color)
    with col4:
        color = st.color_picker('Q7-4', '#87EAFF')
        st.write(color)
                                
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        color = st.color_picker('Q7-5', '#7F00D4')
        st.write(color)
    with col2:
        color = st.color_picker('Q7-6', '#750000')
        st.write(color)
    with col3:
        color = st.color_picker('Q7-7', '#B9BFFF')
        st.write(color)
    with col4:
        color = st.color_picker('Q7-8', '#58B1FF')
        st.write(color)                               
                                
                               
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")    
    st.image("yuuga.treemap.bmp")
    

    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

                   
                   

    #!(8) 気品のある

    st.header("Q8：気品のある(elegant)")

    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q8-1', '#FFFFFF')
        st.write(color)
    with col2:
        color = st.color_picker('Q8-2', '#750049')
        st.write(color)
    with col3:
        color = st.color_picker('Q8-3', '#460076')
        st.write(color)
    with col4:
        color = st.color_picker('Q8-4', '#BF55FF')
        st.write(color)
    with col5:
        color = st.color_picker('Q8-5', '#FFFFB5')
        st.write(color)                                   
    with col6:
        color = st.color_picker('Q8-6', '#000000')
        st.write(color)    
                                
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("kihin.treemap.bmp") 


    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

                  
                  

    st.header("Q9：合理的な(reasonable)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        color = st.color_picker('Q9-1', '#0000D5')
        st.write(color)
    with col2:
        color = st.color_picker('Q9-2', '#000000')
        st.write(color)
    with col3:
        color = st.color_picker('Q9-3', '#FF2A22')
        st.write(color)
    with col4:
        color = st.color_picker('Q9-4', '#FFFFFF')
        st.write(color)                            
    with col5:
        color = st.color_picker('Q9-5', '#FFFF00')
        st.write(color) 
    with col6:
        color = st.color_picker('Q9-6', '#0085FF')
        st.write(color)
    with col7:
        color = st.color_picker('Q9-7', '#7F7F7F')
        st.write(color)                                
   

    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("gouriteki.treemap.bmp")
        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")




    st.header("Q10：春(spring)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q10-1', '#FFB8E6')
        st.write(color)
    with col2:
        color = st.color_picker('Q10-2', '#FFE8F6')
        st.write(color)
    with col3:
        color = st.color_picker('Q10-3', '#FFFFB5')
        st.write(color)
    with col4:
        color = st.color_picker('Q10-4', '#FFB9B8')
        st.write(color)
    with col5:
        color = st.color_picker('Q10-5', '#BDFFB6')
        st.write(color) 

        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("spring.treemap.bmp")        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
     

                                
                                

    st.header("Q11：夏(summer)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q11-1', '#FFFF00')
        st.write(color)
    with col2:
        color = st.color_picker('Q11-2', '#00CFFF')
        st.write(color)
    with col3:
        color = st.color_picker('Q11-3', '#17D9FF')
        st.write(color)
    with col4:
        color = st.color_picker('Q11-4', '#55E1FF')
        st.write(color)
    with col5:
        color = st.color_picker('Q11-5', '#FF0000')
        st.write(color)                            
    with col6:
        color = st.color_picker('Q11-6', '#FF6100')
        st.write(color) 
                                
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("summer.treemap.bmp")


    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
    

                                

    st.header("Q12：秋(autumn)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q12-1', '#A35C00')
        st.write(color)
    with col2:
        color = st.color_picker('Q12-2', '#D37600')
        st.write(color)
    with col3:
        color = st.color_picker('Q12-3', '#A43E00')
        st.write(color)
    with col4:
        color = st.color_picker('Q12-4', '#A40000')
        st.write(color)
    with col5:
        color = st.color_picker('Q12-5', '#750000')
        st.write(color) 
    with col6:
        color = st.color_picker('Q12-6', '#755C00')
        st.write(color) 
                                
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("autumn.treemap.bmp")
        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
     

                                
                                

    st.header("Q13：冬(winter)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        color = st.color_picker('Q13-1', '#FFFFFF')
        st.write(color)
    with col2:
        color = st.color_picker('Q13-2', '#0055A4')
        st.write(color)
    with col3:
        color = st.color_picker('Q13-3', '#DBDBDB')
        st.write(color)
    with col4:
        color = st.color_picker('Q13-4', '#000347')
        st.write(color)
    with col5:
        color = st.color_picker('Q13-5', '#E7FBFF')
        st.write(color)   
    with col6:
        color = st.color_picker('Q13-5', '#B7F2FF')
        st.write(color)   
        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")    
    st.image("winter.treemap.bmp")
        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
 

    #!朝(morning)
    df_morning = df[df['kwd'] == 'morning']

    df_morning_count = df_morning[['count',"col_sum"]].groupby("col_sum").count()

    df_morning_count.plot.bar(by=["col_sum", "count"], xlabel="選択色", ylabel="選択数", figsize=(10, 5),legend=False);

    st.header("Q14：朝(morning)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        color = st.color_picker('Q14-1', '#B7F2FF')
        st.write(color)
    with col2:
        color = st.color_picker('Q14-2', '#E7FBFF')
        st.write(color)
    with col3:
        color = st.color_picker('Q14-3', '#FFFFB5')
        st.write(color)
    with col4:
        color = st.color_picker('Q14-4', '#FF2A22')
        st.write(color)
    with col5:
        color = st.color_picker('Q14-5', '#FFF1B6')
        st.write(color)   
    with col6:
        color = st.color_picker('Q14-6', '#FF9B56')
        st.write(color)
    with col7:
        color = st.color_picker('Q14-7', '#FFB954')
        st.write(color)                                



    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("morning.treemap.bmp")
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
      

    
    st.header("Q15：昼(midday)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q15-1', '#FF9000')
        st.write(color)
    with col2:
        color = st.color_picker('Q15-2', '#FFFF83')
        st.write(color)
    with col3:
        color = st.color_picker('Q15-3', '#FF7F1A')
        st.write(color)
    with col4:
        color = st.color_picker('Q15-4', '#FF6100')
        st.write(color)
    with col5:
        color = st.color_picker('Q15-5', '#FFFF00')
        st.write(color)   


    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("midday.treemap.bmp")        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")


 
                                

                 
    st.header("Q16：夕(sunset)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q16-1', '#FF6100')
        st.write(color)
    with col2:
        color = st.color_picker('Q16-2', '#D35000')
        st.write(color)
    with col3:
        color = st.color_picker('Q16-3', '#FF9000')
        st.write(color)
    with col4:
        color = st.color_picker('Q16-4', '#D37600')
        st.write(color)
    with col5:
        color = st.color_picker('Q16-5', '#FFA511')
        st.write(color) 


    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("sunset.treemap.bmp")        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
     


    
    st.header("Q17：夜(night)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q17-1', '#000000')
        st.write(color)
    with col2:
        color = st.color_picker('Q17-2', '#000347')
        st.write(color)
    with col3:
        color = st.color_picker('Q17-3', '#000032')
        st.write(color)
    with col4:
        color = st.color_picker('Q17-4', '#000276')
        st.write(color)
    with col5:
        color = st.color_picker('Q17-5', '#FFFF00')
        st.write(color) 

    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("night.treemap.bmp")
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")

                  

                                

    st.header("Q18：好きな色(favorite)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q18-1', '#FFB8E6')
        st.write(color)
    with col2:
        color = st.color_picker('Q18-2', '#FFFFFF')
        st.write(color)
    with col3:
        color = st.color_picker('Q18-3', '#000000')
        st.write(color)
    with col4:
        color = st.color_picker('Q18-4', '#E4B7FF')
        st.write(color)
    with col5:
        color = st.color_picker('Q18-5', '#55E1FF')
        st.write(color) 

    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("favorite.treemap.bmp") 

    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")
 

    #1選択時に追加で表示（とりあえずテスト。本当は自動化したい）
    if choose_id == '1':
        st.subheader("あなたの選択した３色")   
        st.text("指定されていません。")
                  
                  

    st.header("Q19：地元(hometown)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q19-1', '#007500')
        st.write(color)
    with col2:
        color = st.color_picker('Q19-2', '#00A400')
        st.write(color)
    with col3:
        color = st.color_picker('Q19-3', '#00A400')
        st.write(color)
    with col4:
        color = st.color_picker('Q19-4', '#D30000')
        st.write(color)
    with col5:
        color = st.color_picker('Q19-5', '#91FF85')
        st.write(color) 

    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("hometown.treemap.bmp") 


    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")




    
    st.header("Q20：国・地域(nation)")


    #streamlitで選択色トップ５を表示　！0は無選択としてカウントに入れず（要検討）
    st.subheader("上位選択色")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        color = st.color_picker('Q20-1', '#FF0000')
        st.write(color)
    with col2:
        color = st.color_picker('Q20-2', '#FFFFFF')
        st.write(color)
    with col3:
        color = st.color_picker('Q20-3', '#D30000')
        st.write(color)
    with col4:
        color = st.color_picker('Q20-4', '#A40000')
        st.write(color)
    with col5:
        color = st.color_picker('Q20-5', '#FF88D5')
        st.write(color)

        
    #flourishで作成したツリーマップの画像（より詳しいアニメーションは有料）
    st.subheader("トレーニング参加者全体の選択色")
    st.image("nation.treemap.bmp")        
        
    #2022選択時に表示
    if choose_id == '2022':
        st.subheader("2022 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2022 All")
        st.image("airashii.treemap.bmp")


    #2023選択時に表示
    if choose_id == '1':
        st.subheader("2023 Top Colors")   
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            color = st.color_picker('Q1-1', '#FFB8E6')
            st.write(color)
    
        with col2:
            color = st.color_picker('Q1-2', '#FFE8F6')
            st.write(color)
    
        with col3:
            color = st.color_picker('Q1-3', '#FF88D5')
            st.write(color)
    
        with col4:
            color = st.color_picker('Q1-4', '#FFB9B8')
            st.write(color)
    
        with col5:
            color = st.color_picker('Q1-5', '#FF58C4')
            st.write(color)

        #PBIで作成したツリーマップの画像
        st.subheader("2023 All")
        st.image("airashii.treemap.bmp")


