float rectSize = 100;

void setup(){
  size(800,800);
}
    
void draw(){
  background(255);
  
  mouseX = constrain(mouseX, 10, width);
  mouseY = constrain(mouseY, 10, height);
  
  fill(255, 0, 0);
  stroke(0,255, 0);
  strokeWeight(10);
  
  for (int y=0; y<height; y+=mouseY) {
    for (int x=0; x<width; x+=mouseX) {
      arc(x, y, rectSize, rectSize, 0, PI);
    }
  }
}
