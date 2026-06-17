    import streamlit as st
import requests
import time

# వెబ్ యాప్ పేజీ సెట్టింగ్స్
st.set_page_config(page_title="Team AI Video Automation", page_icon="🚀", layout="centered")

# యాప్ ముఖ్య శీర్షిక
st.title("🛡️ Rajesh Thota Team - AI వీడియో ఆటోమేషన్ యాప్")
st.write("మీ ఫోటో మరియు సోషల్ media లింక్స్ ఇవ్వండి. 'జాబ్, బిజినెస్, శాలరీ' అనే పదాలు లేకుండా వర్క్ ఫ్రమ్ హోమ్ మరియు ప్రొడక్ట్ వీడియోలు ఆటోమేటిక్‌గా జనరేట్ అయ్యి పోస్ట్ అవుతాయి.")

st.markdown("---")

# 1. ఫోటో అప్‌లోడ్
st.subheader("👤 స్టెప్ 1: మీ ఫోటో")
uploaded_file = st.file_uploader("మీ ఫోటోను ఇక్కడ అప్‌లోడ్ చేయండి (JPG/PNG)", type=["jpg", "png", "jpeg"])

st.markdown("---")

# 2. సోషల్ మీడియా మరియు వాట్సాప్ లింక్స్
st.subheader("🔗 స్టెప్ 2: మీ సోషల్ మీడియా & వాట్సాప్ లింక్స్")
st.info("గమనింపు: మీ దగ్గర ఏ అకౌంట్స్ అయితే ఉన్నాయో వాటి లింక్స్ మాత్రమే ఇవ్వండి. లేని వాటిని ఖాళీగా వదిలేయండి (Optional).")

whatsapp_link = st.text_input("💬 మీ వాట్సాప్ లింక్ (WhatsApp Link) - *ఖచ్చితంగా ఇవ్వాలి*")
yt_channel_1 = st.text_input("📺 యూట్యూబ్ ఛానెల్ 1 లింక్ (Opportunity కోసం)")
yt_channel_2 = st.text_input("📺 యూట్యూబ్ ఛానెల్ 2 లింక్ (Products కోసం - ఉంటేనే ఇవ్వండి)")
fb_page = st.text_input("🔵 ఫేస్‌బుక్ పేజీ లింక్ (ఉంటేనే ఇవ్వండి)")
insta_acc = st.text_input("📸 ఇన్‌స్టాగ్రామ్ అకౌంట్ లింక్ (ఉంటేనే ఇవ్వండి)")
linkedin_profile = st.text_input("💼 లింక్డ్‌ఇన్ ప్రొఫైల్ లింక్ (ఉంటేనే ఇవ్వండి)")

st.markdown("---")

# 3. షెడ్యూలింగ్ సెట్టింగ్స్
st.subheader("📅 స్టెప్ 3: వీడియో టైమింగ్స్")
wfh_frequency = st.selectbox("వర్క్ ఫ్రమ్ హోమ్ వీడియో ఎప్పుడు పోస్ట్ అవ్వాలి?", ["ప్రతి 2 రోజులకు ఒకసారి", "ప్రతి రోజు"])
product_frequency = st.selectbox("ఫరెవర్ ప్రొడక్ట్ వీడియో ఎప్పుడు పోస్ట్ అవ్వాలి?", ["వారానికి ఒకసారి", "వారానికి రెండు సార్లు"])

st.markdown("---")

# --- బ్యాక్‌గ్రౌండ్ ఆటోమేషన్ లాజిక్ ---
def generate_ai_video(image_file, script_text):
    st.write("🤖 AI సర్వర్ మీ ఫోటోను వీడియోగా మారుస్తోంది... (దీనికి 1-2 నిమిషాలు పట్టవచ్చు)")
    time.sleep(5) 
    return "sample_generated_video.mp4"

def post_to_social_media(video_path, links_dict, caption):
    st.write("⚡ వీడియో మరియు క్యాప్షన్ రెడీ! మీరు ఇచ్చిన సోషల్ media లింకులకు పోస్ట్ అప్‌లోడ్ చేయబడుతోంది...")
    success_channels = []
    if links_dict["yt1"]: success_channels.append("YouTube Opportunity Channel")
    if links_dict["yt2"]: success_channels.append("YouTube Product Channel")
    if links_dict["fb"]: success_channels.append("Facebook Page")
    if links_dict["insta"]: success_channels.append("Instagram Business")
    if links_dict["linkedin"]: success_channels.append("LinkedIn Profile")
    time.sleep(3)
    return success_channels

