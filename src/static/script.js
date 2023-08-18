const chatDisplay = document.getElementById('chat-display');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value;
    addMessage('You', userMessage);
    userInput.value = '';

    // Use AJAX or Fetch to send user message to the server
    // Receive response from the server and add it to the chat display
});

function addMessage(sender, content) {
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${content}`;
    chatDisplay.appendChild(messageElement);
}
