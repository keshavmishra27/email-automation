# Email Automation Tool

A lightweight, automated email notification system built with Python. This tool reads a list of recipient emails from a text file and sends automated daily updates using SMTP.

## 🚀 Tech Stack

```mermaid
graph TD
    %% Node Definitions
    Python([<b>Python 3.x Environment</b>])
    SMTP[smtplib<br/><i>SMTP Client</i>]
    Email[email.message<br/><i>Email Building</i>]
    OS[os module<br/><i>Security & Config</i>]
    GmailServer{<b>Gmail SMTP Server</b>}
    DotEnv[[<b>.env File</b><br/>Credentials]]

    %% Connections
    Python --> SMTP
    Python --> Email
    Python --> OS
    SMTP --> GmailServer
    OS --> DotEnv

    %% Styling
    classDef main fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff;
    classDef tools fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff;
    classDef external fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff;
    classDef config fill:#f1c40f,stroke:#f39c12,stroke-width:2px,color:#333;

    class Python main;
    class SMTP,Email,OS tools;
    class GmailServer external;
    class DotEnv config;
```

## 🔄 Workflow Flowchart

```mermaid
flowchart LR
    %% Workflow Steps
    S([<b>🚀 Start Script</b>])
    L1[<b>📂 Load Recipient List</b><br/>emails.txt]
    L2[<b>🔑 Load Credentials</b><br/>.env]
    D{<b>For each<br/>Recipient</b>}
    C[<b>✉️ Build Email</b><br/>Daily Content]
    S1[<b>🔐 Establish SSL</b><br/>Port 465]
    L3[<b>👤 SMTP Login</b>]
    S2[<b>📧 Send Message</b>]
    N{<b>Success?</b>}
    E([<b>🏁 End Process</b>])

    %% Logic Flow
    S --> L1 --> L2 --> D
    D --> C --> S1 --> L3 --> S2 --> N
    N -- Yes --> D
    N -- No --> E
    D -- Finished --> E

    %% Astonishing Styling
    style S fill:#ff9f43,stroke:#ee5253,stroke-width:4px,color:#fff
    style E fill:#ee5253,stroke:#ff9f43,stroke-width:4px,color:#fff
    style D fill:#5f27cd,stroke:#341f97,stroke-width:2px,color:#fff
    style N fill:#1dd1a1,stroke:#10ac84,stroke-width:2px,color:#fff
    
    classDef action fill:#48dbfb,stroke:#0abde3,stroke-width:2px,color:#333;
    class L1,L2,C,S1,L3,S2 action;

    %% Add some cool gradients/shadows logic via link styling
    linkStyle default stroke:#576574,stroke-width:2px,transition:1s;
```

## 🛠️ Setup & Configuration

1. **Environment Variables**: Create a `.env` file in the root directory with the following:
   ```env
   EMAIL_ADDRESS=your-email@gmail.com
   APP_PASSWORD=your-app-password
   ```

2. **Recipient List**: List your recipient emails in `emails.txt` (one per line).

3. **Usage**:
   ```bash
   python send_email.py
   ```

## 📝 Latest Changes
- Automated daily update content integration.
- Enhanced recipient validation.
- Secure connection using SSL on port 465.