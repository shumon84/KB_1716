var express = require('express');
var router = express.Router();
var uuid = require('node-uuid');
var fs = require('fs');
var execSync = require('child_process').execSync;

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
  res.send(result);

  fs.unlink(req.file, function (err){
    console.log(err);
  });
});

module.exports = router;
