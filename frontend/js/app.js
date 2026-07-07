const API="http://127.0.0.1:8000/api/v1";

let diseaseChart=null,cropChart=null,marketChart=null,currentMarketPrice=0;

const imageInput=document.getElementById("imageInput");
const preview=document.getElementById("preview");
const predictBtn=document.getElementById("predictBtn");
const estimateBtn=document.getElementById("estimateBtn");

function animate(el,end,suffix=""){
 let v=0,step=Math.max(1,Math.ceil(end/40));
 const t=setInterval(()=>{v+=step;if(v>=end){v=end;clearInterval(t);}el.textContent=v+suffix;},20);
}

imageInput?.addEventListener("change",e=>{
 const f=e.target.files[0];
 if(f) preview.src=URL.createObjectURL(f);
});

async function loadDashboard(){
 try{
   const s=await fetch(API+"/stats").then(r=>r.json());
   if(s.stats){
      animate(total,Number(s.stats.total_predictions));
      animate(healthy,Number(s.stats.healthy_predictions));
      animate(diseased,Number(s.stats.diseased_predictions));
      confidence.textContent=s.stats.average_confidence+"%";
   }
   const h=await fetch(API+"/history").then(r=>r.json());
   const hist=h.history||[];
   const tb=document.querySelector("#historyTable tbody");
   tb.innerHTML="";
   const dm={},cm={};
   hist.forEach(x=>{
      tb.innerHTML+=`<tr><td>${x.crop}</td><td>${x.disease}</td><td>${x.confidence}%</td></tr>`;
      dm[x.disease]=(dm[x.disease]||0)+1;
      cm[x.crop]=(cm[x.crop]||0)+1;
   });
   if(diseaseChart)diseaseChart.destroy();
   diseaseChart=new Chart(diseaseChart=document.getElementById("diseaseChart"),{
      type:"doughnut",
      data:{labels:Object.keys(dm),datasets:[{data:Object.values(dm)}]}
   });
   if(cropChart)cropChart.destroy();
   cropChart=new Chart(document.getElementById("cropChart"),{
      type:"bar",
      data:{labels:Object.keys(cm),datasets:[{label:"Predictions",data:Object.values(cm)}]}
   });
 }catch(e){console.error(e);}
}

async function loadMarket(crop){
 try{
   const p=await fetch(API+"/market/predict?crop="+encodeURIComponent(crop)).then(r=>r.json());
   const rec=await fetch(API+"/market/recommendation?crop="+encodeURIComponent(crop)).then(r=>r.json());
   const hist=await fetch(API+"/market/history?crop="+encodeURIComponent(crop)).then(r=>r.json());

   currentMarketPrice=Number(p.today)||0;

   currentPrice.textContent="₹"+p.today;
   predictedPrice.textContent="₹"+p.predicted;
   weeklyAverage.textContent="₹"+p.weekly_average;
   marketTrend.textContent=p.trend==="Rising"?"🟢 Rising":"🔴 Falling";
   recommendation.textContent=rec.recommendation;

   const pct=((p.predicted-p.today)/p.today*100).toFixed(2);
   const pc=document.getElementById("priceChange");
   if(pc){
      pc.textContent=(pct>=0?"▲ ":"▼ ")+Math.abs(pct)+"%";
      pc.style.color=pct>=0?"green":"red";
   }

   // Placeholder top markets
   ["m1","m2","m3","m4","m5"].forEach((id,i)=>{
      const el=document.getElementById(id);
      if(el) el.textContent="₹"+Math.round(currentMarketPrice-(i*20));
   });

   // Simple 7-day forecast
   for(let i=1;i<=7;i++){
      const d=document.getElementById("day"+i);
      if(d){
         const val=Math.round(currentMarketPrice*(1+(i*0.003)));
         d.textContent="₹"+val;
      }
   }

   const labels=hist.map(x=>x.Date);
   const prices=hist.map(x=>x.Price);
   if(marketChart)marketChart.destroy();
   marketChart=new Chart(document.getElementById("marketChart"),{
      type:"line",
      data:{labels,datasets:[{label:crop+" Price",data:prices,fill:true,tension:.35}]}
   });

 }catch(e){console.error(e);}
}

estimateBtn?.addEventListener("click",()=>{
 const qty=Number(document.getElementById("quantityInput").value||0);
 const rev=qty*currentMarketPrice;
 document.getElementById("estimatedRevenue").textContent="₹"+rev.toLocaleString();
});

predictBtn?.addEventListener("click",async()=>{
 const f=imageInput.files[0];
 if(!f){alert("Select an image");return;}
 const fd=new FormData(); fd.append("file",f);
 try{
   const data=await fetch(API+"/predict",{method:"POST",body:fd}).then(r=>r.json());
   const p=data.prediction||{};
   predictionCard.innerHTML=`<h2>${p.disease||"-"}</h2>
   <p><b>Crop:</b> ${p.crop||"-"}</p>
   <p><b>Confidence:</b> ${p.confidence||0}%</p>
   <p><b>Cause:</b> ${p.cause||"N/A"}</p>
   <p><b>Symptoms:</b> ${p.symptoms||"N/A"}</p>
   <p><b>Treatment:</b> ${p.treatment||"N/A"}</p>`;
   if(p.crop) await loadMarket(p.crop);
   await loadDashboard();
 }catch(e){console.error(e);alert("Prediction failed");}
});

loadDashboard();
