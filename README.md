# livekit-outbound-calls

**Outbound AI-Powered Call System with LiveKit**

This project provides a flexible and modular setup for making outbound calls using [LiveKit](https://livekit.io/), powered by speech recognition, AI models, and telephony providers. It integrates services like **Cartesia**, **Deepgram**, **Gemini**, and **Twilio** to create intelligent, real-time conversational agents over voice.

* * *

## 🔧 What It Does

- Initiates and manages outbound voice calls using LiveKit.
- Transcribes audio in real-time using Deepgram.
- Analyzes and responds using AI models like Gemini or OpenAI.
- Handles call flows, actions, and decisions via Cartesia.
- Uses Twilio for SIP connectivity.

* * *

## 💡 Motivation

While building AI-powered voice call systems, I encountered several limitations across available tools:

### 🧩 LiveKit

- LiveKit is a powerful and flexible open-source platform, but many of its examples for outbound calls are **incomplete**, **lacking clear explanations**, or assume a lot of prior context.
- This made it hard to understand how to glue together key components like signaling, media routing, and SIP for practical use cases.
- Despite these gaps, LiveKit remains a great open-source base — but it needs a more accessible, opinionated implementation for outbound AI agents.

### 🚫 Limitations of Commercial Tools (Synthflow, Vapi, etc.)

- Tools like **Synthflow** and **Vapi** promise ready-made agent infrastructure, but often come with:
  - **Inconsistent or undocumented APIs**
  - **Frequent errors** in payloads or runtime behavior
  - **Opaque architectures** that limit customization
  - **Unnecessary overhead** and opinionated UIs/workflows that get in the way of rapid prototyping
- These tools are also closed-source and lock you into their infrastructure.

### ✅ Why Open Source

This project embraces a fully open-source stack to:

- Maintain **full control** over how voice agents behave and evolve
- Ensure **transparency** at every step — from SIP signaling to AI response handling
- Keep costs low or zero by leveraging generous free tiers (LiveKit, Deepgram, OpenAI dev access, etc.)
- Enable faster iteration and learning for developers and researchers who want to build and test conversational agents in real-world conditions

Ultimately, this repo is about creating something **useful, understandable, and reproducible** — without relying on black-box solutions.

* * *

## Project Docs

For providers setup instructions, see [providers.md]

For how to install uv and Python, see [installation.md](installation.md).

For development workflows, see [development.md](development.md).

* * *

*This project was built from
[simple-modern-uv](https://github.com/jlevy/simple-modern-uv).*
