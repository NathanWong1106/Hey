const express = require('express');
const app = express(); // app setup
const http = require('http');
const server = http.createServer(app);
const socket = require('socket.io')
const net = require('net');
const fs = require('fs');

var cam_state = new Map();
var emp_list = []

/* static files
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});*/

server.listen(3000, function(){
  console.log('listening on *:3000');
});

var io = socket(server, {
    cors: {
        origin: "*"
    }
}); // socket setup

io.on('connection', (socket) => {
    console.log('User connected');
    socket.on('cam_update', (data) => {
            id = data.id;
            state = data.state;
            cam_state.set(id, state == 1 ? true : false);
            console.log(cam_state);
    })
    console.log(cam_state);
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});
setInterval(() => {
    io.emit('ping', {state: JSON.stringify(Array.from(cam_state))})
    }, 1000); // broadcast map at 5 sec interval