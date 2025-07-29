# livekit-outbound-calls

**Outbound AI-Powered Call System with LiveKit**

This project provides a flexible and modular setup for making outbound calls using [LiveKit](https://livekit.io/), powered by speech recognition, AI models, and telephony providers. It integrates services like **Cartesia**, **Deepgram**, **Gemini**, and **Twilio** to create intelligent, real-time conversational agents over voice.

* * *

## 🔧 What It Does

- Initiates and manages outbound voice calls using LiveKit.
- Transcribes audio in real-time using Deepgram.
- Analyzes and responds using AI models (Gemini as an initial provider).
- Handles call flows, actions, and decisions via Cartesia.
- Uses Twilio for SIP connectivity.

* * *

## 💡 Motivation

While building AI-powered voice call systems, I encountered several limitations across available tools and platforms:

### 🚫 Limitations of Commercial Tools (Synthflow, Vapi, etc.)

Tools like **Synthflow**, **Vapi** and similar commercial platforms promise ready-made agent infrastructure, but often come with significant drawbacks:

- **Inconsistent or undocumented APIs** that change without notice
- **Frequent errors** in payloads, runtime behavior, and unreliable service uptime
- **Opaque architectures** that limit customization and debugging capabilities
- **Unnecessary overhead** and opinionated UIs/workflows that get in the way of rapid prototyping
- **Vendor lock-in** with closed-source solutions that make migration difficult
- **High costs** that scale unpredictably as your usage grows
- **Limited control** over the underlying voice quality, latency, and conversation flow

> 💬 **Note:** In particular, **Synthflow** caused major setbacks in a previous company project. The platform had **poorly structured REST documentation**, **missing or unclear configuration options**, and excessive abstraction layers that made even simple workflows frustrating to implement. It ultimately introduced more friction than value for a technical team. We even lost agent settings overnight!

These tools may be convenient for non-technical users, but for developers who need flexibility, transparency, and control, they can become a serious bottleneck.



### ✅ Why LiveKit

**LiveKit** stands out as the superior foundation for voice AI applications:

- **Battle-tested infrastructure**: Powers major AI applications including **ChatGPT's voice mode**, proving its reliability at scale
- **Open-source transparency**: Full visibility into how your voice calls are handled
- **Professional-grade WebRTC**: Industry-leading audio quality and low-latency streaming
- **Flexible architecture**: Supports both simple demos and complex enterprise deployments
- **Active development**: Continuously improved by a dedicated team and community
- **Cost-effective**: Generous free tiers and predictable pricing that scales with your needs

### 🎯 Purpose of This Project

Despite LiveKit's technical excellence, there's a significant gap in accessible documentation and examples:

- **Incomplete examples**: Many LiveKit demos for outbound calls are **incomplete** or missing crucial integration steps
- **Lacking clear explanations**: Examples assume significant prior knowledge of WebRTC, SIP, and real-time media
- **Scattered documentation**: Key concepts are spread across multiple repos and docs without a cohesive learning path
- **Complex setup**: Getting from "hello world" to a working outbound AI agent requires piecing together multiple services

**This project bridges that gap** by providing:

- A **complete, working implementation** that connects all the necessary pieces
- **Clear, step-by-step setup** instructions for each provider and integration
- **Transparent architecture** that you can understand, modify, and extend
- **Production-ready patterns** for real-world voice AI applications
- **Comprehensive documentation** that explains not just how, but why each component works

### 🌟 Why Open Source

This project embraces a fully open-source stack to:

- Maintain **full control** over how voice agents behave and evolve
- Ensure **transparency** at every step — from SIP signaling to AI response handling
- Keep costs low by leveraging generous free tiers (LiveKit, Deepgram, Gemini, etc.)
- Enable faster iteration and learning for developers who want to build conversational agents
- Create a **reusable foundation** that others can build upon and improve

Ultimately, this repo is about creating something **useful, understandable, and reproducible** — without relying on black-box solutions or incomplete examples.

* * *

## Project Docs

For providers instructions, see [providers.md](providers.md).

For how to install uv and Python, see [installation.md](installation.md).

For development workflows, see [development.md](development.md).

For setup instructions, see [setup.md](setup.md).

* * *

*This project was built from
[simple-modern-uv](https://github.com/jlevy/simple-modern-uv).*
