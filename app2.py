import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# تنظیمات صفحه
st.set_page_config(page_title="پیشنهاد طراحی پست اینستاگرام", layout="centered")
st.title("🎨 ابزار هوشمند پیشنهاد طراحی پست اینستاگرام")

# داده آموزشی ساده
data = pd.DataFrame([
    ["فروش", "آموزش", "جوان", "متوسط", "گرم", "شبکه‌ای", "دایره", "زیاد", "مرکزچین", "قرمز"],
    ["اطلاع‌رسانی", "فشن", "نوجوان", "بالا", "سرد", "ستونی", "مثلث", "کم", "چپ‌چین", "آبی"],
    ["معرفی محصول", "تکنولوژی", "جوان", "متوسط", "خنثی", "مربعی", "مستطیل", "متوسط", "راست‌چین", "خاکستری"],
    ["جذب فالوور", "غذا", "عمومی", "پایین", "گرم", "دایره‌ای", "دایره", "زیاد", "مرکزچین", "نارنجی"],
    ["اطلاع‌رسانی", "مالی", "بزرگسال", "متوسط", "سرد", "ستونی", "مستطیل", "کم", "راست‌چین", "آبی"]
], columns=["هدف پست", "شغل", "مخاطب", "بودجه", "رنگ برند", 
            "layout", "shape", "radius", "alignment", "color"])

# آماده‌سازی داده
le = LabelEncoder()
X = data[["هدف پست", "شغل", "مخاطب", "بودجه", "رنگ برند"]].apply(le.fit_transform)
y = data[["layout", "shape", "radius", "alignment", "color"]].apply(le.fit_transform)

# آموزش مدل
model = DecisionTreeClassifier()
model.fit(X, y)

# فرم ورودی کاربر
with st.form("design_form"):
    col1, col2 = st.columns(2)
    goal = col1.selectbox("🎯 هدف پست", ["فروش", "اطلاع‌رسانی", "معرفی محصول", "جذب فالوور"])
    job = col2.selectbox("💼 حوزه کاری", ["آموزش", "فشن", "تکنولوژی", "غذا", "مالی"])
    audience = col1.selectbox("👥 نوع مخاطب", ["نوجوان", "جوان", "بزرگسال", "عمومی"])
    budget = col2.selectbox("💰 بودجه طراحی", ["پایین", "متوسط", "بالا"])
    brand_color = col1.selectbox("🎨 رنگ برند (در صورت وجود)", ["گرم", "سرد", "خنثی", "مهم نیست"])

    submitted = st.form_submit_button("دریافت پیشنهاد")

if submitted:
    input_df = pd.DataFrame([[goal, job, audience, budget, brand_color]], 
                             columns=["هدف پست", "شغل", "مخاطب", "بودجه", "رنگ برند"])
    input_encoded = input_df.apply(le.fit_transform)
    prediction = model.predict(input_encoded)[0]

    layout, shape, radius, alignment, color = prediction
    st.markdown("## ✨ پیشنهاد طراحی هوشمند")
    st.markdown(f"- **نوع قالب:** {layout}")
    st.markdown(f"- **نوع شکل‌ها:** {shape}")
    st.markdown(f"- **میزان انحنا (radius):** {radius}")
    st.markdown(f"- **چینش عناصر:** {alignment}")
    st.markdown(f"- **🎨 رنگ پیشنهادی:** `{color}`")
