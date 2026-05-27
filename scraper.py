import requests

def fetch_templates(query):
    """
    البحث عن القوالب باستخدام واجهة بحث مفتوحة ومستقرة جداً
    تتجنب الحظر تماماً وتعمل على الهواتف والسحابة بكفاءة
    """
    # صياغة جملة البحث لتبحث عن القوالب مباشرة
    search_query = f"{query} powerpoint templates free download"
    
    # استخدام واجهة بحث سريعة ومفتوحة تعيد البيانات كـ نص منظم
    url = f"https://api.duckduckgo.com/?q={search_query}&format=json&no_html=1;skip_disambig=1"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Mobile) AppleWebKit/537.36"
    }
    
    results = []
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            # جلب الروابط المتعلقة بالموضوع مباشرة من نتائج البحث الذكية
            topics = data.get("RelatedTopics", [])
            for topic in topics:
                if "Text" in topic and "FirstURL" in topic:
                    title_text = topic["Text"]
                    actual_link = topic["FirstURL"]
                    
                    # تصفية العناوين الطويلة جداً لتبدو كبطاقة احترافية
                    short_title = title_text[:60] + "..." if len(title_text) > 60 else title_text
                    
                    results.append({
                        "title": f"📄 {short_title}",
                        "image": "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=500", # صورة افتراضية عصرية
                        "link": actual_link
                    })
                    
        # إذا لم يجد نتائج في البحث الذكي المباشر، نستخدم خطة بديلة سريعة لجلب روابط افتراضية موثوقة للموضوع
        if not results:
            sites = [
                {"name": "Slidesgo Templates", "url": f"https://slidesgo.com/search?q={query}"},
                {"name": "SlidesCarnival Free PPT", "url": f"https://www.slidescarnival.com/?s={query}"},
                {"name": "AllPPT Free Presentation", "url": f"https://allpt.com/?s={query}"}
            ]
            for site in sites:
                results.append({
                    "title": f"🔍 اضغط للانتقال المباشر إلى قوالب '{query}' في موقع {site['name']}",
                    "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500",
                    "link": site["url"]
                })
                
    except Exception as e:
        # خطة طوارئ في حال انقطاع الاتصال بالسحابة: إعطاء أزرار توجيه مباشرة
        sites = [
            {"name": "Slidesgo", "url": f"https://slidesgo.com/search?q={query}"},
            {"name": "SlidesCarnival", "url": f"https://www.slidescarnival.com/?s={query}"}
        ]
        for site in sites:
            results.append({
                "title": f"🔗 انتقل مباشرة لقوالب {site['name']} الخاصة بموضوع: {query}",
                "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500",
                "link": site["url"]
            })
            
    return results
    
