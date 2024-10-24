const quizData = [
    {
        question: "1.What is the capital of France?",
        a: "Berlin",
        b: "Madrid",
        c: "Paris",
        d: "Lisbon",
        correct: "c"
    },
    {
        question: "2.Who is the CEO of Tesla?",
        a: "Jeff Bezos",
        b: "Elon Musk",
        c: "Bill Gates",
        d: "Tony Stark",
        correct: "b"
    },
    {
        question: "3.What is the most used programming language in 2021?",
        a: "Java",
        b: "C",
        c: "Python",
        d: "JavaScript",
        correct: "d"
    },
    {
        question: "4.Who won the 2018 FIFA World Cup?",
        a: "Germany",
        b: "Argentina",
        c: "Brazil",
        d: "France",
        correct: "d"
    },
    {
        question: "5.What does HTML stand for?",
        a: "Hypertext Markup Language",
        b: "Hypertext Markdown Language",
        c: "Hyperloop Machine Language",
        d: "Helicopters Terminals Motorboats Lamborginis",
        correct: "a"
    },
     {
        question:"6.Who draw the monalisa?",
        a:  "Vincent van Gogh",
        b: "Pablo Picasso",  
        c: "Leonardo da Vinci",  
        d: "Michelangelo", 
        correct: "b"
        },
    {
       question:"7.What is the minimum age to become the Prime Minister of India?",
        a:  "26",  
        b: "30",  
        c: "25",  
        d: "27", 
        correct: "c"
        },
        {
        question:"8.How many continents are there in the world?",
        a: "5",  
        b: "7",  
        c: "9",  
        d: "8",  
         correct:"b"
        },
        {
            question:"9.Which planet is known as the Red Planet?",
            a: "Venus",  
            b: "Mars",  
            c:"Jupiter",  
            d: "Saturn",  
            correct: "b"
        },
        {   

        question:"10.Who wrote the play Romeo and Juliet?",
        a: "Charles Dickens", 
        b: "William Shakespeare",  
        c:"Mark Twain",
        d: "Leo Tolstoy",  
        correct: "b"
        }    
];
const quiz = document.getElementById('quiz');
const answersEls = document.querySelectorAll('.answer');
const questionEl = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitBtn = document.getElementById('submit');

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
    deselectAnswers();

    const currentQuizData = quizData[currentQuiz];

    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
}

function deselectAnswers() {
    answersEls.forEach(answerEl => answerEl.checked = false);
}

function getSelected() {
    let answer;
    answersEls.forEach(answerEl => {
        if (answerEl.checked) {
            answer = answerEl.id;
        }
    });
    return answer;
}

submitBtn.addEventListener('click', () => {
    const answer = getSelected();

    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }

        currentQuiz++;

        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {

            quiz.innerHTML = `
                <h2>You answered ${score}/${quizData.length} questions correctly.</h2>
                <h2>Your score=${score}</h2>
                <h3><a href="https://forms.gle/BYdDUY9GBJHx77is6"> Submit your score and experience in this form.</h3></a>
                <h3>Thanks for participate in our contest..</h3>
                <button onclick="location.reload()">Reload</button>
            `;

        }
    }
});