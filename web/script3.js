const questions = [
    {
        question : "What is the determinant of a 2x2 identity matrix?",
        options : ["0", "1", "-1", "2"],
        answer : "1"
    },
    {
        question: "According to Gauss's Law, the electric flux through a closed surface is proportional to what?",
        options: ["The surface area", "The enclosed charge", "The external electric field", "The volume"],
        answer: "The enclosed charge"
    },
    {
        question: "What is the output of a standard 2-input XOR gate when both inputs are 1?",
        options: ["0", "1", "High-Z", "Undefined"],
        answer: "0"
    },
    {
        question : "\"Wings of Fire\" is the autobiography of ......",
        options : ["Mahatma Gandhi", "Swami Vivekanand", "Ramakrishna Paramhans", "Dr. APJ Abdul Kalam"],
        answer : "Dr. APJ Abdul Kalam"
    },
    {
        question : "Which of the following is not a programming language?",
        options : ["Python", "JavaScript", "HTML", "C++"],
        answer : "HTML"
    },
    {
        question : "What is the capital of France?",
        options : ["Berlin", "Madrid", "Paris", "Rome"],
        answer : "Paris"
    },
    {
        question : "Which planet is known as the Red Planet?",
        options : ["Earth", "Mars", "Jupiter", "Saturn"],
        answer : "Mars"
    },
    {
        question : "What is the largest mammal in the world?",
        options : ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        answer : "Blue Whale"
    },
    {
        question : "Who wrote the play 'Romeo and Juliet'?",
        options : ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        answer : "William Shakespeare"
    },
    {
        question : "What gas do plants use for photosynthesis?",
        options : ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        answer : "Carbon Dioxide"
    },
    {
        question : "What is money mainly used for?",
        options : ["communications", "transportation", "exchange of goods and services", "entertainment"],
        answer : "exchange of goods and services"
    },
    {
        question : "Which of the following is a renewable source of energy?",
        options : ["Coal", "Natural Gas", "Solar Energy", "Oil"],
        answer : "Solar Energy"
    },
    {
        question : "What is the chemical symbol for water?",
        options : ["H2O", "CO2", "O2", "NaCl"],
        answer : "H2O"
    },
    {
        question : "Who is known as the Father of Computers?",
        options : ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
        answer : "Charles Babbage"
    },
    {
        question : "What is the largest organ in the human body?",
        options : ["Heart", "Liver", "Skin", "Brain"],
        answer : "Skin"
    },
    {
        question : "Which of the following is not a primary color?",
        options : ["Red", "Green", "Blue", "Yellow"],
        answer : "Yellow"
    },
    {
        question : "What is the speed of light in a vacuum?",
        options : ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s"],
        answer : "300,000 km/s"
    },
    {
        question : "Who painted the Mona Lisa?",
        options : ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"],
        answer : "Leonardo da Vinci"
    },
    {
        question : "What is the smallest prime number?",
        options : ["0", "1", "2", "3"],
        answer : "2"
    }
];

let score = 0;
let time = 30;
let QuestionIndex = 0;
let currentQuestion;
let selectedOption = null;
let timer;

const timeleft = document.getElementById('time-left');
const timeleftContainer = document.getElementById('t');
const questionElement = document.getElementById('question');
const options = [
    document.getElementById('option1'),
    document.getElementById('option2'),
    document.getElementById('option3'),
    document.getElementById('option4')
];
const questionNumber = document.getElementById('number');
const nextButton = document.getElementById('next');
const submitButton = document.getElementById('submit');
const progressBar = document.getElementById('progress-bar');
const scoreText = document.getElementById('score-text');

questions.sort(() => Math.random() - 0.5);

function startTimer() {
    clearInterval(timer);

    timer = setInterval(() => {
        timeleft.innerText = time;
        time--;

        if (time < 0) {
            clearInterval(timer);
            alert("Time's up!");
            loadQuestion();
        }
    }, 1000);
}


function loadQuestion() {
    if (QuestionIndex >= 10) {
        endQuiz();
        return;
    }

    time = 30;
    selectedOption = null;

    options.forEach(opt => {
        opt.style.backgroundColor = "";
        opt.style.color = "";
        opt.style.pointerEvents = "auto";
    });

    currentQuestion = questions[QuestionIndex];
    questionNumber.innerText = `Question ${QuestionIndex + 1}`;
    questionElement.innerText = currentQuestion.question;

    options.forEach((opt, index) => {
        opt.innerText = currentQuestion.options[index];
    });

    startTimer();
}

options.forEach(option => {
    option.addEventListener('click', () => {
    
        options.forEach(opt => {
            opt.style.backgroundColor = "";
            opt.style.color = "";
        });

        option.style.backgroundColor = "white";
        option.style.color = "black";

        selectedOption = option;
    });
});

function checkAnswer() {
    if (!selectedOption) {
        alert("Please select an option first!");
        return;
    }

    clearInterval(timer);

    if (selectedOption.innerText === currentQuestion.answer) {
        score += 10;
        selectedOption.style.backgroundColor = "lightgreen";
    } 
    else {
        selectedOption.style.backgroundColor = "lightcoral";
        options[currentQuestion.options.indexOf(currentQuestion.answer)].style.backgroundColor = "lightgreen";
    }
    updateProgress();

    options.forEach(opt => opt.style.pointerEvents = "none");

    setTimeout(() => {
        QuestionIndex++;
        loadQuestion();
    }, 1000);
    
}

nextButton.addEventListener('click', checkAnswer);

function endQuiz() {
    if (score === 100) {
        questionElement.innerText = `Perfect Score! Congratulations! Your score: ${score}`;
    } else if (score >= 70) {
        questionElement.innerText = `Great Job! Your score: ${score}`;
    } else if (score >= 40) {
        questionElement.innerText = `Good Effort! Your score: ${score}`;
    } else {
        questionElement.innerText = `Better Luck Next Time! Your score: ${score}`;
    }
    timeleft.innerText = "";
    questionNumber.innerText = "";
    options.forEach(opt => opt.style.display = "none");
    nextButton.style.display = "none";
    timeleftContainer.style.display = "none";
    submitButton.innerText = "Restart Quiz";
    submitButton.onclick = () => { location.reload(); };
}
submitButton.addEventListener('click', endQuiz);

function updateProgress() {;
    progressBar.style.width = score + "%";
    scoreText.innerText = `Score: ${score}/${100}`;
}

loadQuestion();
