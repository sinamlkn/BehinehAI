import streamlit as st
import plotly.express as px
from data import محصولات_با_موجودی_کم, df

st.set_page_config(page_title="هشدارهای موجودی")

st.title("🚨 هشدارهای موجودی کم")

کمبود = محصولات_با_موجودی_کم()

st.subheader("📊 توزیع وضعیت موجودی")
fig = px.pie(df, names="وضعیت موجودی", title="توزیع کلی موجودی")
st.plotly_chart(fig)

st.subheader("⚠️ محصولات با موجودی کم")
if not کمبود.empty:
    st.warning("برخی محصولات دارای موجودی کم هستند. لطفاً سفارش دهید!")
    st.dataframe(کمبود)
else:
    st.success("✅ هیچ کمبودی در موجودی وجود ندارد.")