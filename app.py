import streamlit as st
import asyncio
import edge_tts

st.set_page_config(page_title="محول الصوت الاحترافي", page_icon="🎙️")
st.title("🎙️ محول النص إلى صوت طبيعي")

# قائمة بأفضل الأصوات العربية الطبيعية
VOICES = {
    "عربي - مصر (سلمى - أنثى)": "ar-EG-SalmaNeural",
    "عربي - مصر (شاكر - ذكر)": "ar-EG-ShakirNeural",
    "عربي - السعودية (حامد - ذكر)": "ar-SA-HamedNeural",
    "عربي - السعودية (زارينا - أنثى)": "ar-SA-ZariinaNeural",
    "عربي - الإمارات (حمدان - ذكر)": "ar-AE-HamdanNeural"
}

text = st.text_area("اكتب النص الذي تريد تحويله:", "مرحباً بك، يمكنني الآن التحدث بصوت بشري طبيعي.")
selected_voice_label = st.selectbox("اختر الصوت المناسب لك:", list(VOICES.keys()))

if st.button("توليد الصوت"):
    voice_id = VOICES[selected_voice_label]
    
    async def generate():
        communicate = edge_tts.Communicate(text, voice_id)
        await communicate.save("voice.mp3")
    
    with st.spinner('جاري معالجة الصوت...'):
        asyncio.run(generate())
        st.audio("voice.mp3")
        st.success(f"تم التحويل باستخدام صوت {selected_voice_label}")
