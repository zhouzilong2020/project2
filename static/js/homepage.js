document.addEventListener('DOMContentLoaded', ()=>{
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
  const owner = document.querySelector('#owner').innerHTML;

  socket.on('connect', () => {
      document.querySelector('#newChannel').onclick = () =>{
          socket.emit('new channel', {'owner' : owner});
      }
  });


  socket.on('announce new channel', data=>{
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.innerHTML = data['new_channel_id'];
      a.href = "/chatroom/" + owner +  "/" + data['new_channel_id'];
      li.appendChild(a);
      document.querySelector('#channels').appendChild(li);
      return false;
  })


});
