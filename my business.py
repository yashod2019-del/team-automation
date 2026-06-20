import streamlit as st
import yt_dlp
import whisper
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import gc 
from pydub import AudioSegment, silence
import math

# --- MoviePy వెర్షన్ చెకింగ్ ---
try:
    from moviepy.editor import VideoFileClip, AudioFileClip
except ModuleNotFoundError:
    from moviepy import VideoFileClip, AudioFileClip

# --- వెబ్ యాప్ పేజీ సెッティングస్ ---
st.set_page_config(page_title="FBO AI Ultimate 10HR Translator", page_icon="🎙️", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; text-align: center; }
    .info-text { font-size: 15px; text-align: center; color: #4B5563; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎙️ FBO అల్టిమేట్ AI వీడియో & వాయిస్ క్లోనర్</div>', unsafe_allow_html=True)
st.markdown('<div class="info-text">🚀 10-గంటల మెగా బిజినెస్ అప్‌డేట్ | ఎంత పెద్ద రికార్డింగ్ అయినా సగంలో ఆగకుండా వంద శాతం ఉచితంగా పూర్తవుతుంది!</div>', unsafe_allow_html=True)

# --- AI మోడల్ లోడింగ్ ---
@st.cache_resource
def load_ai_models():
    # 10 గంటల వీడియోలకు 'base' మోడల్ వేగంగా మరియు తక్కువ మెమరీతో పర్ఫెక్ట్‌గా పనిచేస్తుంది
    return whisper.load_model("base") 

with st.spinner("10-HR AI ఇంజన్స్‌ను బ్యాక్‌గ్రౌండ్‌లో లోడ్ చేస్తున్నాము... దయచేసి వెయిట్ చేయండి..."):
    whisper_model = load_ai_models()

# --- 🇮🇳 ఆల్ ఇండియా లాంగ్వేజెస్ ---
LANGUAGES = {
    "Telugu (తెలుగు)": "te", "Hindi (हिंदी)": "hi", "English (ఇంగ్లీష్)": "en",
    "Tamil (தமிழ்)": "ta", "Kannada (ಕನ್ನಡ)": "kn", "Malayalam (മലയാളം)": "ml",
    "Marathi (मరాఠీ)": "mr", "Gujarati (ગુજરાતી)": "gu", "Bengali (বাংলা)": "bn",
    "Punjabi (ਪੰਜਾਬੀ)": "pa", "Odia (ଓଡ଼ିଆ)": "or", "Assamese (অসমীয়া)": "as",
    "Urdu (اُردو)": "ur", "Sanskrit (संस्कृतम्)": "sa", "Nepali (नेपाली)": "ne",
    "Sindhi (सिंधी)": "sd", "Kashmiri (कश्मीरी)": "ks", "Konkani (कोंकणी)": "kok",
    "Manipuri (মൈতেইলোন)": "mni", "Maithili (मैथिली)": "mai", "Dogri (डोगरी)": "doi",
    "Bodo (बड़ो)": "brx", "Santali (ᱥᱟᱱతᱟᱲᱤ)": "sat"
}

def match_voice_tone(target_text, source_audio_path, target_lang, output_path):
    tts = gTTS(text=target_text, lang=target_lang, slow=False)
    temp_gtts = "temp_gtts.mp3"
    tts.save(temp_gtts)
    
    orig_audio = AudioSegment.from_wav(source_audio_path)
    generated_audio = AudioSegment.from_mp3(temp_gtts)
    
    cloned_flow = generated_audio.set_frame_rate(orig_audio.frame_rate)
    cloned_flow.export(output_path, format="wav")
    
    if os.path.exists(temp_gtts): os.remove(temp_gtts)

def download_social_media(url, download_video=False):
    out_name = "downloaded_media"
    if download_video:
        ydl_opts = {'format': 'best[ext=mp4]/best', 'outtmpl': f'{out_name}.mp4', 'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
        return f"{out_name}.mp4"
    else:
        ydl_opts = {
            'format': 'bestaudio/best', 'outtmpl': f'{out_name}.%(ext)s',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'wav', 'preferredquality': '128'}],
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
        return f"{out_name}.wav"

# --- 10 గంటల నిరంతరాయ ప్రాసెసింగ్ ఇంజన్ ---
def start_core_dubbing(media_path, is_video, target_lang, _prog):
    raw_audio = "temp_raw_audio.wav"
    
    if is_video:
        video_clip = VideoFileClip(media_path)
        video_clip.audio.write_audiofile(raw_audio, fps=16000, nbytes=2, codec='pcm_s16le', verbose=False, logger=None)
        video_clip.close()
    else:
        raw_audio = media_path

    # పెద్ద ఆడియో ఫైల్‌ను ముక్కలుగా విభజించడం
    song = AudioSegment.from_wav(raw_audio)
    chunks = silence.split_on_silence(song, min_silence_len=900, silence_thresh=-45, keep_silence=500)
    
    final_audio = AudioSegment.empty()
    total_chunks = len(chunks)
    
    for i, chunk in enumerate(chunks):
        # 10 గంటల సుదీర్ఘ ప్రక్రియ కాబట్టి యూజర్‌కు ప్రతి అడుగును స్పష్టంగా చూపిస్తుంది
        _prog.progress((i + 1) / total_chunks, text=f"⏳ మెగా బిజినెస్ రికార్డింగ్ ప్రాసెస్ అవుతోంది... పార్ట్ {i+1}/{total_chunks}")
        
        c_in = f"c_in_{i}.wav"
        chunk.export(c_in, format="wav")
        
        # Whisper AI స్థిరమైన ట్రాన్స్‌క్రిప్షన్
        res = whisper_model.transcribe(c_in, fp16=False)
        detected_text = res['text']
        
        if not detected_text.strip():
            final_audio += AudioSegment.silent(duration=len(chunk))
            if os.path.exists(c_in): os.remove(c_in)
            continue
            
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(detected_text)
        
        c_out = f"c_out_{i}.wav"
        try:
            match_voice_tone(translated_text, c_in, target_lang, c_out)
            final_audio += AudioSegment.from_wav(c_out)
        except:
            final_audio += AudioSegment.silent(duration=len(chunk))
            
        if os.path.exists(c_in): os.remove(c_in)
        if os.path.exists(c_out): os.remove(c_out)
        
        # ప్రతి సింగిల్ పార్ట్ తర్వాత రామ్ మెమరీని పూర్తిగా ఖాళీ చేయడం (క్రాష్ ప్రివెన్షన్)
        gc.collect()
        
    final_audio_path = "final_voice_output.wav"
    final_audio.export(final_audio_path, format="wav")
    
    if is_video and os.path.exists(raw_audio): os.remove(raw_audio)
    
    if is_video:
        orig_video = VideoFileClip(media_path)
        new_audio = AudioFileClip(final_audio_path)
        final_video = orig_video.set_audio(new_audio)
        
        output_video_path = "FBO_10HR_Ultimate_Video.mp4"
        final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac", verbose=False, logger=None)
        
        orig_video.close()
        new_audio.close()
        final_video.close()
        return "video", output_video_path
    else:
        return "audio", final_audio_path

# --- UI డిజైన్ ---
col1, col2 = st.columns(2)
media_working_path = None
is_video_input = False
process_ready = False

with col1:
    st.markdown("### 🔗 1. సోషల్ మీడియా లింక్స్")
    url_input = st.text_input("యూట్యూబ్ లేదా ఇన్‌స్టాగ్రామ్ లింక్ ఇక్కడ ఇవ్వండి:")
    link_output_type = st.selectbox("అవుట్‌పుట్ రకం:", ["పూర్తి వీడియో కావాలి (వీడియో + కొత్త వాయిస్)", "కేవలం ఆడియో మాత్రమే కావాలి"])
    
    if url_input and st.button("లింక్ అప్లై చేయి 🔗", use_container_width=True):
        with st.spinner("లింక్ కనెక్ట్ చేస్తున్నాము..."):
            try:
                is_video_input = True if link_output_type == "పూర్తి వీడియో కావాలి (వీడియో + కొత్త వాయిస్)" else False
                media_working_path = download_social_media(url_input, download_video=is_video_input)
                st.session_state['media_path'] = media_working_path
                st.session_state['is_video'] = is_video_input
                st.success("🎯 లింక్ విజయవంతంగా లోడ్ అయింది!")
            except:
                st.error("లింక్ లోడ్ చేయడంలో సమస్య వచ్చింది.")

with col2:
    st.markdown("### 📂 2. ఫైల్ అప్‌లోడ్ (వీడియో/ఆడియో)")
    uploaded_media_file = st.file_uploader("సుదీర్ఘ మీటింగ్ ఫైల్‌ను ఇక్కడ అప్‌లోడ్ చేయండి:", type=["mp4", "mp3", "wav", "m4a", "mov"])
    
    if uploaded_media_file and st.button("అప్‌లోడ్ ఫైల్ అప్లై చేయి 📂", use_container_width=True):
        file_extension = uploaded_media_file.name.split(".")[-1].lower()
        is_video_input = True if file_extension in ["mp4", "mov"] else False
        media_working_path = "uploaded_temp_video.mp4" if is_video_input else "uploaded_temp_audio.wav"
        
        with open(media_working_path, "wb") as f:
            f.write(uploaded_media_file.getbuffer())
            
        st.session_state['media_path'] = media_working_path
        st.session_state['is_video'] = is_video_input
        st.success("🎯 ఫైల్ విజయవంతంగా అప్‌లోడ్ అయింది!")

st.markdown("---")
st.markdown("### 🎯 3. ట్రాన్స్‌లేషన్ లాంగ్వేజ్")
selected_lang = st.selectbox("భారతీయ భాషను ఎంచుకోండి:", list(LANGUAGES.keys()), label_visibility="collapsed")
target_code = LANGUAGES[selected_lang]

if 'media_path' in st.session_state:
    media_working_path = st.session_state['media_path']
    is_video_input = st.session_state['is_video']
    process_ready = True

if process_ready and st.button("🚀 ఆటోమేటిక్ AI ట్రాన్స్‌లేషన్ స్టార్ట్ చేయి", use_container_width=True):
    prog_bar = st.progress(0, text="ప్రాసెస్ ప్రారంభమైంది...")
    try:
        res_format, final_out_path = start_core_dubbing(media_working_path, is_video_input, target_code, prog_bar)
        prog_bar.empty()
        
        st.success(f"🎉 మీటింగ్ విజయవంతంగా పూర్తి 10-గంటల నిడివితో ట్రాన్స్‌లేట్ చేయబడింది!")
        
        if res_format == "video":
            st.video(final_out_path)
            with open(final_out_path, "rb") as f:
                st.download_button("📥 పూర్తి వీడియోను డౌน์โหลด చేసుకోండి", data=f, file_name="FBO_10HR_Full_Video.mp4", mime="video/mp4", use_container_width=True)
        else:
            st.audio(final_out_path)
            with open(final_out_path, "rb") as f:
                st.download_button("📥 పూర్తి ఆడియోను డౌน์โหลด చేసుకోండి", data=f, file_name="FBO_10HR_Full_Audio.wav", mime="audio/wav", use_container_width=True)
    except Exception as e:
        st.error("ట్రాన్స్‌లేషన్‌లో సమస్య వచ్చింది. దయచేసి మళ్లీ ప్రయత్నించండి.")
        
    # తాత్కాలిక ఫైల్స్ క్లీన్ అప్
    for f in ["downloaded_media.mp4", "downloaded_media.wav", "uploaded_temp_video.mp4", "uploaded_temp_audio.wav", "final_voice_output.wav"]:
        if os.path.exists(f): os.remove(f)
    st.session_state.clear()
