import streamlit as st
import functions.middle_func_media as mfm
import functions.middle_func_sidebar as ufs


# Adaptive UI（サイドバーからの入力に適したUI）を表示する関数
def set_adaptive_ui():
    set_navigation(ufs.get_value_from_the_session_state('navigation'))


# 'media'のsession_stateにあるメディアを表示する関数
def set_medias(selected_medias_list):
    if 'Text' in selected_medias_list:
        mfm.media_text_recipe_container()
    if 'Image' in selected_medias_list:
        mfm.media_image_recipe_container()
    if 'Video' in selected_medias_list:
        mfm.media_video_recipe_container()
    if 'Graph' in selected_medias_list:
        mfm.media_graph_recipe_container()


# 'navigation'のsession_stateにあるレイアウトで表示する関数
def set_navigation(selected_navigation):
    if 'Single Column' in selected_navigation:
        set_medias(ufs.get_value_from_the_session_state('media'))
    elif 'Multi Column' in selected_navigation:
        mfm.media_image_recipe_container()
    elif 'Full Screen' in selected_navigation:
        mfm.media_video_recipe_container()
    elif 'Grid' in selected_navigation:
        mfm.media_graph_recipe_container()