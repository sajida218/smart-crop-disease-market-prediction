
const API="http://127.0.0.1:8000/api/v1/analytics";
fetch(API).then(r=>r.json()).then(d=>{
pie("diseaseChart",d.disease_distribution,"Disease Distribution");
bar("cropChart",d.crop_distribution,"Crop Distribution");
bar("dailyChart",d.daily_predictions,"Daily Predictions");
line("confidenceChart",d.confidence_trend,"Confidence Trend");
});

function pie(id,obj,title){
new Chart(document.getElementById(id),{
type:"pie",
data:{labels:Object.keys(obj),datasets:[{data:Object.values(obj)}]},
options:{plugins:{title:{display:true,text:title}}}
});
}
function bar(id,obj,title){
new Chart(document.getElementById(id),{
type:"bar",
data:{labels:Object.keys(obj),datasets:[{label:title,data:Object.values(obj)}]},
options:{responsive:true}
});
}
function line(id,arr,title){
new Chart(document.getElementById(id),{
type:"line",
data:{labels:arr.map((_,i)=>i+1),datasets:[{label:title,data:arr}]}
});
}
