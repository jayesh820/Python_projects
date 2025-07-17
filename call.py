from twilio.rest import Client

# -----------------------------
# ✅ Replace with your Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'        # e.g., 'ACxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'YOUR_AUTH_TOKEN'          # e.g., 'a1b2c3d4e9j0'
twilio_number = '+1415XXXXX'          # Your Twilio phone number
receiver_number = '+91XXXXXXXX'       # Verified number (yours, with country code)

# -----------------------------
# ✅ Message to be played during the call
twiml_url = 'http://demo.twilio.com/docs/voice.xml'  # Default Twilio message

# -----------------------------
# ✅ Make the call
try:
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=receiver_number,
        from_=twilio_number,
        url=twiml_url
    )

    print(f"✅ Call initiated successfully! Call SID: {call.sid}")

except Exception as e:
    print(f"❌ Failed to make the call: {e}")
