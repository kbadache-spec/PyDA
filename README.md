# PyDA
Python Desktop Assistant


**PyDA** (Python Desktop Assistant) is a beautifully styled, lightweight virtual assistant built with **Python** and **Tkinter**. Powered by the **WolframAlpha** and **Wikipedia** APIs, it's designed to answer your questions in real time.

---

## 🎨 Features & Design

* **Smart Fallback Logic:** PyDA queries WolframAlpha first for precise computational answers. If the question is more conversational or academic, it seamlessly falls back to Wikipedia to fetch a quick 2-sentence summary.
* **Cozy Aesthetic:** Hand-picked color scheme featuring deep plum (`#66545e`), dusty rose (`#aa6f73`), and warm cream (`#f6e0b5`) for an interface that is gentle on the eyes
* **Production-Ready Security:** API credentials are completely isolated from the source code using environment variables, ensuring zero exposure on public repositories.

---

## 🎮 How to Use

1. Launch the application.
2. Type any question into the input field (e.g., *"What is the distance to the moon?"* or *"Who was Albert Einstein?"*).
3. Hit **Enter** and watch PyDA fetch your answer in seconds!

---

## 🛠️ Installation & Setup

To run PyDA locally on your machine, follow these quick steps:

### 1. Clone the Workspace
 ```bash
 git clone [https://github.com/YOUR_USERNAME/PyDA-Desktop-Assistant.git](https://github.com/YOUR_USERNAME/PyDA-   Desktop-Assistant.git)
 cd PyDA-Desktop-Assistant


### 2. Install Dependencies
  ```bash
  pip install requests wikipedia python-dotenv

### 3. 3. Configure Your Secret API Key 🔑
You will need to plug in your own free WolframAlpha App ID:

Sign up for a developer account at WolframAlpha.

Create a new App ID.

In the root folder of this project, create a file named exactly .env.

Add your key inside the file like this (no spaces, no quotes!):
```bash
WOLFRAM_APP_ID=YOUR_ACTUAL_APP_ID_HERE

## 4. Run the Assistant! 🚀
Launch the user interface by running GUI.py:
```bash
python GUI.py
