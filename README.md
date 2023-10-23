# HackDuke2023

## Inspiration

Day after day, the media is filled with dreadful articles relating to climate change and the natural disasters inflicted by it. As a result, there is a growing uncertainty about what places will be safe to live in the coming decades. Livability seeks to tackle this issue by presenting users with vivid and dynamic heat maps of the globe that show you how livable a certain will be in the future.

## What it does

Livability makes use of climate models based on data released by the IPCC to make predictions about the feasibility of living healthily and safely in a location. Users can access the next 30 years of climate data and its effects across the entire U.S. via the map visualization. The more intense the red is on the map, the less the potential livability will be.

## How we built it

In order to create a heat map that visualizes such livability, we needed to quantity in a standardized index for this “livability,” which we researched and denoted as the “livability index.” The livability index considers four environmental factors that we feel would affect one’s ability to live healthily and safely in a location. The four factors we chose were pm2.5 (particulate matter with a size of 2.5 micrometers and below) concentrations measured in (ug / m^3), rainfall amounts measured in millimeters, shortwave radiation from the sun measured in (mJ / m^2), and temperature highs/lows in Fahrenheit.

In order to calculate a total index, we calculated indices for each of the four factors separately and then combined them into a final index with a range of 0 - 100. The index for the pm2.5 was based on a square root function with the concentrations as the input, so the smallest concentration was best. The index for rainfall was calculated from a Gaussian distribution of the average rainfall. The number of standard deviations from the average was placed into a square root function. The index for the shortwave radiation was based on a square root function, where values less than 100 mJ / m^2 was considered safe and did not add to the index, but anything past that value was considered slightly dangerous and possibly harmful by the WHO, so this is where we began increasing the index. Lastly, the index for the temperature was also based on a Gaussian distribution, where temperatures below 80 degrees Fahrenheit and above 36 Fahrenheit were considered safe. The number of standard deviations away from that range was placed into a square root function. We calculated the rain, temperature, and radiation indices in both the summer months of June and July as well as December, then accepted the highest index between the summer and winter and used that to represent the year. All of these indices were summated and then placed into a sigmoid function to visually quantify the differences in indices.

Using those livability indices, we paired them to their corresponding latitude and longitude on a heatmap layer displayed over our map. Higher index values implied less livability and a red gradient, while lower index values implied more livability and a green and white gradient.

## Challenges we ran into

Properly formatting the JSON files for use by the Google Maps API was extremely challenging for us to figure out. Along with this, we had a limited amount of requests that could’ve been made to the climate API, meaning that our attempts to properly export the data for our website were limited.

## Accomplishments that we're proud of

The creation of the map displaying livability was a proud feat, as it was very neat to see our custom-calculated data displayed in such a way over a map.

## What we learned

Throughout our process of developing the map, we learned the power of external APIs and the ability to understand documentation written for them. Many simple problems can be solved if you spend a little bit of time understanding how the API actually works, instead of googling or using StackOverflow. Our team also recognized the value of planning. Through planning, your project can be created in a much more stable process, as under-planning results in unexpected bugs and issues.

## What's Next for Livability

In the future, we plan to expand our livability index calculations to the entire world, not just the United States. We will also introduce tools to the map granting more insight into how livable a specific area will be and what factors contribute to its livability, as opposed to only offering a large-scale map as we have now.

[Devpost](https://devpost.com/software/livability-ry06i5) 

