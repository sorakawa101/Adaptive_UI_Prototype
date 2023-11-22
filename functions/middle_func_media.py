import streamlit as st
import pandas as pd
import numpy as np
import functions.lowwer_func_assets as fa


def media_text_recipe_container():
    texts_container(fa.abstList1)

def media_image_recipe_container():
    images_container(fa.imgList1, fa.abstList1)

def media_video_recipe_container():
    videos_container(fa.movList1, fa.abstList1)

def media_graph_recipe_container():
    graph_container()



def texts_container(abstList):
    for i in range(8):
        st.write(f'{i+1}. ' + abstList[i])


    # 画像を切り替えるタブのコンテナ
def images_container(imgList, abstList):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["全て", "サラダ①", "サラダ②", "サラダ③", "サラダ④", "おかず①", "メイン①", "メイン②", "メイン③", "メイン④"])

    with tab1:
        image_container(tab1, imgList, abstList, 0)
    with tab2:
        image_container(tab2, imgList, abstList, 1)
    with tab3:
        image_container(tab3, imgList, abstList, 2)
    with tab4:
        image_container(tab4, imgList, abstList, 3)
    with tab5:
        image_container(tab5, imgList, abstList, 4)
    with tab6:
        image_container(tab6, imgList, abstList, 5)
    with tab7:
        image_container(tab7, imgList, abstList, 6)
    with tab8:
        image_container(tab8, imgList, abstList, 7)
    with tab9:
        image_container(tab9, imgList, abstList, 8)
    with tab10:
        image_container(tab10, imgList, abstList, 9)



# 画像3枚を配置するコンテナ
def image_container(con, imgList, abstList, i):
    # con.image(IMG_DICT[img])
    col1, col2, col3 = con.columns(3)

    with col1:
        st.image(imgList[i*3], use_column_width=True)

    with col2:
        st.image(imgList[i*3+1], use_column_width=True)

    with col3:
        st.image(imgList[i*3+2], use_column_width=True)

    con.subheader(abstList[i])


# 画像を切り替えるタブのコンテナ
def videos_container(movList, abstList):
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["全て", "サラダ①", "サラダ②", "サラダ③", "サラダ④", "おかず①", "メイン①", "メイン②", "メイン③", "メイン④"])

    with tab1:
        video_container(tab1, movList, abstList, 0)
    with tab2:
        video_container(tab2, movList, abstList, 1)
    with tab3:
        video_container(tab3, movList, abstList, 2)
    with tab4:
        video_container(tab4, movList, abstList, 3)
    with tab5:
        video_container(tab5, movList, abstList, 4)
    with tab6:
        video_container(tab6, movList, abstList, 5)
    with tab7:
        video_container(tab7, movList, abstList, 6)
    with tab8:
        video_container(tab8, movList, abstList, 7)
    with tab9:
        video_container(tab9, movList, abstList, 8)
    with tab10:
        video_container(tab10, movList, abstList, 9)


# 映像閲覧部分のコンテナ
def video_container(con, movList, abstList, i):
    con.video(movList[i])
    con.subheader(abstList[i])


def graph_container():
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.area_chart(chart_data)