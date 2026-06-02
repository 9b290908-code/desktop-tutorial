import streamlit as st
from streamlit_option_menu import option_menu

# 1. 網頁基本設定 (必須是第一個 Streamlit 指令)
st.set_page_config(
    page_title="Peter Tsai | 南台資訊有限公司",
    page_icon="💻",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. 注入自訂高級感 CSS 樣式 (Vibe Styling)
st.markdown("""
    <style>
    /* 全域背景與文字優化 */
    .stApp {
        background: linear-gradient(135deg, #0b0f19 0%, #111827 100%);
        color: #f3f4f6;
    }
    
    /* 標語特殊樣式 */
    .slogan {
        font-size: 1.5rem !important;
        color: #38bdf8 !important;
        font-weight: 600;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 5px;
    }
    
    /* 名字樣式 */
    .hero-name {
        font-size: 3.5rem !important;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(to right, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    /* 職稱樣式 */
    .hero-title {
        font-size: 1.3rem;
        color: #9ca3af;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* 區塊標題 */
    .section-title {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        border-bottom: 2px solid #38bdf8;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    
    /* 服務項目卡片 */
    .service-card {
        background-color: #1f2937;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #38bdf8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .service-card h4 {
        color: #f3f4f6;
        margin-bottom: 0.5rem;
    }
    .service-card p {
        color: #9ca3af;
        font-size: 0.95rem;
    }
    
    /* 聯絡資訊連結優化 */
    .contact-link {
        color: #38bdf8;
        text-decoration: none;
        font-weight: bold;
    }
    .contact-link:hover {
        color: #818cf8;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 頂部導覽列 (使用 streamlit-option-menu 營造單頁式應用 Vibe)
selected = option_menu(
    menu_title=None,
    options=["首頁", "核心服務", "聯絡執行長"],
    icons=["house", "cpu", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#111827"},
        "icon": {"color": "#38bdf8", "font-size": "1rem"}, 
        "nav-link": {"font-size": "1rem", "text-align": "center", "margin":"0px", "color": "#9ca3af"},
        "nav-link-selected": {"background-color": "#1f2937", "color": "#38bdf8", "font-weight": "600"},
    }
)

# 4. 各分頁內容
if selected == "首頁":
    # Hero 區塊
    st.markdown('<p class="slogan">「 數據驅動未來，技術鑄就卓越 」</p>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-name">Peter Tsai</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-title">執行長 | 南台資訊有限公司</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">關於執行長</div>', unsafe_allow_html=True)
    st.markdown("""
    歡迎來到 **南台資訊有限公司**。
    
    身為執行長，我致力於將最前沿的資訊技術轉化為企業的實質競爭力。在瞬息萬變的數位時代，我們不只是系統的建構者，更是企業數位轉型路上最值得信賴的策略夥伴。
    我們堅持以最高規格的技術與創新思維，為客戶打造安全、高效且具擴充性的解決方案。
    """)
    
    # 放一個現代感的 CTA 按鈕
    st.write("")
    if st.button("🚀 了解我們的核心服務"):
        st.info("請點擊上方導覽列的『核心服務』查看更多詳情！")

elif selected == "核心服務":
    st.markdown('<div class="section-title">常見服務項目</div>', unsafe_allow_html=True)
    st.write("南台資訊提供全方位的企業級 IT 解決方案：")
    
    # 服務項目卡片 1
    st.markdown("""
    <div class="service-card">
        <h4>🌐 企業數位轉型服務 (Digital Transformation)</h4>
        <p>評估企業現有流程，量身打造雲端化與自動化方案，全面提升營運效率與市場競爭力。</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 服務項目卡片 2
    st.markdown("""
    <div class="service-card">
        <h4>☁️ 雲端架構與整合 (Cloud Infrastructure)</h4>
        <p>提供 AWS、Azure 等主流雲端系統部署與維護，優化資料流與伺服器負載，確保服務永續不中斷。</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 服務項目卡片 3
    st.markdown("""
    <div class="service-card">
        <h4>🔒 網路資訊安全防護 (Cybersecurity)</h4>
        <p>資安漏洞健檢、企業防火牆架設及資安事件應變，全方位守護您的核心商業數據。</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 服務項目卡片 4
    st.markdown("""
    <div class="service-card">
        <h4>📊 大數據分析與 AI 應用 (Data & AI Solutions)</h4>
        <p>運用數據探勘與機器學習技術，將海量資料轉化為精準的商業決策預測，搶佔市場先機。</p>
    </div>
    """, unsafe_allow_html=True)

elif selected == "聯絡執行長":
    st.markdown('<div class="section-title">聯絡資訊</div>', unsafe_allow_html=True)
    st.write("歡迎透過以下方式與我建立聯繫，或洽談商務合作：")
    
    # 使用 Streamlit 的 columns 做出乾淨的排版
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏢 公司資訊")
        st.write("**公司名稱：** 南台資訊有限公司")
        st.write("**職稱：** 執行長")
        st.write("**連絡電話：** [06-253-3131](tel:06-253-3131)")
        
    with col2:
        st.subheader("🔗 線上聯絡")
        st.write("**電子郵件：** [chtsai@stust.edu.tw](mailto:chtsai@stust.edu.tw)")
        
        # 加上要求的 Facebook 連結，使用好看的 Markdown 按鈕樣式
        st.write("**社群網絡：**")
        st.markdown(
            '<a href="https://www.facebook.com/keepbusytsai" target="_blank" style="display:inline-block; background-color:#1877F2; color:white; padding:8px 16px; border-radius:8px; text-decoration:none; font-weight:bold;">'
            '📘 訪問 Peter 的 Facebook'
            '</a>', 
            unsafe_allow_html=True
        )

# 5. 頁尾
st.markdown("""
<hr style="border-color: rgba(255,255,255,0.1);">
<p style="text-align: center; color: #6b7280; font-size: 0.85rem;">
    &copy; 2026 南台資訊有限公司. All rights reserved. Built with Streamlit Vibe.
</p>
""", unsafe_allow_html=True)
