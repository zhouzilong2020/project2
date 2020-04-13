document.addEventListener('DOMContentLoaded', ()=>{
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
  const room_id = document.querySelector('#room_id').innerHTML;
  const user_id = document.querySelector('#user_id').innerHTML;

  socket.on('connect', function() {
      document.querySelector('#new-message').onsubmit = () =>{
        const new_message = document.querySelector('#message').value;
        document.querySelector('#message').value = '';
        socket.emit('new message', {'new_message': new_message, 'room_id':room_id, 'user_id':user_id});
        return false;
      };
  });

  socket.on('announce message', data =>{
      if (data['room_id'] === room_id){
          const li = document.createElement('li');
          const new_message = data['user_id'] + '  said:' + data['new_message'];
          li.innerHTML = new_message;
          document.querySelector('#messages').append(li);
    }
  });

});
