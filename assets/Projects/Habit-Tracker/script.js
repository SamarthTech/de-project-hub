let habits = JSON.parse(localStorage.getItem('habits')) || [];

function saveHabits() {
    localStorage.setItem('habits', JSON.stringify(habits));
}

function addHabit(name, goal) {
    habits.push({
        name,
        goal,
        progress: 0,
        lastUpdated: new Date().toDateString(),
        history: []
    });
    saveHabits();
    renderHabits();
    renderChart();
}

function updateHabit(index, progress) {
    const habit = habits[index];
    const today = new Date().toDateString();
    
    if (habit.lastUpdated !== today) {
        habit.progress = 0;
        habit.history.push(habit.progress);
        if (habit.history.length > 7) habit.history.shift();
    }
    
    habit.progress = Math.min(habit.goal, habit.progress + progress);
    habit.lastUpdated = today;
    
    saveHabits();
    renderHabits();
    renderChart();
}

function renderHabits() {
    const habitsList = document.getElementById('habits-list');
    habitsList.innerHTML = '';
    
    habits.forEach((habit, index) => {
        const habitItem = document.createElement('div');
        habitItem.className = 'habit-item';
        
        const progress = Math.round((habit.progress / habit.goal) * 100);
        
        habitItem.innerHTML = `
            <h3>${habit.name}</h3>
            <p>Goal: ${habit.goal} | Progress: ${habit.progress}</p>
            <div class="progress-bar">
                <div class="progress" style="width: ${progress}%">${progress}%</div>
            </div>
            <button onclick="updateHabit(${index}, 1)">+</button>
            <button onclick="updateHabit(${index}, -1)">-</button>
        `;
        
        habitsList.appendChild(habitItem);
    });
}

function renderChart() {
    const chart = document.getElementById('progress-chart');
    chart.innerHTML = '<h2>Weekly Progress</h2>';
    
    const chartBar = document.createElement('div');
    chartBar.className = 'chart-bar';
    
    habits.forEach(habit => {
        const bar = document.createElement('div');
        bar.className = 'bar';
        const height = (habit.progress / habit.goal) * 100;
        bar.style.height = `${height}%`;
        bar.title = `${habit.name}: ${habit.progress}/${habit.goal}`;
        chartBar.appendChild(bar);
    });
    
    chart.appendChild(chartBar);
}

document.getElementById('habit-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const name = document.getElementById('habit-name').value;
    const goal = parseInt(document.getElementById('habit-goal').value);
    addHabit(name, goal);
    this.reset();
});

// Check for reminders
setInterval(() => {
    const now = new Date();
    if (now.getHours() === 20 && now.getMinutes() === 0) {  // 8:00 PM
        habits.forEach(habit => {
            if (habit.lastUpdated !== now.toDateString()) {
                alert(`Don't forget to update your progress for ${habit.name}!`);
            }
        });
    }
}, 60000);  // Check every minute

// Initial render
renderHabits();
renderChart();