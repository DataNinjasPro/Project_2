// Load data from hours-of-tv-watched.csv
d3.csv("hours-of-tv-watched.csv", function(error, tvData) {
  if (error) throw error;

  console.log(tvData);

  // Cast the hours value to a number for each piece of tvData
  tvData.forEach(function(data) {
    data.hours = +data.hours;
    console.log("Name", data.name);
    console.log("Hours", data.hours);
  });

  tvData.map(function(data) {
    return data.name;
  });
});
