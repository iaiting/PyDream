(function() {
    var $msg = $('#msg');
    var $text = $('#text');

    var WebSocket = window.WebSocket || window.MozWebSocket;
    if (WebSocket) {
        try {
            var socket = new WebSocket('ws://127.0.0.1:8000/new-msg/socket');
        } catch (e) {}
    }

    if (socket) {
        socket.onmessage = function(event) {

            $msg.append('<p>' + event.data + '</p>');
            console.log("****************:"+event.data+" msg " +$msg)
        }

        $('form').submit(function() {
            socket.send($text.val());
            $text.val('').select();
            return false;
        });
    } else {
        var error_sleep_time = 500;
        function poll() {
            $.ajax({
                url: '/new-msg/',
                type: 'GET',
                success: function(event) {
                    $msg.append('<p>' + event + '</p>');
                    error_sleep_time = 500;
                    poll();
                },
                error: function() {
                    error_sleep_time *= 2;
                    setTimeout(poll, error_sleep_time);
                }
            });
        }
        poll();

        $('form').submit(function() {
            $.ajax({
                url: '/new-msg/',
                type: 'POST',
                data: {text: $text.val()},
                success: function() {
                    $text.val('').select();
                }
            });
            return false;
        });
    }
})();