import csv, os

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
CSV=os.path.join(BASE_DIR,"data","market_prices.csv")

def _rows():
    with open(CSV,encoding="utf-8") as f:
        r=list(csv.DictReader(f))
    for x in r: x["Price"]=float(x["Price"])
    return r

def _crop(c):
    return [r for r in _rows() if r["Crop"].lower()==c.lower()]

def predict(crop):
    h=_crop(crop)
    p=[x["Price"] for x in h]
    today=p[-1]
    avg=sum(p)/len(p)
    pred=round((today+avg)/2,2)
    return {"today":today,"predicted":pred,"weekly_average":round(avg,2),
            "trend":"Rising" if pred>=today else "Falling"}

def history(crop): return _crop(crop)

def recommendation(crop):
    pr=predict(crop)
    return {"recommendation":"Hold" if pr["trend"]=="Rising" else "Sell Today"}

def top(crop):
    pr=predict(crop)["today"]
    names=["Guntur","Vijayawada","Kurnool","Warangal","Hyderabad"]
    return [{"market":n,"price":round(pr-i*20,2)} for i,n in enumerate(names)]

def forecast(crop):
    today=predict(crop)["today"]
    vals=[]
    for d in range(1,8):
        vals.append({"day":d,"price":round(today*(1+d*0.003),2)})
    return vals

def profit(crop,qty):
    price=predict(crop)["today"]
    return {"quantity":qty,"price":price,"revenue":round(qty*price,2)}
