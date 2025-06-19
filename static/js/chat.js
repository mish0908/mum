const socket = io();
const messages = document.getElementById('messages');
const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('message');
const usernameInput = document.getElementById('username');

chatForm.onsubmit = (e) => {
    e.preventDefault();
    if (messageInput.value && usernameInput.value) {
        socket.emit('message', {
            user: usernameInput.value,
            message: messageInput.value
        });
        messageInput.value = '';
    }
};

socket.on('message', (data) => {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message-bubble';
    if (data.user === usernameInput.value) {
        messageDiv.className += ' own';
    }
    messageDiv.innerHTML = `
        <strong>${data.user}</strong>
        <p>${data.message}</p>
        <small>${data.timestamp}</small>
    `;
    messages.appendChild(messageDiv);
    messages.scrollTop = messages.scrollHeight;
}); 