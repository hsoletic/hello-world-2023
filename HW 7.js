// https://kylemcdonald.github.io/cv-examples/
// https://github.com/kylemcdonald/AppropriatingNewTechnologies/wiki/Week-2
var capture;
var tracker
var w = 640,
    h = 480;
function setup() {
    capture = createCapture({
        audio: false,
        video: {
            width: w,
            height: h
        }
    }, function() {
        console.log('capture ready.')
    });
    capture.elt.setAttribute('playsinline', '');
    createCanvas(w, h);
    capture.size(w, h);
    capture.hide();
    colorMode(HSB);
    tracker = new clm.tracker();
    tracker.init();
    tracker.start(capture.elt);
}
function draw() {
    image(capture, 0, 0, w, h);
    var positions = tracker.getCurrentPosition();
    noFill();
    stroke(255);
    beginShape();
    for (var i = 0; i < positions.length; i++) {
        vertex(positions[i][0], positions[i][1]);
    }
    endShape();
    noStroke();
    for (var i = 0; i < positions.length; i++) {
        fill(map(i, 0, positions.length, 0, 360), 50, 100);
        //ellipse(positions[i][0], positions[i][1], 4, 4);
        //text(i, positions[i][0], positions[i][1]);
    }
    if (positions.length > 0) {
        var mouthLeft = createVector(positions[44][0], positions[44][1]);
       var eyebrowleft = createVector(positions[19][0], positions[22][0])
       var eyebrowright = createVector(positions[22][0], positions[22][1])
        var mouthRight = createVector(positions[18][0], positions[18][1]);
        var smile = mouthLeft.dist(mouthRight);
        var frown = eyebrowleft.dist(eyebrowright);
      console.log(smile); 
      console.log(frown);
      if (smile > 120){
        
      textSize(150);
      text(":astonished:", positions[43][0], positions[43][1])
        
      } else{
      textSize(150);
      text(":neutral_face:", positions[43][0], positions[43][1])
      }
    if (frown < 160){
        
      textSize(150);
      text(":weary:", positions[43][0], positions[43][1])
        
      }
        // uncomment the line below to show an estimate of amount "smiling"
        // rect(20, 20, smile * 3, 20);
        // uncomment for a surprise
        noStroke();
        fill(0, 255, 255);
        ellipse(positions[62][0], positions[62][1], 50, 50);
      
    }
}