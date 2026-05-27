import streamlit as st

def load_local_css():
    """حقن كود CSS مخصص لجعل الواجهة عصرية وتشبه تطبيقات AI الحديثة"""
    st.markdown("""
        <style>
        /* تحسين الخطوط والخلفيات */
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
        
        html, body, [data-testid="stSidebarNav"] {
            font-family: 'Tajawal', sans-serif;
        }
        
        /* تصميم بطاقات عرض القوالب */
        .template-card {
            background-color: #1e222b;
            border: 1px solid #3e4451;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }
        .template-card:hover {
            transform: translateY(-5px);
            border-color: #4a90e2;
        }
        .template-title {
            color: #ffffff;
            font-size: 1.1rem;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .download-btn {
            display: inline-block;
            background: linear-gradient(135deg, #4a90e2, #50e3c2);
            color: white !important;
            padding: 8px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            text-align: center;
            margin-top: 10px;
            width: 100%;
        }
        </style>
    """, unsafe_style=False)

def get_translation(lang):
    """قاموس اللغات لدعم العربية والإنجليزية"""
    translations = {
        "ar": {
            "title": "🧠 مـستكشف قوالب PowerPoint الذكي",
            "subtitle": "ابحث عن أفضل القوالب الجاهزة لعرضك التقديمي في ثوانٍ",
            "placeholder": "اكتب موضوع العرض هنا (مثال: ذكاء اصطناعي، طب، تعليم)...",
            "search_btn": "🔍 ابحث عن قوالب",
            "loading": "جاري البحث وجلب القوالب المناسبة...",
            "no_results": "لم نجد قوالب تطابق هذا البحث حالياً. جرب كلمات مفتاحية أخرى.",
            "results_found": "تم العثور على {} قالب مميز لـ:",
            "download": "🔗 معاينة وتحميل القالب",
            "lang_label": "🌐 اختر اللغة / Language"
        },
        "en": {
            "title": "🧠 Smart PowerPoint Template Finder",
            "subtitle": "Find the best ready-made templates for your presentation in seconds",
            "placeholder": "Type presentation topic here (e.g., AI, Medicine, Education)...",
            "search_btn": "🔍 Search Templates",
            "loading": "Searching and fetching matching templates...",
            "no_results": "No templates found matching this topic. Try other keywords.",
            "results_found": "Found {} premium templates for:",
            "download": "🔗 Preview & Download Template",
            "lang_label": "🌐 اختر اللغة / Language"
        }
    }
    return translations[lang]
  
