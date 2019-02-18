suppressMessages(require(maps))
suppressMessages(require(ggmap))
suppressMessages(require(mapproj))
suppressMessages(require(dplyr))

library(rgdal)
library(ggplot2)
library(dplyr)
library(ggmap)
library(mapproj)
library(maps)
library(viridis)

world <- read.csv(file="/Users/sally/Desktop/world_rain_happiness_correlation_normalized.csv", header=TRUE, sep=",")

for(val in 1:100){
png(filename="/Users/sally/Desktop/Rain_Hap_norm_"+(1900+val)+".png")

map <- ggplot(data = world, aes(x=long, y=lat, group = group))

map + geom_path()

map <- ggplot(data = world, aes(x = long, y = lat, group = group))

map + geom_polygon(aes(fill = year_(1900+val)), color = 'gray', size = 0.01) + 
  scale_fill_viridis_c(limits = c(-0.5, 0.5)) + coord_fixed(1.3)

dev.off()
}

#data <- read.csv(file="/Users/sally/Desktop/2.csv", header=TRUE, sep=",")

#world = map_data("world")

#write.csv(world, "/Users/sally/Desktop/world.csv")

#head(world)
#head(data)

#map <- ggplot(data = world, aes(x=long, y=lat, group = group))

#map + geom_path()

#data %>%
#  distinct(normalized) %>%
#  write.csv("try.csv", row.names = FALSE)

#h.data <- read.csv("try.csv")
#colnames(h.data) <- c("region", "normalized")

#world <- merge(world, data, by="region")

#map <- ggplot(data = world, aes(x = long, y = lat, group = group))
#map + 
#  geom_polygon(aes(fill = normalized), color = 'blue', size = 0.1) +
#  coord_fixed(1.3)

#map <- ggplot(data = data, aes(x = long, y = lat, group = group))
#map + geom_polygon(aes(fill = normalized), color = "blue", size = 0.1) + coord_fixed(1.3)

#g <- ggplot()
#g = g + geom_map(data=world, map=world,
#                 aes(map_id=region),
#                 fill="#ffffff", color="#ffffff", size=0.15)

#g = g + geom_map(data=data, map=world,
#                 aes(fill=normalized, map_id=region),
#                 color="#ffffff", size=0.15)
#g


#dfworldmap = map_data("world")
#ggplot() + geom_polygon(aes(long,lat, group=group), 
#                        data=dfworldmap) + theme_bw() + ggtitle("2017 World Happiness")

#map + geom_polygon(aes(fill = random), color = "blue", size = 0.1) + coord_fixed(1.3)


#map + 
#  geom_polygon(aes(fill = year_1999), color = 'gray', size = 0.1) +
#  scale_fill_gradient(high = "#e34a33", low = "#fee8c8", guide = "colorbar") +
#  coord_fixed(1.3)

#map + 
#  geom_polygon(aes(fill = year_1999), color = 'gray', size = 0.1) +
#  scale_fill_gradient(high = "#e34a33", low = "#fee8c8", guide = "colorbar") +
#  coord_fixed(1.3)

#map + 
#  geom_polygon(aes(fill = random), color = 'gray', size = 0.1) +
#  scale_fill_gradient(high = '#0072B9', low = "#56B4E9", guide = "colorbar") +
#  coord_fixed(1.3)

#map + 
#  geom_polygon(aes(fill = random), color = 'gray', size = 0.1) +
#  scale_fill_gradient(high = 'steel blue', low = "light blue", guide = "colorbar") +
#  coord_fixed(1.3)
