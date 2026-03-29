// Quiz Data
const quizData = [
    {
        question: "What is the determinant of a 2x2 identity matrix?",
        options: ["0", "1", "-1", "2"],
        correctAnswer: "1"
    },
    {
        question: "During gene expression, which molecule carries the genetic code from DNA to the ribosome?",
        options: ["tRNA", "rRNA", "mRNA", "ATP"],
        correctAnswer: "mRNA"
    },
    {
        question: "According to Gauss's Law, the electric flux through a closed surface is proportional to what?",
        options: ["The surface area", "The enclosed charge", "The external electric field", "The volume"],
        correctAnswer: "The enclosed charge"
    },
    {
        question: "What is the output of a standard 2-input XOR gate when both inputs are 1?",
        options: ["0", "1", "High-Z", "Undefined"],
        correctAnswer: "0"
    }
];

// State Variables
let currentQuestionIndex = 0;
let score = 0;
let timeLeft = 15;
let timerInterval;

// DOM Elements
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.getElementById('result-screen');
const questionText = document.getElementById('question-text');
const optionsContainer = document.getElementById('options-container');
const timerElement = document.getElementById('time-left');
const questionTracker = document.getElementById('question-tracker');

// Event Listeners
document.getElementById('start-btn').addEventListener('click', startQuiz);
document.getElementById('restart-btn').addEventListener('click', resetQuiz);

function startQuiz() {
    startScreen.classList.remove('active');
    quizScreen.classList.add('active');
    loadQuestion();
}

function loadQuestion() {
    // Reset timer
    clearInterval(timerInterval);
    timeLeft = 15;
    timerElement.innerText = timeLeft;
    
    const currentQ = quizData[currentQuestionIndex];
    questionText.innerText = currentQ.question;
    questionTracker.innerText = `Question ${currentQuestionIndex + 1}/${quizData.length}`;
    
    // Render options
    optionsContainer.innerHTML = '';
    currentQ.options.forEach(option => {
        const button = document.createElement('button');
        button.innerText = option;
        button.classList.add('option-btn');
        button.addEventListener('click', () => checkAnswer(button, option, currentQ.correctAnswer));
        optionsContainer.appendChild(button);
    });

    startTimer();
}

function startTimer() {
    timerInterval = setInterval(() => {
        timeLeft--;
        timerElement.innerText = timeLeft;
        
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            handleTimeout();
        }
    }, 1000);
}

function checkAnswer(selectedButton, selectedAnswer, correctAnswer) {
    clearInterval(timerInterval);
    
    // Disable all buttons to prevent multiple clicks
    const allButtons = optionsContainer.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true);

    if (selectedAnswer === correctAnswer) {
        selectedButton.classList.add('correct');
        score++;
    } else {
        selectedButton.classList.add('wrong');
        // Highlight correct answer
        allButtons.forEach(btn => {
            if (btn.innerText === correctAnswer) btn.classList.add('correct');
        });
    }

    setTimeout(nextQuestion, 1500); // Wait 1.5 seconds before moving on
}

function handleTimeout() {
    const allButtons = optionsContainer.querySelectorAll('.option-btn');
    allButtons.forEach(btn => {
        btn.disabled = true;
        if (btn.innerText === quizData[currentQuestionIndex].correctAnswer) {
            btn.classList.add('correct');
        }
    });
    setTimeout(nextQuestion, 1500);
}

function nextQuestion() {
    currentQuestionIndex++;
    if (currentQuestionIndex < quizData.length) {
        loadQuestion();
    } else {
        endQuiz();
    }
}

function endQuiz() {
    quizScreen.classList.remove('active');
    resultScreen.classList.add('active');
    document.getElementById('final-score').innerText = score;
    document.getElementById('total-questions').innerText = quizData.length;
}

function resetQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    resultScreen.classList.remove('active');
    startScreen.classList.add('active');
}