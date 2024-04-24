const express = require('express');

const app = express();
const port = 3000;

const allowCrossDomain = (req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    res.header('Access-Control-Allow-Headers', 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization')
    next()
}
app.use(allowCrossDomain);

const allJokes = JSON.parse(
    require('fs')
        .readFileSync('jokes.json', { encoding: 'utf-8' })
);
console.log(`Loaded ${allJokes.length} jokes.`);

app.get('/random_joke', (req, res) => {
    console.log("NEW REQUEST: req", req.socket.remoteAddress)
    res.send(allJokes[Math.floor(Math.random() * allJokes.length)]);
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});