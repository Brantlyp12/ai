<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        #chatbox { width: 100%; max-width: 500px; height: 400px; border: 1px solid #ccc; overflow-y: auto; padding: 10px; margin: auto; }
        #userInput { width: 80%; padding: 10px; }
        button { padding: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>AI Chatbot</h1>
    <div id="chatbox"></div>
    <input type="text" id="userInput" placeholder="Type a message..." />
    <button onclick="sendMessage()">Send</button>

    <script>
        function sendMessage() {
            let userText = document.getElementById("userInput").value;
            if (userText.trim() === "") return;

            let chatbox = document.getElementById("chatbox");
            chatbox.innerHTML += `<p><strong>You:</strong> ${userText}</p>`;

            fetch("https://yourchatbotapi.com/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userText })
            })
            .then(response => response.json())
            .then(data => {
                chatbox.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
            })
            .catch(error => console.error("Error:", error));

            document.getElementById("userInput").value = "";
        }
    </script>
</body>
</html>
