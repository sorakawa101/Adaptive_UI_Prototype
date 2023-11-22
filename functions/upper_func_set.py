import streamlit as st
import functions.middle_func_media as fm

def set_medias(selected_medias_list):
    if 'Text' in selected_medias_list:
        fm.media_text_recipe_container()
    if 'Image' in selected_medias_list:
        fm.media_image_recipe_container()
    if 'Video' in selected_medias_list:
        fm.media_video_recipe_container()
    if 'Graph' in selected_medias_list:
        fm.media_graph_recipe_container()