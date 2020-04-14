document.addEventListener('DOMContentLoaded', ()=>{
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  socket.on('connect', function() {
      document.querySelector('#newChannel').onsubmit = () =>{
        socket.emit('new channel', {'user_id': user_id, 'displayname':displayname} );
        return false;
      };
  });

  // 
  socket.on('new channel', channelLog=>{

  })


});
