import { Router } from "express";
import { EmployeModel } from "../models/employe";
import path from 'path';
class VisorDicomRoutes{
    router: Router = Router();
    constructor(){
        this.config();
    }

    config(): void{
        console.log('jj -- ');
       /* this.router.get('/', (req, res) => {
            const employeModel: EmployeModel = {
                id: 1,
                firstName: "Juan Carlos",
                lastName: "Mendoza ",
                age: 29,
                position: "TI",
                salary: 2000,
            }
            console.log("este es mi test");
            res.send(employeModel); 
        });*/
        this.router.get('/', function(req, res) {
            res.sendFile( path.resolve('../../../APLICACIONES/VisorDICOM/client/index.html') );
            /*const employeModel: EmployeModel = {
                id: 1,
                firstName: "Juan Carlos",
                lastName: "Mendoza ",
                age: 29,
                position: "TI",
                salary: 2000,
            }
            console.log("este es mi test");
            res.send(employeModel); */
        });
        console.log('madre te amo');
    }
}

const visorDicomRoutes = new VisorDicomRoutes();
export default visorDicomRoutes.router;