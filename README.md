# Join the discord with 17,000+ Members! 

Our Discord: https://discord.gg/slayerlegend

<img width="526" height="296" alt="image" src="https://github.com/user-attachments/assets/0a647bb7-32ee-4f34-9e01-705afcba833d" />

Official Game can be downloaded here: https://play.google.com/store/apps/details?id=com.gear2.growslayer&hl=en_US&gl=US

# ⚔️ Slayer Legend Discord Bot

A robust, scalable Discord bot engineered to support and enhance the player experience within the **Slayer Legend** community. This bot serves as an intelligent assistant, delivering game-specific builds, community ticketing workflows, and progression calculators with clean embedded responses and command routing.

---

## 🧠 Overview

Designed with extensibility and performance in mind, this project demonstrates real-world applications of:

- Event-driven architecture (via `discord.py`)
- Dynamic embed generation for content-rich messaging
- Role-sensitive ticketing workflows with permission control
- Regex-driven parsing for multi-modal command inputs
- Modular design enabling scalability across game content updates

---

## 🔑 Key Features

### 📘 Guide and Build Command System
- Provides **minimum viable loadouts** for over a dozen game contexts:
  - Stage farming, closed mines, training cave, spirit dungeon
  - Boss fights, promotions (Mithril → Dragonos), and special events
- Uses custom emoji and embedded formatting for a visually guided experience
- Supports aliases and fallback logic for alternate command calls

### 🧮 Equipment Cost Calculator
- `!equip` command computes resource requirements (e.g. diamonds) for summoning upgrades
- Implements a progressive calculation algorithm with residual rollovers for tiered costs

### 🧾 Ticketing and Moderation Suite
- Role-based **ticket creation system** with dropdown support and per-category logic
- Permissions are dynamically applied based on ticket type (Support vs Master Slayer)
- Logs edited and deleted messages server-wide for audit visibility

### 👤 Utility Commands
- `!avatar` to preview user avatars
- `!new`, `!guide`, `!growth`, `!miscguides` to streamline onboarding and access to external documentation

---

## 🧰 Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Bot Core    | [discord.py](https://discordpy.readthedocs.io/) |
| Env Config  | `python-dotenv`   |
| Async Logic | `asyncio`         |
| Input Logic | `re`, `math.ceil` |

---

## 🚀 Getting Started

1. Clone the repository.
2. Create a `.env` file in the root directory and add your bot token:

## Demonstration & Usage
### **Ticketing System for Management**

![image](https://github.com/Erebonia/Discord-Bot-Slayer-Legend-Public/assets/52137104/138bd2fe-bb58-4120-b29b-5fbe3bc2140c)

### **Command List:**

![image](https://github.com/Erebonia/Discord-Bot-Slayer-Legend-Public/assets/52137104/19dc9768-eba1-48e7-ae59-a0696c2fe4e9)


### **Sample Output:**

![image](https://github.com/Erebonia/Discord-Bot-Slayer-Legend-Public/assets/52137104/62fe3dfd-e52d-43d2-9a74-14c93879c0d2)



