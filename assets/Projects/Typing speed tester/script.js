const paragraphs = [
    "The quick brown fox jumps over the lazy dog. This is a classic pangram used to showcase typefaces. It includes every letter in the English alphabet.",
    "Practice makes perfect. Keep typing to improve your speed and accuracy. The more you practice, the better you will get.",
    "A journey of a thousand miles begins with a single step. Each step you take leads you closer to your goal. Embrace the journey as much as the destination.",
    "To be or not to be, that is the question. This famous quote raises profound questions about existence. Every individual must grapple with their own purpose.",
    "Good things come to those who wait. Patience is often rewarded in life. In our fast-paced world, taking time can lead to better outcomes."
  ];
  
  
  let currentParagraph = "";
  let timer;
  let startTime;
  let isTyping = false;
  let isCompleted = false; // New flag to check if the test is completed
  
  function startTest() {
    currentParagraph = paragraphs[Math.floor(Math.random() * paragraphs.length)];
    displayText(currentParagraph);
    document.getElementById("text-input").value = "";
    document.getElementById("time").innerText = 0;
    document.getElementById("wpm").innerText = 0;
    document.getElementById("accuracy").innerText = 100;
    isTyping = false;
    isCompleted = false; // Reset completion status
    clearInterval(timer);
  }
  
  function displayText(text) {
    const display = document.getElementById("text-display");
    display.innerHTML = "";
    text.split("").forEach(char => {
      const span = document.createElement("span");
      span.innerText = char;
      display.appendChild(span);
    });
  }
  
  function startTimer() {
    startTime = new Date();
    timer = setInterval(updateTimer, 1000);
  }
  
  function updateTimer() {
    const timeTaken = Math.floor((new Date() - startTime) / 1000);
    document.getElementById("time").innerText = timeTaken;
  }
  
  function calculateResults() {
    const typedText = document.getElementById("text-input").value.trim();
    const originalText = currentParagraph.trim();
    
    // Split into words for counting
    const typedWords = typedText.split(/\s+/); // Split typed text into words
    const originalWords = originalText.split(/\s+/); // Split original text into words
    
    let correctWordCount = 0;
    
    // Count correctly typed words
    originalWords.forEach((word, index) => {
      if (typedWords[index] === word) {
        correctWordCount++;
      }
    });
  
    const timeTakenMinutes = (new Date() - startTime) / 1000 / 60; // Time in minutes
    const wpm = timeTakenMinutes > 0 ? Math.round(correctWordCount / timeTakenMinutes) : 0; // Avoid division by zero
    const accuracy = Math.round((correctWordCount / originalWords.length) * 100); // Calculate accuracy based on total words
  
    document.getElementById("wpm").innerText = wpm;
    document.getElementById("accuracy").innerText = accuracy;
  }
  
  document.getElementById("text-input").addEventListener("input", () => {
    if (isCompleted) return;  // Prevent updates if completed
  
    if (!isTyping) {
      startTimer();
      isTyping = true;
    }
  
    const typedText = document.getElementById("text-input").value;
    const originalText = currentParagraph;
  
    // Highlight characters in real-time
    const typedChars = typedText.split("");
    Array.from(document.getElementById("text-display").children).forEach((span, index) => {
      if (typedChars[index] === span.innerText) {
        span.classList.add("correct");
        span.classList.remove("incorrect");
      } else if (typedChars[index]) {
        span.classList.add("incorrect");
        span.classList.remove("correct");
      } else {
        span.classList.remove("correct", "incorrect");
      }
    });
  
    // Check for completion
    if (typedText === originalText) {
      clearInterval(timer);
      calculateResults();
      isTyping = false;
      isCompleted = true; // Set completion status to true
    }
  });
  
  startTest();
 
// Theme toggle function
function toggleTheme() {
    document.body.classList.toggle("dark");
    const theme = document.body.classList.contains("dark") ? "dark" : "light";
    localStorage.setItem("theme", theme);
    document.getElementById("theme-toggle").textContent = theme === "dark" ? "☀️ Light Mode" : "🌙 Dark Mode";
  }
  
  // Load theme on page load
  window.onload = () => {
    const theme = localStorage.getItem("theme") || "light";
    if (theme === "dark") document.body.classList.add("dark");
    document.getElementById("theme-toggle").textContent = theme === "dark" ? "☀️ Light Mode" : "🌙 Dark Mode";
  };