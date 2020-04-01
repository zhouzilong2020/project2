document.addEventListener('DOMContentLoaded', ()=>{
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', function() {
      document.querySelector('#new-message').onsubmit = () =>{
        const new_message = document.querySelector('#message').value;
        socket.emit('new message', {new_message: new_message});
        return false;
      };
  });

  socket.on('announce message', function(){
      const li = document.createElement('li');
      const new_message = data[new_message];
      li.innerHTML = new_message;
      document.querySelector('#messages').append(li);
  });

});
