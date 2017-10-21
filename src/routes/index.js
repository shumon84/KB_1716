var express = require('express');
var router = express.Router();
var uuid = require('node-uuid');
var fs = require('fs');
var execSync = require('child_process').execSync;
var mysql = require('mysql');
var connection = mysql.createConnection({
  host  : '',
  user  : 'yorechi',
  password  : 'hogehoge123';
});


var multer = require('multer');
var multerStorage = multer.diskStorage({
  destination: function (req, file ,cb) {
    cb(null, './uploads');
  },
  filename: function (req, file, cb) {
    cb(null, uuid.v4());
  }
});
var upload = multer({ storage: multerStorage });

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/', upload.single('picture'), function(req, res) {
  console.log(req.file);
  var COMMAND = `python ./scripts/hoge.py ./uploads/${req.file.filename}`;

  var result = execSync(COMMAND).toString();

  if(result[0] === 'ERROR'){
    console.log(result);
    res.render('error', {error: result[1]}); //人数によって変動
  }else{
    console.log(result);
    connection.connect(function(err) {
      if(err){
        console.error('error connecting: ' + err.stack);
        return;
      }
      console.log('connected as id ' + connection.threadId);
    });
    connection.query('SELECT * FROM `cocktailTB` WHERE `color` = result[0]', function(err,res,fields){
      var left = res[0].name;
    });
    connection.query('SELECT * FROM `cocktailTB` WHERE `color` = result[1]', function(err,res,fields){
      var right = res[0].name;
    });
    res.render('result', {
      title: 'result',
      left: left,
      right: right
    });
    fs.unlink(req.file, function (err){
      console.log(err);
    });
  }
});

module.exports = router;
