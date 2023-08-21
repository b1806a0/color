import os
import streamlit as st


def app():

  st.title("トレーニング結果分析")

  #PBIで作成したツリーマップの画像
  st.subheader("箱ひげ図")
  st.image("boxplot.png")
