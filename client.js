const socket = new WebSocket('ws://localhost:8080/ws');

socket.onopen = () => {
    console.log('WebSocket conectado');
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    const message = document.createElement('div');
    message.textContent = data.message;
    document.querySelector('#messages').appendChild(message);

};

socket.onclose = () => {
    console.log('WebSocket desconectado');
};

document.querySelector('#send-btn').addEventListener('click', () => {
    const message = document.querySelector('#message-input').value;
    socket.send(JSON.stringify({ message }));
});
