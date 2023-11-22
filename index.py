import streamlit as st
import functions.upper_func_set as ufs
import functions.lower_func_common as lfc
import functions.middle_func_sidebar as mfs


# * サイドバーコンテンツ
def sidebar():
    with st.sidebar:
        mfs.view_media()

        st.header("Navigation")
        # ラジオボタン（レイアウト）
        navigation = mfs.input_navigation()
        mfs.set_value_to_the_session_state("navigation", navigation)

        st.header("Layout")
        # スライダー（フォントサイズ）
        font_size = mfs.input_font_size()
        mfs.set_value_to_the_session_state("font_size", font_size)

        # カラーピッカー（色）
        color = mfs.input_color()
        mfs.set_value_to_the_session_state("color", color)

        st.header("Task-Feature Set")
        # トグル（情報量最大・最小）
        task_feature_set = mfs.input_task_feature_set()
        mfs.set_value_to_the_session_state("task_feature_set", task_feature_set)


def container():
    ufs.set_medias(mfs.get_value_from_the_session_state('media'))
    # st.write(mfs.get_value_from_the_session_state("media"))
    # st.write(mfs.get_value_from_the_session_state("navigation"))
    # st.write(mfs.get_value_from_the_session_state("font_size"))
    # st.write(mfs.get_value_from_the_session_state("color"))
    # st.write(mfs.get_value_from_the_session_state("task_feature_set"))


# main関数
def main():
    lfc.set_page_config()
    sidebar()
    container()


# 実行
if __name__ == "__main__":
    main()
