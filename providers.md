# Providers

This project creates AI-driven voice interactions that can handle phone calls. To build a complete AI calling system, you need several key components working together. Each provider below offers a **generous free tier**, making this an accessible and cost-effective solution for development and testing.

## Essential Components for AI Calls

Building an AI calling system requires five core components:

1. **Real-time Media Infrastructure** - Handles audio streaming, WebRTC connections, and SIP protocol integration
2. **Speech-to-Text (STT)** - Converts incoming audio to text for AI processing  
3. **AI Language Model** - Processes conversations, understands context, and generates responses
4. **Text-to-Speech (TTS)** - Converts AI responses back to natural-sounding audio
5. **Telephony Infrastructure** - Connects to traditional phone networks (PSTN) for outbound calling

## Our Provider Choices

### LiveKit - Real-time Media Infrastructure

**Why LiveKit:**  
LiveKit powers the core real-time media layer and is the same technology behind major AI voice applications like ChatGPT's voice mode. It provides enterprise-grade WebRTC infrastructure with excellent SIP integration.

**Usage in this project:**  
- Creates voice rooms and handles audio transmission
- Manages SIP integration for connecting to phone networks
- Provides the foundational infrastructure for real-time audio streaming
- Handles media encoding/decoding and network optimization

**How to Set Up:**
1. Go to [livekit.io](https://livekit.io) and sign up for a free account
2. Create a project and obtain your credentials
3. Set the values in your `.env` file:
   ```env
   LIVEKIT_API_KEY=your_api_key
   LIVEKIT_API_SECRET=your_api_secret
   LIVEKIT_URL=https://your-instance.livekit.cloud
   ```

**Free Tier:** Generous limits for development including substantial monthly minutes and concurrent connections.

### Deepgram - Speech-to-Text

**Why Deepgram:**  
Industry-leading accuracy with ultra-low latency, essential for natural real-time conversations. Deepgram's streaming capabilities ensure minimal delay between speech and transcription.

**Usage in this project:**  
- Transcribes incoming audio from callers in real-time
- Converts speech to text for AI processing
- Handles streaming audio with minimal delay for natural conversations

**How to Set Up:**
1. Visit [deepgram.com](https://deepgram.com) and create a free account
2. Navigate to your dashboard and generate an API key
3. Add to your `.env` file:
   ```env
   DEEPGRAM_API_KEY=your_api_key
   ```

**Free Tier:** $200 in free credits plus ongoing free tier with substantial monthly transcription hours.

### Gemini - AI Language Model

**Why Gemini:**  
Google's Gemini offers excellent performance with very generous free tiers and strong function calling capabilities for dynamic interactions.

**Usage in this project:**  
- Processes transcribed text to understand user intent
- Generates contextually appropriate responses
- Maintains conversation state and handles complex dialogue flows
- Integrates with function calling for dynamic actions

**How to Set Up:**
1. Visit [ai.google.dev](https://ai.google.dev) and get access to Gemini API
2. Create an API key in the Google AI Studio
3. Add to your `.env` file:
   ```env
   GEMINI_API_KEY=your_api_key
   ```

**Free Tier:** Very generous free quota with high rate limits, perfect for development and moderate production use.

### Cartesia - Text-to-Speech

**Why Cartesia:**  
Ultra-fast, high-quality speech synthesis specifically optimized for real-time conversational applications with minimal latency.

**Usage in this project:**  
- Converts AI-generated responses to natural-sounding speech
- Streams audio back to callers with minimal latency
- Provides various voice options for different use cases

**How to Set Up:**
1. Go to [cartesia.ai](https://cartesia.ai) and sign up for an account
2. Get your API key from the dashboard
3. Add to your `.env` file:
   ```env
   CARTESIA_API_KEY=your_api_key
   ```

**Free Tier:** Generous monthly character limits perfect for development and testing.

### Twilio - Telephony Infrastructure

**Why Twilio:**  
Reliable SIP trunking and telephony infrastructure with excellent LiveKit integration for connecting to traditional phone networks.

**Usage in this project:**  
- Provides phone numbers for outbound calling
- Handles SIP protocol integration with LiveKit
- Manages call routing and telephony infrastructure
- Enables connection to PSTN (Public Switched Telephone Network)

**Internal Connection Setup:**
Unlike other providers, Twilio requires internal connection handling where we configure SIP trunks that integrate with LiveKit. This involves:

1. **Twilio SIP Trunk Setup** - Creating a SIP trunk in Twilio with proper termination URLs
2. **LiveKit Outbound Trunk Configuration** - Setting up the outbound trunk in LiveKit that connects to your Twilio SIP trunk
3. **Trunk ID Integration** - Using the LiveKit-generated trunk ID in your application

**How to Set Up:**
1. Create an account at [twilio.com](https://twilio.com)
2. Follow the Twilio SIP trunk setup guide: [Configuring Twilio Trunk](https://docs.livekit.io/sip/quickstarts/configuring-twilio-trunk/)
3. Configure the outbound trunk in LiveKit: [LiveKit SIP Setup](https://docs.livekit.io/sip/quickstarts/configuring-sip-trunk/#livekit-setup)
4. Get your verified phone number from Twilio for testing
5. Obtain the SIP outbound trunk ID from your LiveKit dashboard after configuration

**Environment Variables:**
```env
SIP_OUTBOUND_TRUNK_ID=your_livekit_trunk_id
PHONE_NUMBER=your_verified_twilio_number
```

**Free Tier:** $15 in free credits to get started, plus competitive per-minute pricing.

## Complete Environment Setup

Create a `.env` file in your project root with all the required keys:

```env
# LiveKit - Real-time Media Infrastructure
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=https://your-instance.livekit.cloud

# Deepgram - Speech-to-Text
DEEPGRAM_API_KEY=your_deepgram_api_key

# Gemini - AI Language Model
GEMINI_API_KEY=your_gemini_api_key

# Cartesia - Text-to-Speech
CARTESIA_API_KEY=your_cartesia_api_key

# Twilio/LiveKit - Telephony Infrastructure
SIP_OUTBOUND_TRUNK_ID=your_livekit_trunk_id
PHONE_NUMBER=your_verified_twilio_number
```

Note: The phone number should be a verified number from your Twilio account for testing purposes. The SIP outbound trunk ID comes from LiveKit after configuring your Twilio SIP trunk integration.