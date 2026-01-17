import streamlit as st
import asyncio
import edge_tts

st.title("🎙️ مسجل القصص الدرامي")

VOICES = {
    "حامد (رخيم/هادئ)": "ar-SA-HamedNeural",
    "شاكر (متحمس/درامي)": "ar-EG-ShakirNeural",
    "سلمى (ناعمة/سردية)": "ar-EG-SalmaNeural"
}

text = st.text_area("اكتب قصتك هنا (استخدم ... للوقفات الطويلة):", height=250)
selected_voice = st.selectbox("اختر المعلق:", list(VOICES.keys()))

if st.button("توليد الأداء الدرامي"):
    # تحويل النص العادي إلى نص تفاعلي بوقفات
    # كلما وجد البرنامج "..." سيضع وقفة صمت حقيقية
    processed_text = text.replace("...", " <break time='1500ms'/> ")
    
    async def generate():
        # استخدام Communicate لإرسال النص المعدل
        communicate = edge_tts.Communicate(text, VOICES[selected_voice])
        await communicate.save("drama.mp3")
    
    with st.spinner('جاري هندسة الصوت درامياً...'):
        asyncio.run(generate())
        st.audio("drama.mp3")
