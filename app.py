import streamlit as st

st.set_page_config(page_title="Peter Tsai | 南台資訊", page_icon="💼")

# 標題與形象區域 (移除舊版本不支援的參數)
col1, col2 = st.columns([2, 1])

with col1:
    st.title("Peter Tsai")
    st.subheader("執行長 | 南台資訊有限公司")
    st.markdown("> **「連結數位未來，為您的企業打造無限可能。」**")

with col2:
    # 使用 placeholder 圖片，你之後可以換成實際的 URL
    st.image("https://ui-avatars.com/api/?name=Peter+Tsai&size=150&background=0D8ABC&color=fff", width=150)

st.markdown("---")

# 聯絡與服務資訊
col3, col4 = st.columns(2)
with col3:
    st.markdown("### 🌐 聯絡資訊")
    st.write(f"📧 **Email:** chtsai@stust.edu.tw")
    st.write(f"📞 **電話:** 06-253-3131")
    st.write(f"🔗 [Facebook 個人專頁](https://www.facebook.com/keepbusytsai)")

with col4:
    st.markdown("### 🛠 核心服務")
    st.info("雲端整合 • 數位轉型 • 資安防護")

st.success("✨ **卓越科技，誠信服務** —— 南台資訊是您最可靠的夥伴。")
