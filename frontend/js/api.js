
const API="http://127.0.0.1:8000/api/v1";
async function getStats(){return fetch(API+"/stats").then(r=>r.json())}
async function getHistory(){return fetch(API+"/history").then(r=>r.json())}
async function predictImage(fd){return fetch(API+"/predict",{method:"POST",body:fd}).then(r=>r.json())}
