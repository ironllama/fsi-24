const express = require('express');

const app = express();
const port = 3002;

const allowCrossDomain = (req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    res.header('Access-Control-Allow-Headers', 'DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization')
    next()
}
app.use(allowCrossDomain);

app.use(express.json())

function loadDataFile(fileName, lineHandler) {
    return require('fs')
        .readFileSync(fileName, { encoding: 'utf-8' })
        .split("\n")
        .map(lineHandler)
        .filter(line => line !== null);
}

const allChats = loadDataFile('chats2.txt', line => {
    if (line) {
        const [date, name, text] = line.split("|");
        return ({ date, name, text });
    }
    else return (null);
})
console.log(`Loaded ${allChats.length} chats.`);

const allUsers = loadDataFile('chat-users2.txt', line => {
    if (line) {
        const [name, password, token] = line.split("|");
        return ({ name, password, token });
    }
    else return (null);
})
console.log(`Loaded ${allUsers.length} users.`);

function getDate() {
    // return new Date().toISOString().substring(11, 19);
    return new Date().toTimeString().substring(0, 8);
}

function getIPAddr(req) {
    return req.socket.remoteAddress.substring(7);
}

app.post('/createUser', (req, res) => {
    console.log(`${getDate()}: ${getIPAddr(req)} - createUser:`, req.body);
    try {
        const { name, password } = req.body;
        if (!name || !password) {
            res.status(400).send({ code: "400", message: 'Required fields missing.' });
            return;
        }

        password

        allUsers.push({ name, password, token });

        const newLine = `${name}|${password}|${token}\n`;
        require('fs')
            .appendFileSync('chats2.txt', newLine, { flag: 'a', encoding: 'utf-8' });



    }
    catch {
        res.status(500).send({ code: "500", message: 'Something went terribly wrong. ' })
    }
});

app.post('/login', (req, res) => {
    console.log(`${getDate()}: ${getIPAddr(req)} - sendChat:`, req.body);
    try {
    }
    catch {
        res.status(500).send({ code: "500", message: 'Something went terribly wrong. ' })
    }
});

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
            .appendFileSync('chats2.txt', newLine, { flag: 'a', encoding: 'utf-8' });
    }
    catch {
        res.status(500).send({ code: "500", message: 'Something went terribly wrong. ' })
    }
});

app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
});
