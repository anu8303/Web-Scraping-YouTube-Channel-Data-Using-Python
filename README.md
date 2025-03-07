# 🎧 YouTube Channel Scraper using Selenium  

## 🚀 Overview  
This Python script scrapes YouTube channels based on a search query (e.g., "Fitness in India") and saves details into a CSV file. It extracts essential information such as:
- **Channel Name**  
- **Channel URL**  
- **Description**  
- **Subscriber Count**  

The script is optimized for **Google Colab** and uses Selenium for web automation.

---

## 🛠️ Installation & Setup  
### **1️⃣ Install Dependencies**  
Run the following commands in your **Google Colab notebook**:  

```sh
!apt-get update
!apt install -y libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1
!pip install selenium webdriver-manager
```

---

### **2️⃣ Clone Repository (Optional)**  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

---

### **3️⃣ Run the Script**  
```sh
python youtube_scraper.py
```

---

## 📂 Output Format  
The extracted data is saved in **`youtube_channels.csv`**, structured as follows:

| Channel URL | Name | Description | Subscriber Count |
|------------|------|-------------|------------------|
| youtube.com/c/example | Example Channel | This is a test | 1M |

---

## 🔧 Tech Stack  
- **Python**  
- **Selenium (Web Scraping & Automation)**  
- **WebDriver Manager**  
- **CSV Module**  

---

## 🚀 Features  
- Extracts **channel details from YouTube search results**  
- Uses **Selenium WebDriver** to interact with dynamic content  
- Saves data in **CSV format**  
- Works in **Google Colab** with headless Chrome  
- Includes **error handling for missing data**  

---

## 👨‍💻 Author  
**Anushka**  
🔗 [GitHub Profile](https://github.com/YOUR_GITHUB_USERNAME)  

---

## 📚 License  
This project is **open-source** under the [MIT License](LICENSE).  

---

## 🔄 Contributing  
Feel free to submit **pull requests** to improve this project! 🚀
