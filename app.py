import streamlit as st
from utils import load_local_css, get_translation
from scraper import fetch_templates

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Smart PPT Finder",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تحميل الستايل المخصص
load_local_css()

# 2. شريط الجانبي لإعدادات التطبيق (Sidebar)
with st.sidebar:
    st.markdown("### ⚙️ Control Panel / لوحة التحكم")
    lang = st.selectbox(
        "🌐 اختر اللغة / Language",
        options=["ar", "en"],
        format_func=lambda x: "العربية" if x == "ar" else "English"
    )

# جلب نصوص اللغة المختارة
t = get_translation(lang)

# تحديد اتجاه النص بناء على اللغة لضمان تجربة مستخدم احترافية (RTL/LTR)
direction = "rtl" if lang == "ar" else "ltr"

# 3. واجهة التطبيق الرئيسية (Main UI)
st.markdown(f"""
    <div style='text-align: center; direction: {direction}; margin-bottom: 40px;'>
        <h1 style='font-size: 2.5rem; color: #ffffff;'>{t['title']}</h1>
        <p style='color: #a0aec0; font-size: 1.2rem;'>{t['subtitle']}</p>
    </div>
""", unsafe_allow_html=True)

# 4. منطقة الإدخال والبحث
with st.container():
    col1, col2 = st.columns([5, 1] if direction == "rtl" else [1, 5])
    
    # جعل مربع النص والزر متناسقين حسب الاتجاه
    if direction == "rtl":
        with col1:
            query = st.text_input("", placeholder=t["placeholder"], label_visibility="collapsed")
        with col2:
            search_button = st.button(t["search_btn"], use_container_width=True)
    else:
        with col2:
            query = st.text_input("", placeholder=t["placeholder"], label_visibility="collapsed")
        with col1:
            search_button = st.button(t["search_btn"], use_container_width=True)

# 5. منطق المعالجة وعرض النتائج
if search_button and query:
    with st.spinner(t["loading"]):
        # استدعاء دالة البحث من ملف scraper.py
        results = fetch_templates(query)
        
    if results:
        st.markdown(f"<h3 style='direction: {direction}; color: #50e3c2;'>{t['results_found'].format(len(results))} '{query}'</h3>", unsafe_allow_html=True)
        st.write("---")
        
        # عرض النتائج في شبكة (Grid) احترافية (3 أعمدة في كل صف)
        cols = st.columns(3)
        for idx, item in enumerate(results):
            with cols[idx % 3]:
                st.markdown(f"""
                    <div class="template-card" style="direction: {direction};">
                        <img src="{item['image']}" style="width:100%; border-radius:8px; max-height:180px; object-fit:cover; margin-bottom:10px;">
                        <div class="template-title">{item['title']}</div>
                        <a href="{item['link']}" target="_blank" class="download-btn">{t['download']}</a>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.info(t["no_results"])
