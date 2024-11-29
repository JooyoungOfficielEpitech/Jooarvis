document.addEventListener("DOMContentLoaded", () => {
    const apiBase = "http://127.0.0.1:8000/api";

    async function fetchTasks() {
        const response = await fetch(`${apiBase}/tasks`);
        const tasks = await response.json();
        console.log(tasks);
    }

    fetchTasks();
});
