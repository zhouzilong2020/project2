document.addEventListener('DOMContentLoaded', () => {

    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    const template = Handlebars.compile("<li>{{message}}</li>");

    // When connected, configure buttons
    socket.on('connect', () => {

        // Each button should emit a "submit vote" event
        document.querySelector('button').onclick =() => {
                const message = document.querySelector('message')
                socket.emit('message', {'message': message});
            };
        });

    // When a new vote is announced, add to the unordered list
    socket.on('message', data => {
      const content = template({'message': message});
      document.querySelector('#send_mesasge').innerHTML += content;
      });
});
