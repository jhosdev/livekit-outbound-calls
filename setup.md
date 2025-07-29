# Setup Instructions

This guide will help you set up the development environment for the LiveKit outbound calls project.

## Prerequisites

- Python 3.13 or higher
- uv (Python package manager)

## Environment Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jhosdev/livekit-outbound-calls.git
cd livekit-outbound-calls
```

### 2. Sync dependencies

```bash
uv sync
```

### 3. Download agent files from LiveKit

```bash
uv run agent download-files
```

### 4. Run the agent

#### Speak directly in terminal

```bash
uv run agent console
```

#### Use with telephony/frontend

```bash
uv run agent dev
```

#### Run in production

```bash
uv run agent start
```