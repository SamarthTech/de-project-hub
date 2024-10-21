let choice = document.querySelectorAll(".choice");
let msg = document.querySelector("#result");
let scuser=document.querySelector("#scuser");
let sccomp=document.querySelector("#sccomp");

let userscore = 0;
let compscore = 0;

const compChoice = () => {
    const options = ["rock", "paper", "scissors"];
    const index = (Math.floor(Math.random() * 3));
    return options[index];
}


choice.forEach((choice) => {
    choice.addEventListener("click", () => {
        const userChoice = choice.getAttribute("id");
        playGame(userChoice);
    })
})

const playGame = (userChoice) => {
    let userWin = true;
    const computerchoice = compChoice();
    console.log("Computer Choice is", computerchoice);
    console.log("User Choice is ", userChoice);
    if (userChoice === computerchoice) {
        drawGame();
    }
    else {
        if (userChoice === "rock") {
            userWin = computerchoice === "paper" ? false : true;
        }
        else if (userChoice === "paper") {
            userWin = computerchoice === "scissors" ? false : true;
        }
        else {
            userWin = computerchoice === "rock" ? false : true;
        }
    }
    showWinner(userWin);
}


const drawGame = () => {
    console.log("The Game was Draw");
}


const showWinner = (userWin) => {
    if (userWin) {
        msg.innerText = "User Won";
    }
    else {
        msg.innerText = "Computer Won";
    }
}

const updateScore =()=>{
    if (userWin) {
        scuser
    }
    else {
        msg.innerText = "Computer Won";
    }
}


