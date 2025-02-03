const ws = require("ws")
const server = new ws.Server({port : 4444})

server.on("connection", (socket) => {
    console.log("New Connection!")
    socket.on("message", message => {
        const b = Buffer.from(message)
        console.log(b.toString())
        socket.send(`${message}`)
    })
});