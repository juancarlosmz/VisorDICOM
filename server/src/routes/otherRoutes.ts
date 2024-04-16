import { Router } from "express";
import path from 'path';

class OtherRoutes{
    router: Router = Router();

    constructor(){
        this.config();
    }

    config(): void{
        console.log('Test 1 -- ');
        //this.router.get('/', (req, res) => res.send('Other'));
        console.log('Test 2 -- ');
        //console.log(this.router.get('/', (req, res) => res.send(this.router.post('/'))));
        console.log('Test 3 -- ');
        //this.router.get('/', (req, ress) => res.send(new Buffer('wahoo')));
        //this.router.get('/', (req, res) => res.send({ some: 'json' }));
        //this.router.get('/', (req, res) => res.send('<p>some html</p>'));
        //this.router.get('/', (req, res) => res.status(404).send('Sorry, cant find that'));

        this.router.get('/', function(req, res) {
            res.sendFile( path.resolve('../../../APLICACIONES/VisorDICOM/client/index.html?+51931180310') );
        });

    }
}

const otherRoutes = new OtherRoutes();
export default otherRoutes.router;