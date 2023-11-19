import streamlit as st

movList1 = [
    "./assets/mov1_all1.mp4",
    "./assets/mov1_salad1.mp4", "./assets/mov1_salad2.mp4", "./assets/mov1_salad3.mp4", "./assets/mov1_salad4.mp4",
    "./assets/mov1_side1.mp4",
    "./assets/mov1_main1.mp4", "./assets/mov1_main2.mp4", "./assets/mov1_main3.mp4", "./assets/mov1_main4.mp4",
    ]
movList2 = [
    "./assets/mov2_all1.mp4",
    "./assets/mov2_salad1.mp4", "./assets/mov2_salad2.mp4", "./assets/mov2_salad3.mp4", "./assets/mov2_salad4.mp4",
    "./assets/mov2_side1.mp4",
    "./assets/mov2_main1.mp4", "./assets/mov2_main2.mp4", "./assets/mov2_main3.mp4", "./assets/mov2_main4.mp4",
    ]


chapter_imgList1 = [
    "./assets/img1_all13.jpg",
    "./assets/img1_salad13.jpg", "./assets/img1_salad23.jpg", "./assets/img1_salad33.jpg", "./assets/img1_salad43.jpg",
    "./assets/img1_side13.jpg",
    "./assets/img1_main13.jpg", "./assets/img1_main23.jpg", "./assets/img1_main33.jpg", "./assets/img1_main43.jpg"
    ]

chapter_imgList2 = [
    "./assets/img2_all13.jpg",
    "./assets/img2_salad13.jpg", "./assets/img2_salad23.jpg", "./assets/img2_salad33.jpg", "./assets/img2_salad43.jpg",
    "./assets/img2_side13.jpg",
    "./assets/img2_main13.jpg", "./assets/img2_main23.jpg", "./assets/img2_main33.jpg", "./assets/img2_main43.jpg"
    ]


abstList1 = [
    "全て：盛り付けの全体像",
    "サラダ①：コールスロー30gを盛り付ける", "サラダ②：ドレッシングをかける", "サラダ③：ハム2切れをコールスローの上に乗せる", "サラダ④：コーンをスプーン山盛り1杯分コールスローの上に乗せる",
    "おかず：からあげ2つを1分温めて盛り付ける",
    "メイン①：ライス1pcを1分半温めて丸く盛り付ける", "メイン②：揚げなすを2切れを10秒温めてライスに立てかける", "メイン③：カレーソース70gを1分温めてライスにかける", "メイン④：ライスにパセリを振りかける"
]

abstList2 = [
    "全て：盛り付けの全体像",
    "サラダ①：リーフミックス30gを盛り付ける", "サラダ②：ドレッシングをかける", "サラダ③：サラダチキン2切れをリーフミックスの上に乗せる", "サラダ④：トマト2切れをリーフミックスの上に乗せる",
    "おかず：からあげ2つを1分温めて盛り付ける",
    "メイン①：パスタ70gをスチーム準備し，4分温めて盛り付ける", "メイン②：ミートソース80gを1分半温めてパスタにかける", "メイン③：ベーコンを4切れを10秒温めてからパスタに乗せる", "メイン④：パスタにパセリを振りかける"
]


# 画像リスト
imgList1 = [
    "./assets/img1_all11.jpg", "./assets/img1_all12.jpg", "./assets/img1_all13.jpg",
    "./assets/img1_salad11.jpg", "./assets/img1_salad12.jpg", "./assets/img1_salad13.jpg",
    "./assets/img1_salad21.jpg", "./assets/img1_salad22.jpg", "./assets/img1_salad23.jpg",
    "./assets/img1_salad31.jpg", "./assets/img1_salad32.jpg", "./assets/img1_salad33.jpg",
    "./assets/img1_salad41.jpg", "./assets/img1_salad42.jpg", "./assets/img1_salad43.jpg",
    "./assets/img1_side11.jpg", "./assets/img1_side12.jpg", "./assets/img1_side13.jpg",
    "./assets/img1_main11.jpg", "./assets/img1_main12.jpg", "./assets/img1_main13.jpg",
    "./assets/img1_main21.jpg", "./assets/img1_main22.jpg", "./assets/img1_main23.jpg",
    "./assets/img1_main31.jpg", "./assets/img1_main32.jpg", "./assets/img1_main33.jpg",
    "./assets/img1_main41.jpg", "./assets/img1_main42.jpg", "./assets/img1_main43.jpg",
            ]

imgList2 = [
    "./assets/img2_all11.jpg", "./assets/img2_all12.jpg", "./assets/img2_all13.jpg",
    "./assets/img2_salad11.jpg", "./assets/img2_salad12.jpg", "./assets/img2_salad13.jpg",
    "./assets/img2_salad21.jpg", "./assets/img2_salad22.jpg", "./assets/img2_salad23.jpg",
    "./assets/img2_salad31.jpg", "./assets/img2_salad32.jpg", "./assets/img2_salad33.jpg",
    "./assets/img2_salad41.jpg", "./assets/img2_salad42.jpg", "./assets/img2_salad43.jpg",
    "./assets/img2_side11.jpg", "./assets/img2_side12.jpg", "./assets/img2_side13.jpg",
    "./assets/img2_main11.jpg", "./assets/img2_main12.jpg", "./assets/img2_main13.jpg",
    "./assets/img2_main21.jpg", "./assets/img2_main22.jpg", "./assets/img2_main23.jpg",
    "./assets/img2_main31.jpg", "./assets/img2_main32.jpg", "./assets/img2_main33.jpg",
    "./assets/img2_main41.jpg", "./assets/img2_main42.jpg", "./assets/img2_main43.jpg",
            ]

chapter_imgList1 = [
    "./assets/img1_all13.jpg",
    "./assets/img1_salad13.jpg", "./assets/img1_salad23.jpg", "./assets/img1_salad33.jpg", "./assets/img1_salad43.jpg",
    "./assets/img1_side13.jpg",
    "./assets/img1_main13.jpg", "./assets/img1_main23.jpg", "./assets/img1_main33.jpg", "./assets/img1_main43.jpg"
    ]

chapter_imgList2 = [
    "./assets/img2_all13.jpg",
    "./assets/img2_salad13.jpg", "./assets/img2_salad23.jpg", "./assets/img2_salad33.jpg", "./assets/img2_salad43.jpg",
    "./assets/img2_side13.jpg",
    "./assets/img2_main13.jpg", "./assets/img2_main23.jpg", "./assets/img2_main33.jpg", "./assets/img2_main43.jpg"
    ]