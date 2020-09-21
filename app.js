const spawn = require("child_process").spawn;

var schedule = require('node-schedule');
var express = require('express');
var app = express();
var fs = require('fs')

app.use(express.static(__dirname));


/*
app.get('/', function (req, res) {
	res.send('Hello World!');
});
*/
/* GET home page. */
app.get('/', function(req, res, next) {
	var pythonProcess = spawn('python3', ["./bstest.py"]);

	fs.readFile('menu_text.txt', 'utf8', function(err, data) {
		if (err){
			throw err;
			res.send('error');
		}
		console.log(data)
		res.send(data);
	});
});

app.post('/', function(req, res, next) {
	var pythonProcess = spawn('python3', ["./bstest.py"]);

	fs.readFile('menu_text.txt', 'utf8', function(err, data) {
		if (err){
			throw err;
			res.send('error');
		}
		console.log(data)
		res.send(data);
	});
});

app.get('/update', function(req, res, next) {
	var updateProcess = spawn('python3', ["./update.py"]);
	updateProcess.stdout.on('data', (data) => {
		console.log(data);
		res.send('Update completed');
	});
});

app.post('/update', function(req, res, next) {
	var updateProcess = spawn('python3', ["./update.py"]);
	updateProcess.stdout.on('data', (data) => {
		console.log(data);
		res.send('Update completed');
	});
});


app.listen(58885, function () {
	console.log('Bob-bot app listening on port 58885!');
});


var j = schedule.scheduleJob('0 0 7 * * *', function(){
	console.log('The answer to life, the universe, and everything!');
	var updateProcess = spawn('python3', ["./update.py"]);
	updateProcess.stdout.on('data', (data) => {
		console.log(data);
	});

});

