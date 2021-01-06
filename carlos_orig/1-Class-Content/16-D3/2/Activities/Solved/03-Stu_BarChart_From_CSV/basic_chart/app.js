// Define SVG area dimensions
var svgWidth = 960;
var svgHeight = 640;

// Select body, append SVG area to it, and set the dimensions
var svg = d3
  .select("body")
  .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

// Load data from hours-of-tv-watched.csv
d3.csv("hours-of-tv-watched.csv", function(error, tvData) {

  // Throw an error if one exists
  if (error) throw error;

  var barWidth = svgWidth / tvData.length;
  svg.selectAll(".bar")
    .data(tvData)
    .enter()
    .append("rect")
      .attr("class", "bar")
      .attr("x", (d, i) => i * barWidth)
      .attr("y", d => svgHeight - d.hours)
      .attr("width", barWidth)
      .attr("height", d => d.hours);
});
