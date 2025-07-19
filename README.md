# 🥗 AI-Powered Diet Planner

A smart, fun, and personalized diet planning web app built using **Flask**, **MongoDB**, and **Generative AI** (Gemini). Users can generate daily diet plans, save their profile, and download the plan as a beautiful PDF.

---

## 🚀 Features

- 🍎 **User Profile Creation** – Stores age, weight, height, preferences, allergies, and goals
- 🧠 **AI Meal Generator** – Uses Gemini API to generate customized meals
- 🥘 **Cuisine & Spice Preferences** – Indian, Continental, Spicy, Mild, etc.
- 📅 **Daily Plan Generation** – Choose the day and get unique meals
- 📄 **PDF Download** – Export your plan in a printable format
- 🧠 **Fallback Diet Logic** – When no AI key is available
- ☁️ **Deployed on Render**

---

## 🛠️ Tech Stack

| Tech        | Usage                          |
|-------------|--------------------------------|
| Flask       | Backend server (Python)        |
| MongoDB     | Database for storing profiles  |
| HTML/CSS    | Frontend & UI                  |
| Gemini API  | AI-generated meals             |
| Render      | Hosting and deployment         |

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/yashitiwary/diet-planner2.git
cd diet-planner2
pip install -r requirements.txt
