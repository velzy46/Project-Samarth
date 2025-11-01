const form = document.getElementById("chatForm");
const input = document.getElementById("msg");
const chat = document.getElementById("chat");

function appendMessage(text, who = "bot") {
  const div = document.createElement("div");
  div.className = "message " + (who === "user" ? "user" : "bot");
  div.innerText = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const q = input.value.trim();
  if (!q) return;
  appendMessage(q, "user");
  input.value = "";
  appendMessage("Thinking...", "bot");

  try {
    const res = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q }),
    });

    const data = await res.json();

    const last = chat.querySelectorAll(".message.bot");
    if (last.length) last[last.length - 1].remove();

    if (data && data.answer) {
      appendMessage(data.answer, "bot");
    } else {
      appendMessage("Sorry, something went wrong.", "bot");
    }
  } catch (err) {
    console.error("Error:", err);
    const last = chat.querySelectorAll(".message.bot");
    if (last.length) last[last.length - 1].remove();
    appendMessage("Error contacting server. Make sure Flask is running.", "bot");
  }
});
