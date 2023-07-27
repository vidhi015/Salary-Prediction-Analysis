var http = require('http');
//create a serYer object:
http.createServer(function (req, res) {
res.write('Hello World!'); //write a response to the client
res.end(); //end the response
}).listen(8078); //the serYer object listens on port 8080