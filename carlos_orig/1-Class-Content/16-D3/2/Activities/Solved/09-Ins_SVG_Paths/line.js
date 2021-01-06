var dataArray = [{x: 5, y:1}, {x:10, y:3}, {x:20, y:5}];

// line is a function generator that we can use as a function later on
var line = d3.line()
     .x(d => d.x*10)
     .y(d => d.y*10);

var svg = d3.select("svg");

svg.append("path")
    .attr("fill", "none")
    .attr("stroke", "orange")
    .attr("stroke-width", 5)
    .attr("d", line(dataArray));
