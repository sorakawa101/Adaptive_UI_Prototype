import streamlit as st
import functions.func_common as fc
import functions.func_sidebar as fs
import functions.func_media as fm
import functions.func_assets as fa



# * サイドバーコンテンツ
def sidebar():
    with st.sidebar:
        st.header("Media")
        # マルチセレクト（動画・画像・逐次・全体）
        media = fs.input_media()
        fs.set_value_to_the_session_state("media", media)

        st.header("Navigation")
        # ラジオボタン（レイアウト）
        navigation = fs.input_navigation()
        fs.set_value_to_the_session_state("navigation", navigation)

        st.header("Layout")
        # スライダー（フォントサイズ）
        font_size = fs.input_font_size()
        fs.set_value_to_the_session_state("font_size", font_size)

        # カラーピッカー（色）
        color = fs.input_color()
        fs.set_value_to_the_session_state("color", color)

        st.header("Task-Feature Set")
        # トグル（情報量最大・最小）
        task_feature_set = fs.input_task_feature_set()
        fs.set_value_to_the_session_state("task_feature_set", task_feature_set)


def container():
    fm.media_text_recipe()
    fm.media_image_recipe()
    fm.media_video_recipe()
    fm.media_graph_recipe()
    # st.write(fs.get_value_from_the_session_state("media"))
    # st.write(fs.get_value_from_the_session_state("navigation"))
    # st.write(fs.get_value_from_the_session_state("font_size"))
    # st.write(fs.get_value_from_the_session_state("color"))
    # st.write(fs.get_value_from_the_session_state("task_feature_set"))


# main関数
def main():
    fc.set_page_config()
    sidebar()
    container()


# 実行
if __name__ == "__main__":
    main()
