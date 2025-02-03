const client_sock = new WebSocket("ws://localhost:4444")
client_sock.onopen = () => console.log("Connected to server!")

// Send Messages
function sendMessage(e) {
    e.preventDefault()
    const msg = document.querySelector('#message')
    if (msg.value) {
        client_sock.send(msg.value)
        msg.value = ""
    }
    msg.focus()
}

document.querySelector('#message-form')
    .addEventListener('submit', sendMessage)


// Listen for message
client_sock.addEventListener('message', ({data}) => {
    const li = document.createElement('li')
    li.textContent = data
    document.querySelector('#message-list').appendChild(li)
})