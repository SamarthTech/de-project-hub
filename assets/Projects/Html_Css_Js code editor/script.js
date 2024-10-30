// Initialize CodeMirror for HTML, CSS, and JavaScript
const htmlEditor = CodeMirror.fromTextArea(document.getElementById("html-code"), {
  mode: "text/html",
  theme: "material",
  lineNumbers: true,
});

const cssEditor = CodeMirror.fromTextArea(document.getElementById("css-code"), {
  mode: "text/css",
  theme: "material",
  lineNumbers: true,
});

const jsEditor = CodeMirror.fromTextArea(document.getElementById("js-code"), {
  mode: "text/javascript",
  theme: "material",
  lineNumbers: true,
});

// Function to run code
function runCode() {
  const htmlCode = htmlEditor.getValue();
  const cssCode = cssEditor.getValue();
  const jsCode = jsEditor.getValue();

  const completeHTML = `
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>${cssCode}</style>
      </head>
      <body>
        ${htmlCode}
        <script>${jsCode}<\/script>
      </body>
    </html>
  `;

  const blob = new Blob([completeHTML], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  document.getElementById("output-frame").src = url;
}

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
