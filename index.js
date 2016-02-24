var http = require('http'),
    jade = require('jade');

http.createServer(function (req, res) {
    if (req.method == 'GET') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        var f = jade.compileFile('index.jade', {
            'pretty': true
        });
        res.end(f());
    } else if (req.method == 'POST') {
        var body = '';
        req.on('data', function (data) {
            body += data;
        });
        req.on('end', function () {
            // Do something:
            console.log(body);
            res.end();
        });
    }
}).listen(3000);
