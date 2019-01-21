library(ggplot2)

## Simple plot
ggplot(forest_legal_forest_loss, aes(x = Tahun, y = `Hutan Konservasi`)) + geom_bar(stat = "identity")


## Plotting with label
ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`)) + geom_bar(stat = "identity", fill = "deeppink") + geom_text(aes(label = `Areal Penggunaan Lain`), vjust = 1.6, color = "white", size = 3.5) + theme_classic()


## restructure x axis
ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`)) + geom_bar(stat = "identity", fill = "deeppink") + geom_text(aes(label = `Areal Penggunaan Lain`), vjust = 1.6, color = "white", size = 3.5) + theme_classic() + scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016))

## changing the number of decimal places on x axis
roundTwo <- function(x) sprintf("%.2f", x)

## bar chart
ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`, label = sprintf("%0.2f", round(`Areal Penggunaan Lain`, digits = 2)))) +
    geom_bar(stat = "identity", fill = "deeppink") +
    geom_text(size = 3, vjust = 1.2, fontface = "bold") +
    theme_classic() +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo) +
    geom_smooth(method = "lm", formula = y ~ x, se = FALSE) +
	labs(x = "Year", y = "Non Forest", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))
	
## line
ggplot(forest_loss_apl, aes(x = Tahun, y = `Areal Penggunaan Lain`, label = sprintf("%0.2f", round(`Areal Penggunaan Lain`, digits = 2)))) +
    geom_line(stat = "identity", colour = "deeppink") +
    # geom_text(size = 3, vjust = 1.2, fontface = "bold") +
    theme_classic() +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo, limits = c(0, 500)) +
	labs(x = "Year", y = "Non Forest (thousands of Ha)", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))
	
#### three variables on line plots
ggplot() +
    geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Konservasi`, colour = "Conservation Forest")) +
	geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Produksi`, colour = "Production Forest")) +
	geom_line(data = forest_loss_fclass, aes(x = Tahun, y = `Hutan Lindung`, colour = "Protected Forest")) +
    # geom_text(size = 3, vjust = 1.2, fontface = "bold") +
	theme(legend.position = "bottom", legend.background = element_blank(), panel.grid = element_blank(), panel.background = element_blank()) +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo, limits = c(0, 500)) +
	labs(x = "Year", y = "Forest (thousands of Ha)", colour = "Legend", caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))
	
	
	
#### reshaping wide-format to long-format using reshape2 package
library(reshape2)

forest_loss_fclass_long <- melt(forest_loss_fclass, id.vars = "Tahun")

ggplot(forest_loss_fclass_long, aes(x = Tahun, y = value, fill = variable)) +
	geom_bar(stat = "identity") +
	theme_classic() +
    scale_x_continuous(breaks = c(2001:2016), labels = c(2001:2016)) +
    scale_y_continuous(labels = roundTwo) +
	labs(x = "Year", y = "Forest (thousands of Ha)", colour = "Legend",caption = expression(italic("based on data from Global Forest Watch and Forest Legal Class (MoEF)")))
	
	
### Changing value
forest_loss_fclass_long$variable <- gsub("Hutan Lindung", "Protection Forest", forest_loss_fclass_long$variable)
forest_loss_fclass_long$variable <- gsub("Hutan Produksi", "Production Forest", forest_loss_fclass_long$variable)
forest_loss_fclass_long$variable <- gsub("Hutan Konservasi", "Conservation Forest", forest_loss_fclass_long$variable)

