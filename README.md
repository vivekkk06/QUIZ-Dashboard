# 🧠 Quiz Application

A simple and interactive Quiz Web App built using **HTML, CSS, and JavaScript**.
This app presents multiple-choice questions, tracks the user’s score, includes a countdown timer, and displays a progress bar.

---

## 🚀 Features

* ✅ Multiple-choice questions
* ⏱️ Countdown timer for each question
* 🎯 Score tracking system
* 📊 Live progress bar based on score
* 🎨 Visual feedback (correct/wrong answers)
* 🔒 Prevents multiple selections after answering
* 🔁 Restart quiz functionality
* 🎲 Randomized question order (shuffle)

---

## 📁 Project Structure

```
📦 Quiz-App
 ┣ 📜 WELCOME.html   # welcoming the user
 ┣ 📜 style0.css     # Styling (UI design) of welcome page
 ┣ 📜 q1.html        # Main HTML file or question file
 ┣ 📜 style1.css     # Styling (UI design) questions
 ┣ 📜 script3.js     # Quiz logic (JavaScript)
 ┗ 📜 README.md      # Project documentation
```

---

## 🛠️ Technologies Used

* HTML5 – Structure of the web page
* CSS3 – Styling and layout
* JavaScript (ES6) – Logic and interactivity

---

## ⚙️ How It Works

1. Questions are stored in an array.
2. The array is shuffled using:

   ```js
   questions.sort(() => Math.random() - 0.5);
   ```
3. One question is displayed at a time.
4. User selects an option and clicks **Next**.
5. The app:

   * Checks the answer
   * Updates the score
   * Highlights correct/wrong answers
6. Progress bar updates dynamically.
7. Timer resets for each question.
8. After all questions, the final score is shown.

---

## ▶️ How to Run

1. Download or clone the repository
2. Open `q1.html` in any browser
3. Start the quiz 

---

## 🎮 Controls

* **Click an option** → Select your answer
* **Next button** → Submit answer & go to next question
* **Timer** → Auto moves to next question if time runs out

---

## 🧩 Key Concepts Used

* DOM Manipulation
* Event Handling
* Arrays & Objects
* Timers (`setInterval`, `clearInterval`)
* Dynamic UI updates

---

## ⚠️ Known Limitations

* Uses basic shuffle (not perfectly random)
* No backend (scores not saved permanently)
* No category/difficulty selection

---

## 🔮 Future Improvements

* 📊 Leaderboard with localStorage
* 🎨 Improved UI/animations
* 📱 Mobile responsiveness
* 🔊 Sound effects
* 🌐 Backend integration for user accounts

---

## 🙌 Author
Nitin Thakur && VIVEK BADGUJAR
