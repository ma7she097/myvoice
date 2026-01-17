import streamlit as st
import asyncio
import edge_tts

st.set_page_config(page_title="محول الصوت العربي", page_icon="🎙️")
st.title("🎙️ محول النص إلى صوت احترافي")

text = st.text_area("اكتب النص الذي تريد تحويله:", "أهلاً بك، أنا صوتك الذكي الجديد.")
voice = st.selectbox("اختر الصوت:", ["ar-EG-SalmaNeural (مصر)", "ar-SA-HamedNeural (السعودية)"])

if st.button("اسمع الصوت الآن"):
    async def generate():
        communicate = edge_tts.Communicate(text, voice.split(" ")[0])
        await communicate.save("voice.mp3")
    
    with st.spinner('انتظر قليلاً... جاري التحويل'):
        asyncio.run(generate())
        st.audio("voice.mp3")
        st.success("تم التحويل بنجاح!")