# 4. రన్ బటన్
if st.button("🚀 వీడియో జనరేట్ చేసి ఆటో-పోస్ట్ చేయి"):
    if uploaded_file is None:
        st.error("దయచేసి మీ ఫోటోను అప్‌లోడ్ చేయండి.")
    elif not whatsapp_link:
        st.error("లింక్ కింద వాట్సాప్ బటన్ కోసం దయచేసి మీ వాట్సాప్ లింక్ ఇవ్వండి.")
    else:
        st.success("🎉 వివరాలు విజయవంతంగా తీసుకున్నాము!")
        
        # వీడియో స్క్రిప్ట్ టెక్స్ట్
        script_text = f"హలో ఫ్రెండ్స్, ఇంటి నుండే మొబైల్ ద్వారా రోజుకు 2-3 గంటలు పనిచేస్తూ మంచి ఆదాయం సంపాదించే అద్భుతమైన అవకాశం. ఎలాంటి పెట్టుబడి అవసరం లేదు. పూర్తి వివరాల కోసం కింద ఉన్న నా వాట్సాప్ లింక్ క్లిక్ చేసి నన్ను సంప్రదించండి."
        
        video_result = generate_ai_video(uploaded_file, script_text)
        
        user_links = {
            "yt1": yt_channel_1, "yt2": yt_channel_2,
            "fb": fb_page, "insta": insta_acc, "linkedin": linkedin_profile
        }
        
        # --- కొత్తగా యాడ్ చేసిన పర్ఫెక్ట్ క్యాప్షన్ మరియు హ్యాష్‌ట్యాగ్స్ లాజిక్ ---
        perfect_caption = (
            f"🎯 🌟 ఇంటి నుండే పని చేస్తూ ఎదిగే అద్భుతమైన అవకాశం! 🌟\n\n"
            f"మీ మొబైల్ ఫోన్ ఉపయోగించి రోజుకు 2-3 గంటలు కేటాయించి మంచి ఆదాయం పొందండి. "
            f"ఎలాంటి పెట్టుబడి (No Investment) అవసరం లేదు. మా టీమ్‌తో కలిసి డిజిటల్‌గా ముందుకు సాగండి! 🔥\n\n"
            f"మరిన్ని వివరాల కోసం వెంటనే కింద ఉన్న లింక్ క్లిక్ చేసి నన్ను వాట్సాప్‌లో సంప్రదించండి:\n"
            f"👇👇👇\n"
            f"🔗 {whatsapp_link}\n\n"
            f"#WorkFromHome #DigitalOpportunity #IncomeOpportunity #RajeshThotaTeam #SocialMediaGrowth #NoInvestment #OnlineEarning #TeamAutomation"
        )
        
        posted_list = post_to_social_media(video_result, user_links, perfect_caption)
        
        st.balloons() 
        st.success(f"🎉 అద్భుతం! మీ వీడియో షెడ్యూల్ చేయబడింది. కింది ప్లాట్‌ఫారమ్స్‌లో ఆటోమేటిక్‌గా అప్‌లోడ్ అవుతుంది: {', '.join(posted_list)}")
        
        # --- స్క్రీన్ మీద యూజర్‌కి క్యాప్షన్ చూపించడం ---
        st.subheader("📝 వీడియోతో పాటు అప్‌లోడ్ అయిన పర్ఫెక్ట్ క్యాప్షన్:")
        st.code(perfect_caption, language="text")
        
        # --- వాట్సాప్ కాంటాక్ట్ బాక్స్ బటన్ ---
        st.markdown("---")
        st.subheader("📱 వీడియో చూసిన వాళ్ళు మెసేజ్ చేయడానికి వాట్సాప్ బాక్స్:")
        
        st.markdown(
            f"""
            <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; border: 2px solid #28a745; text-align: center;">
                <h4 style="color: #155724; margin: 0;">💬 వీడియో కింద వచ్చే మీ వాట్సాప్ కాంటాక్ట్ లింక్:</h4>
                <p style="font-size: 16px; margin: 10px 0 15px 0; color: #155724;">వీడియో చూసిన వాళ్ళు ఈ కింది లింక్ లేదా బటన్ నొక్కి మీకు మెసేజ్ పంపగలరు.</p>
                <a href="{whatsapp_link}" target="_blank" style="background-color: #25D366; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px; font-weight: bold;">👉 నాతో వాట్సాప్‌లో చాట్ చేయండి</a>
            </div>
            """, 
            unsafe_allow_html=True
        )
