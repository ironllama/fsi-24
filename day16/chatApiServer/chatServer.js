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

app.use(express.json())

const allChats =
    require('fs')
        .readFileSync('chats.txt', { encoding: 'utf-8' })
        .split("\n")
        .map(line => {
            if (line) {
                const [date, name, text] = line.split("|");
                return ({ date, name, text });
            }
            else return (null);
        })
        .filter(line => line !== null);
console.log(`Loaded ${allChats.length} chats.`);

function getDate() {
    // return new Date().toISOString().substring(11, 19);
    return new Date().toTimeString().substring(0, 8);
}

function getIPAddr(req) {
    return req.socket.remoteAddress.substring(7) || req.headers['x-forwarded-for'];
}

app.get('/getChats', (req, res) => {
    console.log(`${getDate()}: ${getIPAddr(req)} - getChats`);
    // res.send(allJokes[Math.floor(Math.random() * allJokes.length)]);
    res.send(allChats);
});

app.post('/sendChat', (req, res) => {
    console.log(`${getDate()}: ${getIPAddr(req)} - sendChat:`, req.body);
    try {

        const { name, text } = req.body;
        if (!name || !text) {
            res.status(400).send({ code: "400", message: 'Required fields missing.' });
            return;
        }
        const date = new Date().toISOString();

        allChats.push({ date, name, text });

        const newLine = `${date}|${name}|${text}\n`;
        require('fs')
            .appendFileSync('chats.txt', newLine, { flag: 'a', encoding: 'utf-8' });

        res.send({ message: "OK. Operation successful." });
    }
    catch {
        res.status(500).send({ code: "500", message: 'Something went terribly wrong. ' })
    }
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
