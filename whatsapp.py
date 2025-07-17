import streamlit as st
import pywhatkit as kit

def send_whatsapp():
    st.title("📱 WhatsApp Auto Message Sender")

    phone = st.text_input("📞 Enter WhatsApp Number (with country code)", value="+91")
    message = st.text_area("💬 Enter Message", value="!")

    col1, col2 = st.columns(2)
    with col1:
        hour_input = st.number_input("🕑 Hour (0-23)", min_value=0, max_value=23, value=12)
    with col2:
        min_input = st.number_input("🕓 Minutes (0-59)", min_value=0, max_value=59, value=30)

    st.markdown("### 📋 Message Summary")
    st.markdown(f"**Phone Number:** {phone}")
    st.markdown(f"**Message:** {message}")
    st.markdown(f"**Scheduled Time:** {hour_input:02d}:{min_input:02d}")

    if st.button("📤 Send WhatsApp Message"):
        try:
            st.info("Opening WhatsApp Web. Please scan QR if not already logged in.")
            kit.sendwhatmsg(phone, message, hour_input, min_input, wait_time=10, tab_close=True)
            st.success("✅ Message Scheduled Successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Run the function when script executes
if __name__ == "__main__":
    send_whatsapp()
