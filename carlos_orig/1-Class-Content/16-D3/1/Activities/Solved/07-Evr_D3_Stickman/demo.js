var $svg = d3.select("body").append("svg");

$svg.attr("width", "100px").attr("height", "100px");

$svg.append("circle")
    .attr("cx", 50)
    .attr("cy", 25)
    .attr("r", 25)
    .attr("stroke", "gray")
    .attr("stroke-width", "5")
    .attr("fill", "none");

// Show how to bind the svg to data

var r_values = [5, 15, 25];

var $svg = d3.select("body").append("svg");

$svg.attr("width", "100px").attr("height", "100px");

$circles = $svg.selectAll("circle").data(r_values);

$circles.enter().append("circle")
    .attr("cx", 50)
    .attr("cy", 25)
    .attr("r", function(d) {
        return d;
    })
    .attr("stroke", "gray")
    .attr("stroke-width", "5")
    .attr("fill", "none");
