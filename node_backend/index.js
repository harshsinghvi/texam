express = require('express');
bodyParser = require("body-parser");
cors = require('cors')

const DB_URI = process.env.MONGO_DB_URI

const app = express();
app.use(bodyParser.json());
app.use(cors());
const PORT = process.env.PORT || 3000;

app.get('/hello-world', (request, response) => {
    response.send("Hello World ");
    // console.log(request.log);
});

app.listen(PORT,'0.0.0.0', function() {
    console.log('App listening on port '+ PORT+' !');
});