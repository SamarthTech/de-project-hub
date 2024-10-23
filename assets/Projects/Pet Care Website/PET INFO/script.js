function checkAnswer(answer) {
  const result = document.getElementById('result');
  if (answer === 'Dogs') {
      result.textContent = 'Correct! Dogs are the most popular pet in the whole world!';
      result.style.color = 'green';
  } else {
      result.textContent = 'Sorry, that\'s not correct. Try again!';
      result.style.color = 'red';
  }
}