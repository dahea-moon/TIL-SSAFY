const http = require('http');
const port = 3001;

http.createServer((req, res) => {
    res.writeHead(404, {
        'Content-Type': 'text.plain',
    });
    res.statusCode = 200;
    res.write('LunchTime');
    res.end('End of responses\n');
}).listen(port);


console.log(`Server is running @ http://localhost:${port}`);
