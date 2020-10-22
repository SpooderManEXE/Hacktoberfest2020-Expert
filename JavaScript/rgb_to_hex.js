// this function converts a rgb color value to hex value

function rgbToHex(r, g, b) {
  const red = r.toString(16);
  const green = g.toString(16);
  const blue = b.toString(16);

  if (red.length == 1) {
    red = "0" + red;
  }

  if (green.length == 1) {
    green = "0" + green;
  }

  if (blue.length == 1) {
    blue = "0" + blue;
  }
}
