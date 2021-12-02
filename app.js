const http = require('http');
const fs = require('fs');


const server = http.createServer((req, res) => {
    console.log('Request Made');
    res.setHeader('Content-Type', 'text/html');
    console.log(req.url)
    
    fs.readFile('./templates/index.html', (err, data)=>{
        if (err){
            console.log(err);
            res.end();
        } else{
            res.write(data);
            res.end();
        }
    });

});

server.listen(3000, '192.168.29.217', () => {
    console.log('Listening...');
});