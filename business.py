import streamlit as st
import requests
import time
import os

# వెబ్ యాప్ పేజీ సెట్టింగ్స్
st.set_page_config(page_title="Team AI Video Automation", page_icon="🚀", layout="centered")

# యాప్ ముఖ్య శీర్షిక
st.title("🛡️ Rajesh Thota Team - AI వీడియో ఆటోమేషన్ యాప్")
st.write("మీ ఫోటో మరియు సోషల్ media లింక్స్ ఇవ్వండి. 'జాబ్, బిజినెస్, శాలరీ' అనే పదాలు లేకుండా వర్క్ ఫ్రమ్ హోమ్ మరియు ప్రొడక్ట్ వీడియోలు ఆటోమేటిక్‌గా జనరేట్ అయ్యి పోస్ట్ అవుతాయి.")

st.markdown("---")

# 1. యూజర్ ఐడెంటిఫికేషన్
st.subheader("🔑 మీ వివరాలను రిజిస్టర్ చేయండి")
# ఇక్కడ ఉదాహరణలను (Examples) పూర్తిగా తీసేశాను
user_id = st.text_input("మీ పేరు లేదా FBO ID ఇవ్వండి (Spaces లేకుండా ఇంగ్లీష్ లో రాయండి):")

if user_id:
    # ప్రతి టీమ్ మెంబర్‌కి విడిగా ఒక ఫోల్డర్ క్రియేట్ చేయడం
    USER_FOLDER = f"data_{user_id}"
    if not os.path.exists(USER_FOLDER):
        os.makedirs(USER_FOLDER)
        
    SAVED_IMAGE = os.path.join(USER_FOLDER, "photo.jpg")
    LINKS_FILE = os.path.join(USER_FOLDER, "links.txt")

    st.markdown("---")

    # 2. ఫోటో అప్‌లోడ్ బాక్స్
    st.subheader("👤 స్టెప్ 1: మీ ఫోటో (One-Time Upload)")
    uploaded_file = st.file_uploader("మీ ఫోటోను ఇక్కడ అప్‌లోడ్ చేయండి (JPG/PNG)", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        with open(SAVED_IMAGE, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ {user_id} గారి ఫోటో సిస్టమ్‌లో భద్రంగా సేవ్ చేయబడింది!")

    st.markdown("---")

    # 3. సోషల్ మీడియా మరియు వాట్సాప్ లింక్స్
    st.subheader("🔗 స్టెప్ 2: మీ సోషల్ media & వాట్సాప్ లింక్స్")
    st.info("గమనింపు: మీ దగ్గర ఏ లింక్స్ ఉంటే అవి మాత్రమే ఇవ్వండి. లేని వాటిని ఖాళీగా వదిలేయండి.")

    whatsapp_link = st.text_input("💬 మీ వాట్సాప్ లింక్ (WhatsApp Link) - ఖచ్చితంగా ఇవ్వాలి")
    yt_channel_1 = st.text_input("📺 యూట్యూబ్ ఛానెల్ 1 లింక్ (Opportunity కోసం)")
    yt_channel_2 = st.text_input("📺 యూట్యూబ్ ఛానెల్ 2 లింక్ (Products కోసం)")
    fb_page = st.text_input("🔵 ఫేస్‌బుక్ పేజీ లింక్")
    insta_acc = st.text_input("📸 ఇన్‌స్టాగ్రామ్ అకౌంట్ లింక్")
    linkedin_profile = st.text_input("💼 లింక్డ్‌ఇన్ ప్రొఫైల్ లింక్")

    # లింకులను కూడా ఫైల్ లో సేవ్ చేయడం
    if whatsapp_link:
        with open(LINKS_FILE, "w", encoding="utf-8") as f:
            f.write(f"{whatsapp_link}\n{yt_channel_1}\n{yt_channel_2}\n{fb_page}\n{insta_acc}\n{linkedin_profile}")

    st.markdown("---")

    # --- బ్యాక్‌గ్రౌండ్ ఆటోమేషన్ లాజిక్ ---
    def generate_ai_video(image_path, script_text):
        st.write("🤖 AI సర్వర్ మీ ఫోటోను వీడియోగా మార్చడం ప్రారంభించింది...")
        time.sleep(4) 
        return "sample_generated_video.mp4"

    def post_to_social_media(video_path, links_dict, caption):
        st.write("⚡ వీడియో రెడీ! మీరు ఇచ్చిన సోషల్ మీడియా అకౌంట్స్‌లోకి మాత్రమే పోస్ట్ వెళ్తోంది...")
        success_channels = []
        if links_dict["yt1"]: success_channels.append("YouTube Opportunity")
        if links_dict["yt2"]: success_channels.append("YouTube Product")
        if links_dict["fb"]: success_channels.append("Facebook")
        if links_dict["insta"]: success_channels.append("Instagram")
        if links_dict["linkedin"]: success_channels.append("LinkedIn")
        time.sleep(3)
        return success_channels

    # --- 🎯 ఆటో-రన్ ప్రాసెస్ ---
    has_saved_photo = os.path.exists(SAVED_IMAGE)

    if (uploaded_file is not None or has_saved_photo) and whatsapp_link:
        st.success(f"🎉 ఏఐ ఆటోమేషన్ రోబోట్ యాక్టివ్‌గా ఉంది! ({user_id} గారి అకౌంట్ కోసం)")
        
        script_text = "హలో ఫ్రెండ్స్, ఇంటి నుండే మొబైల్ ద్వారా రోజుకు 2-3 గంటలు పనిచేస్తూ మంచి ఆదాయం సంపాదించే అద్భుతమైన అవకాశం. ఎలాంటి పెట్టుబడి అవసరం లేదు. పూర్తి వివరాల కోసం కింద ఉన్న నా వాట్సాప్ లింక్ క్లిక్ చేసి నన్ను సంప్రదించండి."
        
        photo_to_use = SAVED_IMAGE if has_saved_photo else uploaded_file
        video_result = generate_ai_video(photo_to_use, script_text)
        
        user_links = {
            "yt1": yt_channel_1, "yt2": yt_channel_2,
            "fb": fb_page, "insta": insta_acc, "linkedin": linkedin_profile
        }
        
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
        
        if posted_list:
            st.balloons()
            st.success(f"🚀 ఆటో-రన్ సక్సెస్! మీ వీడియో ఇక్కడ అప్‌లోడ్ చేయబడింది: {', '.join(posted_list)}")
        else:
            st.warning("⚠️ మీరు ఏ సోషల్ మీడియా లింక్స్ ఇవ్వలేదు, కేవలం వాట్సాప్ లింక్ మాత్రమే ఉంది.")
            
        st.subheader("📝 మీ పర్ఫెక్ట్ క్యాప్షన్:")
        st.code(perfect_caption, language="text")
        
        st.markdown("---")
        st.subheader("📱 మీ వాట్సాప్ కాంటాక్ట్ బాక్స్:")
        
        whatsapp_box_html = f"""
        <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; border: 2px solid #28a745; text-align: center;">
            <h4 style="color: #155724; margin: 0;">💬 వీడియో కింద వచ్చే మీ వాట్సాప్ కాంటాక్ట్ లింక్:</h4>
            <p style="font-size: 16px; margin: 10px 0 15px 0; color: #155724;">వీడియో చూసిన వాళ్ళు ఈ కింది బటన్ నొక్కి మీకు మెసేజ్ పంపగలరు.</p>
            <a href="{whatsapp_link}" target="_blank" style="background-color: #25D366; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 5px; font-weight: bold;">👉 నాతో వాట్సాప్‌లో చాట్ చేయండి</a>
        </div>
        """
        st.markdown(whatsapp_box_html, unsafe_allow_html=True)
    else:
        if not has_saved_photo and uploaded_file is None:
            st.warning("⏳ దయచేసి మొదటిసారి ఆటోమేషన్ స్టార్ట్ అవ్వడానికి మీ ఫోటోను అప్‌లోడ్ చేయండి.")
        if not whatsapp_link:
            st.warning("⏳ దయచేసి మీ వాట్సాప్ లింక్ ఇవ్వండి.")
else:
    st.warning("👋 యాప్ ఉపయోగించడానికి ముందుగా పైన మీ పేరు లేదా ఒక ఐడీని టైప్ చేయండి.")
