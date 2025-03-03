document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chat-form");
    const queryInput = document.getElementById("query");
    const chatBox = document.getElementById("chat-box");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const question = queryInput.value.trim();
        if (!question) return;

        // Append user message
        appendMessage("user", question);

        try {
            const response = await fetch("/ask", {
                method: "POST",
                body: new URLSearchParams({ "query": question }),
                headers: { "Content-Type": "application/x-www-form-urlencoded" }
            });

            const data = await response.json();
            if (response.ok) {
                appendMessage("bot", data.answer);
            } else {
                appendMessage("error", `Error: ${data.error}`);
            }
        } catch (error) {
            appendMessage("error", "Failed to fetch response from server.");
        }

        queryInput.value = "";
    });

    function appendMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.innerHTML = `<p>${message}</p>`;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to latest message
    }
});
