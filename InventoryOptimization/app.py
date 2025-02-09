import streamlit as st
import pandas as pd
import plotly.express as px
from data import df, بروزرسانی_موجودی

st.set_page_config(page_title="داشبورد موجودی", layout="wide")

st.title("📦 داشبورد مدیریت موجودی")

# جستجو
جستجو = st.text_input("🔍 جستجو در موجودی (بر اساس نام محصول یا کد کالا)", "")

# فیلتر بر اساس جستجو
فیلتر_شده = df[df["محصول"].str.contains(جستجو, case=False) | df["کد کالا"].str.contains(جستجو, case=False)]

st.subheader("📊 وضعیت موجودی")
st.dataframe(فیلتر_شده)

# نمودار روند موجودی
st.subheader("📉 نمودار موجودی")
fig = px.bar(فیلتر_شده, x="محصول", y=["موجودی", "موجودی پیش‌بینی‌شده", "حداقل موجودی"], barmode="group")
st.plotly_chart(fig)

# ویرایش موجودی
st.subheader("⚙️ ویرایش موجودی")
انتخاب_محصول = st.selectbox("انتخاب محصول برای ویرایش", df["محصول"].tolist())
تغییر_موجودی = st.number_input("تعداد برای اضافه/کم کردن (عدد منفی برای کاهش)", value=0)

if st.button("بروزرسانی موجودی"):
    بروزرسانی_موجودی(انتخاب_محصول, تغییر_موجودی)
    st.success(f"✅ موجودی برای {انتخاب_محصول} به‌روز شد!")
    st.rerun()  # اصلاح‌شده