# LogoClarifier

  Sets the alpha values of all pixels outside of an inner circle with a specified
  radius and coordinates to 0 for a given png image. This means that if a logo is 
  represented as a png but is surrounded by white pixels instead of transparent ones, 
  this function can make the surrounding white pixels transparent, while keeping the white
  pixels in the logo solid. 
  
  I have included an example of a case where this might be useful.
  
  Looking forward, it might be interesting to have the ability to change the shape of the 
  "protected area" to something like an oval or rectangle
