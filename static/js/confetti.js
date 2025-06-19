function createConfetti() {
    const colors = ['#ff8fa3', '#ffc2d1', '#ffb1c3', '#ff7a93', '#ffd1dc', '#ffb6c1'];
    const confettiContainer = document.querySelector('.confetti-container');
    
    for (let i = 0; i < 50; i++) {
        const confetti = document.createElement('div');
        const color = colors[Math.floor(Math.random() * colors.length)];
        
        confetti.style.cssText = `
            position: absolute;
            width: ${Math.random() * 8 + 5}px;
            height: ${Math.random() * 8 + 5}px;
            background-color: ${color};
            left: ${Math.random() * 100}vw;
            top: -10px;
            opacity: ${Math.random() * 0.5 + 0.5};
            transform: rotate(${Math.random() * 360}deg);
            animation: confettiFall ${Math.random() * 2 + 3}s linear infinite;
            border-radius: 50%;
        `;
        
        confettiContainer.appendChild(confetti);
    }
}

// Start confetti when page loads
window.addEventListener('load', createConfetti);

// Clean up confetti periodically to prevent too many elements
setInterval(() => {
    const confettiContainer = document.querySelector('.confetti-container');
    while (confettiContainer.firstChild) {
        confettiContainer.removeChild(confettiContainer.firstChild);
    }
    createConfetti();
}, 10000); 