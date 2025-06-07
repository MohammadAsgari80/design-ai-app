
import streamlit as st
import pandas as pd
import joblib

# بارگذاری مدل آموزش‌دیده
model = joblib.load("decision_tree_model.pkl")

# عنوان اپلیکیشن
st.set_page_config(page_title="پیشنهاد طراحی پست اینستاگرام", layout="centered")
st.title("🎨 ابزار هوشمند پیشنهاد طراحی پست اینستاگرام")

# فرم ورودی کاربر
with st.form("design_form"):
    col1, col2 = st.columns(2)
    goal = col1.selectbox("🎯 هدف پست", ["فروش", "اطلاع‌رسانی", "معرفی محصول", "جذب فالوور"])
    job = col2.selectbox("💼 حوزه کاری", ["آموزش", "فشن", "تکنولوژی", "غذا", "مالی"])
    audience = col1.selectbox("👥 نوع مخاطب", ["نوجوان", "جوان", "بزرگسال", "عمومی"])
    budget = col2.selectbox("💰 بودجه طراحی", ["پایین", "متوسط", "بالا"])
    brand_color = col1.selectbox("🎨 رنگ برند (در صورت وجود)", ["گرم", "سرد", "خنثی", "مهم نیست"])

    submitted = st.form_submit_button("دریافت پیشنهاد")

# پیش‌بینی و نمایش
if submitted:
    user_input = pd.DataFrame([[goal, job, audience, budget, brand_color]],
                              columns=["هدف پست", "شغل", "مخاطب", "بودجه", "رنگ برند"])
    prediction = model.predict(user_input)[0]
    layout, shape, radius, alignment, color = prediction

    st.markdown("## ✨ پیشنهاد طراحی هوشمند")
    st.markdown(f"- **نوع قالب:** {layout}")
    st.markdown(f"- **نوع شکل‌ها:** {shape}")
    st.markdown(f"- **میزان انحنا (radius):** {radius}")
    st.markdown(f"- **چینش عناصر:** {alignment}")
    st.markdown(f"- **🎨 رنگ پیشنهادی:** `{color}`")
