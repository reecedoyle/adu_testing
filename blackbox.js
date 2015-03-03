var WINDOW_SIZE = 300000;
var CURRENT_TIME = Math.floor((new Date).getTime()/1000);
var WINDOW_CUTOFF = CURRENT_TIME-(WINDOW_SIZE*60);
var LAST_READING_TIME = CURRENT_TIME-65;
 
var BANDWIDTH_0 = 0.302494;
var BANDWIDTH_1 = 0.597704;
var BANDWIDTH_2 = 0.467658;
var BANDWIDTH_3 = 0.768034;
 
var runtimeStart = (new Date).getTime()/1000.0;
 
 
var conn = new Mongo();
var db = conn.getDB("tempdata");
var cursor = db.temps.find({"time":{ "$gt": WINDOW_CUTOFF.toString()}});
var lastReading = db.temps.find({"time": {"$gt": LAST_READING_TIME.toString()}}).next();
var lastReadingTime = lastReading["time"];
var y0 = lastReading["0"];
var y1 = lastReading["1"];
var y2 = lastReading["2"];
var y3 = lastReading["3"];
 
var ANOMALY_SCORE = 0.0;
 
while(cursor.hasNext()){
        var currentReading = cursor.next();
        var x0 = currentReading["0"];
        var x1 = currentReading["1"];
        var x2 = currentReading["2"];
        var x3 = currentReading["3"];
        var calc0 = -(Math.pow((y0-x0), 2.0)/(2.0*Math.pow(BANDWIDTH_0, 2.0)));
        var calc1 = -(Math.pow((y1-x1), 2.0)/(2.0*Math.pow(BANDWIDTH_1, 2.0)));
        var calc2 = -(Math.pow((y2-x2), 2.0)/(2.0*Math.pow(BANDWIDTH_2, 2.0)));
        var calc3 = -(Math.pow((y3-x3), 2.0)/(2.0*Math.pow(BANDWIDTH_3, 2.0)));
        ANOMALY_SCORE += Math.pow(Math.E, (calc0+calc1+calc2+calc3));
       
}
 
var runtimeEnd = (new Date).getTime()/1000.0;
var totalRuntime = runtimeEnd-runtimeStart;
 
ANOMALY_SCORE = 1/ANOMALY_SCORE;
if(ANOMALY_SCORE>1){
        ANOMALY_SCORE = 1;
}
//green, amber, red thresholds
var cursor = db.thresholds.find({"network":"ucl-cs-machineroom"});
var amberThreshold = 1;
var redThreshold = 1;
while(cursor.hasNext()){
        var thresholds = cursor.next();
        if(thresholds){
                amberThreshold = thresholds.amber;
                redThreshold = thresholds.red;
        }
}
 
var classification = "green";
if(ANOMALY_SCORE>redThreshold){
        classification = "red";
}
else if(ANOMALY_SCORE>amberThreshold){
        classification = "amber";
}
 
 
db.temps.update({"time":lastReadingTime}, {"$set":{"anomalyScore":ANOMALY_SCORE, "classification": classification}});
 
print("---------------------------");
print("CURRENT ANOMALY SCORE: "+ANOMALY_SCORE.toString());
print("CURRENT WINDOW SIZE: "+WINDOW_SIZE.toString());
print("RUNTIME: "+totalRuntime.toString()+"s");
print("CURRENT CLASSIFICATION: "+classification);
print("---------------------------");