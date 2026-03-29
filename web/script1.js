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
    }
];

let score = 0;
let time = 30;
let QuestionIndex = 0;

const timeleft = document.getElementById('time-left');
const q_element = document.getElementById('question');
const option1 = document.getElementById('option1');
const option2 = document.getElementById('option2');
const option3 = document.getElementById('option3');
const option4 = document.getElementById('option4');
const nextBtn = document.getElementById('next');
const submitBtn = document.getElementById('submit');
const q_number = document.getElementById('number');


// function timeLeft() {
//     timeleft.innerText = time;
//     setTimeout(() => {
//         time--;
//         timeLeft();
//     }, 1000);
//     if(time <= 0) {
//         alert("Time's up!!!");
//         loadQuestion();
//     }
// }

function loadQuestion() {
    time = 30;
    // timeLeft();
    QuestionIndex++;
    q_number.innerText = "Q" + QuestionIndex;
    if(score < (questions.length)*10) {
        // const randomIndex = Math.floor(Math.random() * questions.length);
        const currentQuestion = questions[QuestionIndex-1];
        q_element.innerText = currentQuestion.question;
        option1.innerText = currentQuestion.options[0];
        option2.innerText = currentQuestion.options[1];
        option3.innerText = currentQuestion.options[2];
        option4.innerText = currentQuestion.options[3];
        option1.addEventListener('click', () => {
            if(currentQuestion.options[0] === currentQuestion.answer) {
                score += 10;

            }
        });
        option2.addEventListener('click', () => {
            if(currentQuestion.options[1] === currentQuestion.answer) {
                score += 10;
            }
        });
        option3.addEventListener('click', () => {
            if(currentQuestion.options[2] === currentQuestion.answer) {
                score += 10;
            }
        });
        option4.addEventListener('click', () => {
            if(currentQuestion.options[3] === currentQuestion.answer) {
                score += 10;
            }
        });
    }
    else {
        alert("Quiz Completed!!! Your score is " + score);
    }
}

// function nextQuestion() {
//     if(score < (questions.length)*10) {
//         loadQuestion();
//     } else {
//         alert("Quiz Completed!!! Your score is " + score);
//     }
// }
nextBtn.addEventListener('click', loadQuestion);
submitBtn.addEventListener('click', () => {
    alert("Quiz Completed!!! Your score is " + score);
});

loadQuestion();
