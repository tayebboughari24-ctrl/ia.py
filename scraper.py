import requests
from bs4 import BeautifulSoup
import urllib.parse

def fetch_templates(query):
    """
    البحث عن قوالب بناءً على الكلمة المفتاحية للمستخدم.
    """
    # ترميز النص ليتوافق مع الروابط (URL Encoding)
    encoded_query = urllib.parse.quote(query)
    
    # سنستخدم موقع يعتمد بنية بسيطة للبحث كمثال (يمكنك تكييف الروابط والـ Classes حسب الموقع المستهدف)
    # ملاحظة: بعض المواقع تتطلب توجيه البحث للإنجليزية لنتائج أفضل، سنتعامل مع ما يكتبه المستخدم مباشرة
    url = f"https://allpt.com/?s={encoded_query}" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    results = []
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return results
            
        soup = BeautifulSoup(response.text, "lxml")
        
        # تخصيص المستخرجات بناءً على بنية موقع الهيكل المستهدف
        # (هذا التحديد متوافق مع بنية مدونات القوالب الشائعة المعتمدة على ووردبريس)
        articles = soup.find_all("article") or soup.find_all("div", class_="post")
        
        for article in articles:
            # 1. استخراج العنوان
            title_tag = article.find("h2") or article.find("h3")
            title = title_tag.get_text(strip=True) if title_tag else "PowerPoint Template"
            
            # 2. استخراج رابط المقال/القالب
            link_tag = article.find("a")
            link = link_tag["href"] if link_tag and link_tag.has_attr("href") else "#"
            
            # 3. استخراج صورة المعاينة
            img_tag = article.find("img")
            if img_tag:
                img_url = img_tag.get("src") or img_tag.get("data-src") or img_tag.get("data-lazy-src")
            else:
                # صورة افتراضية في حال عدم وجود صورة للمعاينة
                img_url = "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=500"
                
            # تصفية وترتيب مبدئي: التأكد من أن العنوان يحتوي على جزء من كلمة البحث لزيادة الملاءمة
            results.append({
                "title": title,
                "image": img_url,
                "link": link
            })
            
        # نظام ترتيب ذكي (Relevance Ranking):
        # نضع النتائج التي تحتوي الكلمة المفتاحية في العنوان أولاً
        results.sort(key=lambda x: any(word.lower() in x["title"].lower() for word in query.split()), reverse=True)
        
    except Exception as e:
        print(f"Error during scraping: {e}")
        
    return results
