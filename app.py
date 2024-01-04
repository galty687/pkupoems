import streamlit as st 
from pymongo import MongoClient

# 配置存储的数据库

user =st.secrets["user"]
password = st.secrets["password"]

url = f"mongodb+srv://{user}:{password}@cluster0.m9he2zx.mongodb.net/"

mongo_client = MongoClient(url)

db = mongo_client["poems"]
collection = db["PKU"]


# 页面说明

product_intro='''
Welcome to our platform, where you can explore the beauty of classical Chinese poetry through a variety of translation styles. \n 
Delve into the rich world of these timeless verses and experience their meaning and elegance in different linguistic interpretations. \n 
Whether you're a connoisseur of poetry or new to the realm of Chinese literary classics, our platform offers a unique window into the artistry of words. \n 
We are currently exploring a novel approach to translate Chinese poems. We warmly invite you to share your feedback after experiencing these poems. Your insights are invaluable to us in refining this method.
'''
st.sidebar.image("pkulogo.png", width=100)
st.sidebar.title("Project Introduction")
st.sidebar.write(product_intro)

st.title("Appreciation of Ancient Chinese Poetry")

st.header("Chinese Original")



# 创建一个容器放中文诗歌
with st.container():
    # 添加诗歌标题和作者
    

    # 创建两列
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("《幽寻》")
        st.caption("作者：赵翼（清）")
        # 左列：原始诗歌
        st.write("""
        幽寻不知疲，意行度遥陌。\n
        昔游所未经，数折地愈僻。\n
        忽至野水岸，路断行迹绝。\n
        欲问空无人，一鹭草边白。\n
        """)

        st.image("images/youxun.png", caption="You Xun", width=200)

    with col2:
        st.subheader("Yōu Xún")
        st.subheader("《幽寻》")
        st.subheader("Quiet Search")
        st.markdown("....................")
        st.caption("Zuòzhě: Zhào Yì (Qīng) ")
        st.caption("作者：赵翼（清）")
        st.caption("Author: Zhao Yi (Qing)")
        st.markdown("....................")


        # 右列：加了拼音和英文翻译的诗歌
        lines = [
            {
                "pinyin": "yōu xún bù zhī pí, yì xíng dù yáo mò.",
                "text": "幽 寻 不知 疲，意行 度 遥陌。",
                "translation": "Solitude, seek, not know, fatigue; Thoughts of the heart, cross(v.), remote, path"
            },
            {
                "pinyin": "xī yóu suǒ wèi jīng, shù zhé dì yù pì.",
                "text": "昔游 所 未经，数折 地 愈 僻。",
                "translation": "Past trip, aux., never experience; several turns, land, more desolate"
            },
            {
                "pinyin": "hū zhì yě shuǐ àn, lù duàn xíng jì jué.",
                "text": "忽至 野水 岸，路断 行迹 绝。",
                "translation": "Suddenly  arrive, wild water,bank; Paths, end (v.), tracks, vanish"
            },
            {
                "pinyin": "yù wèn kōng wú rén, yī lù cǎo biān bái.",
                "text": "欲 问 空 无 人，一 鹭 草 边 白。",
                "translation": "wish, ask, empty, no, people; one, egret, grass edge, white"
            }
        ]

        # 展示诗句及其拼音和翻译
        for line in lines:
            st.caption(line["pinyin"])
            st.write(line["text"])
            st.caption(line["translation"])
            st.markdown("....................")








# 分割线
st.markdown("---")

st.header("Three versions of English Translation")


# 定义诗歌
poem1 = """
In quest of solitude, fatigue unknown, \n
I roam the paths to realms yet unshown. \n

Where ne'er my feet have ventured before, \n
The landscape grows wild, an untamed lore. \n

Abruptly I reach a pond so serene, \n
Whence no traces of path can be seen. \n

To ask: not a soul I find in sight, \n
Save a lone egret in the grass, pure and white.

"""

poem2 = """
In quest of solitude, fatigue unknown, \n
I roam the paths to realms unshown. \n

Where never my feet have been before, \n
The landscape wild, an untamed lore. \n

A pond appears, so serene, \n
of man-made paths, no trace is seen. \n

To ask：no soul in sight \n
But for an egret, pure and white.  \n

"""

poem3 = """
In Search of Solitude \n
I never tire in my search of solitude; \n
I wander aimlessly along out-out-the-way trails \n
Where I have never been before, \n
The more I change my direction, the wilder the road becomes. \n
Suddenly I come to the bank of a raging river; \n
The path breaks off, all trails vanish. \n
No one is there for me to ask directions; \n
Only a lone egret beside the tall grass, glistening white. \n
"""



# 定义诗歌及其评价
poems = [
    {"text": poem1, },
    {"text": poem2, },
    {"text": poem3, }
]

ratings = [None] * len(poems)

# 对于每首诗和评价创建一个行
for i, poem in enumerate(poems):
    # 创建两列
    col1, col2 = st.columns([3, 1])

    # 在左列中放置诗歌
    with col1:
        st.subheader("In Quest of Solitude")
        st.write("By Zhao Yi (Qing Dynasty)")
        st.write(poem["text"])
    

    # 在右列中放置评价
    with col2:
        
        st.write("Version"+str(i+1))
        st.audio("audio/"+str(i+1)+".mp3",)

    # 除了最后一行之外，在每行后添加分割线
    if i < len(poems) - 1:
        st.markdown("---")


st.markdown("---")

languages = [
    'Arabic', 'Bengali', 'Chinese', 'Czech', 'Dutch', 'English', 'Filipino', 
    'French', 'German', 'Greek', 'Hindi', 'Hungarian', 'Indonesian', 'Italian', 
    'Japanese', 'Korean', 'Malay', 'Persian', 'Polish', 'Portuguese', 'Punjabi', 
    'Romanian', 'Russian', 'Spanish', 'Swedish', 'Tamil', 'Turkish', 'Ukrainian', 
    'Urdu', 'Vietnamese'
]


# 创建评价表单
with st.form("evaluation_form"):
    st.write("Please tell us which version do you like?")

    # Collecting user's personal information
    mother_tounge =  st.selectbox("Your First Language", ["Please select"] + languages + ["Other"])
    if mother_tounge == "Other":
        other_language = st.text_input("Please enter your language")
    email = st.text_input("Email (Optional)")

    # Collecting ratings for each poem
    for i, poem in enumerate(poems):
        poems[i]["rating"] = st.radio(
            f"Rate Poem {i+1} (1-5 stars, 1 being the least liked, 5 being the most liked):",
            [1, 2, 3, 4, 5],
            key=f"poem_{i}",
            horizontal=True
        )

    # Submit button
    submitted = st.form_submit_button("Submit Review")
    if submitted and mother_tounge and email:
        st.write("Your submitted information is as follows:")
        st.write(f"Your selected language is: {mother_tounge}")
        if mother_tounge == "Other":
            st.write(f"Your manually entered language is: {other_language}")

        st.write(f"Email: {email}")
        for i, poem in enumerate(poems):
            st.write(f"Rating for Version {i+1}: {poem['rating']} stars")

        feedback_data = {
        "mother_tongue": mother_tounge if mother_tounge != "Other" else other_language,
        "email": email,
        "ratings": [poem["rating"] for poem in poems]
        }

    # 插入数据到 MongoDB Atlas
        collection.insert_one(feedback_data)   
        st.success("Sucess. Thank you for your feedback!")    
