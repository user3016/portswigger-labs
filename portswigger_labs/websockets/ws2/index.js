const ws = require('ws')
const server = new ws.WebSocketServer({port : 8080})

server.on('connection', function conn(sock){
    console.log("Recieved a connection")
})