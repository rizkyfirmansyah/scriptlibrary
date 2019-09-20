
library(DBI)
library(RPostgreSQL)
db <- dbConnect(RPostgres::Postgres(), host='wri-indonesia.id', dbname='social_forestry', user='postgres', password='WRIpass18!')

library(ggplot2)
library(dplyr)
library(sqldf)
library(ggplot2)
library(reshape2)
#library(xlsx)
library(sf)
library(DT)
library(gridExtra)
library(stringr)

# remove all the variables stored in global environment if needed
rm(list = ls())

# Specify working directory or predefined parameters here
path <- 'D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Social Forestry/Results/'
path_plot <- 'D:/DATA/GEOSPATIAL/ADHOC ANALYSIS/Social Forestry/Results/plot/'

## Aggregate the Forest cover loss by its province (Forest Cover Loss before the establishment of permit)

# use where loss_description = 'before' if you would like to see the trend 5 years backwards since establishment

lb_query <- "SELECT province, sf_class, type, year, round(CAST(avg(s.total_ha) as numeric), 3) as avg, array_to_string(array_agg(loss_year ORDER BY loss_year), ', ') as loss_year
FROM (
      SELECT province, sf_class, type, year, gridcode + 2000 AS loss_year, loss_status, sum(ha) as total_ha
      FROM idn_adm2_fcl_fa_loss
      WHERE loss_description = 'before'
      GROUP BY 1, 2, 3, 4, 5, 6) AS s
GROUP BY 1, 2, 3, 4
HAVING round(CAST(avg(s.total_ha) as numeric), 3) > 0
ORDER BY 1, 4;"

loss_before <- dbGetQuery(db, statement = lb_query)
colnames(loss_before) <- c("Province", "Forest Area", "Social Forestry (SF) Scheme", "SF Establishment Year", "Average Forest Loss (Ha)", "Loss Year (Before)")
#datatable(head(loss_before, n = nrow(loss_before)))


## Aggregate the Forest cover loss by its (Forest Cover Loss after the establishment of permit)

# use where loss_description = 'after' if you would like to see the trend upcoming 5 years since establishment
la_query <- "SELECT province, sf_class, type, year, round(CAST(avg(s.total_ha) as numeric), 3) as avg, array_to_string(array_agg(loss_year ORDER BY loss_year), ', ') as loss_year
FROM (
      SELECT province, sf_class, type, year, gridcode + 2000 AS loss_year, loss_status, sum(ha) as total_ha
      FROM idn_adm2_fcl_fa_loss
      WHERE loss_status = 'after'
      GROUP BY 1, 2, 3, 4, 5, 6) AS s
GROUP BY 1, 2, 3, 4
HAVING round(CAST(avg(s.total_ha) as numeric), 3) > 0
ORDER BY 1, 4;"

loss_after <- dbGetQuery(db, statement = la_query)
colnames(loss_after) <- c("Province", "Forest Area", "Social Forestry (SF) Scheme", "SF Establishment Year", "Average Forest Loss (Ha)", "Loss Year (After)")
#datatable(head(loss_after, n = nrow(loss_after)))

## Disaggregate the Forest cover loss by its social forestry schemes

query <- "SELECT i1.sf_id, i1.sf_name, i1.province, i1.sf_class, i1.type, i1.sk_year, i1.avg_ha_before, i1.loss_gc_before, i2.avg_ha_after, i2.loss_gc_after
FROM (
	SELECT sf_id, sf_name, province, sf_class, type, year as sk_year, round(CAST(sum(ha) / count(distinct(gridcode)) as numeric), 3) as avg_ha_before, array_to_string(array_agg(DISTINCT(gridcode + 2000)), ', ') as loss_gc_before
      FROM idn_adm2_fcl_fa_loss
      WHERE loss_status = 'before'
      GROUP BY 1, 2, 3, 4, 5, 6
			HAVING round(CAST(sum(ha) / count(distinct(gridcode)) as numeric), 3) > 0
			ORDER BY sf_id
			) i1
INNER JOIN (
	SELECT sf_id, sf_name, province, sf_class, type, year, round(CAST(sum(ha) / count(distinct(gridcode)) as numeric), 3) as avg_ha_after, array_to_string(array_agg(DISTINCT(gridcode + 2000)), ', ') as loss_gc_after
      FROM idn_adm2_fcl_fa_loss
      WHERE loss_status = 'after'
      GROUP BY 1, 2, 3, 4, 5, 6
			HAVING round(CAST(sum(ha) / count(distinct(gridcode)) as numeric), 3) > 0
			ORDER BY sf_id
			) i2
ON (i1.sf_id = i2.sf_id and i1.sf_class = i2.sf_class)
ORDER BY 3, 4, 6;"

loss_per_sf <- dbGetQuery(db, statement = query)
colnames(loss_per_sf) <- c("ID", "Kelompok/Nama Perhutanan Sosial", "Provinsi", "Kawasan Hutan", "Skema Perhutanan Sosial", "Tahun PS", "Rata-Rata Kehilangan Tutupan Pohon (Ha) Sebelum Izin PS", "Tahun Kehilangan Tutupan Pohon Sebelum Izin PS", "Rata-Rata Kehilangan Tutupan Pohon (Ha) Setelah Izin PS", "Tahun Kehilangan Tutupan Pohon Setelah Izin PS")
#datatable(head(loss_per_sf, n = nrow(loss_per_sf)), options = list(pageLength = 5))

## Determine the FC extent, projection, and attribute information

# Read the feature class; using sf package much faster than rgdal!
# idn_social_forestry <- st_read(dsn=con_dsn, layer = 'idn_adm2_tcl')

#summary(idn_social_forestry)


## Write the dataframe into csv format
write.csv(loss_after, file.path(path, "loss_after.csv"))
write.csv(loss_before, file.path(path, "loss_before.csv"))
write.csv(loss_per_sf, file.path(path, "loss_per_sf.csv"))

# dbDisconnect(db)
colnames(loss_before) <- c("province", "forest_area", "sf_type", "sf_year", "loss_ha", "loss_year")
colnames(loss_after) <- c("province", "forest_area", "sf_type", "sf_year", "loss_ha", "loss_year")

loss_before$sf_type_en <- ifelse(loss_before$sf_type == 'Hutan Adat', 'Customary Forest',
                                 ifelse(loss_before$sf_type == 'Hutan Desa', 'Village Forest',
                                        ifelse(loss_before$sf_type == 'Hutan Kemasyarakatan', 'Community Forest',
                                               ifelse(loss_before$sf_type == 'Hutan Tanaman Rakyat', "People's Plantation Forest",
                                                      ifelse(loss_before$sf_type == 'Izin Pemanfaatan Hutan Perhutanan Sosial', 'Perhutani-based Social Forestry',
                                                             ifelse(loss_before$sf_type == 'Pengakuan dan Perlindungan Kemitraan Kehutanan', 'Partnership Forest', '')
                                                                )))))

loss_before$forest_area_en <- ifelse(loss_before$forest_area == 'Hutan Produksi', 'Production Forest',
                                     ifelse(loss_before$forest_area == 'Hutan Produksi Terbatas', 'Limited Production Forest',
                                            ifelse(loss_before$forest_area == 'Hutan Produksi Konversi', 'Convertible Production Forest',
                                                   ifelse(loss_before$forest_area == 'Hutan Konservasi', "Conservation Forest",
                                                          ifelse(loss_before$forest_area == 'Hutan Lindung', 'Protected Forest',
                                                                 ifelse(loss_before$forest_area == 'Areal Penggunaan Lain', 'Non Forest', '')
                                                          )))))

loss_after$forest_area_en <- ifelse(loss_after$forest_area == 'Hutan Produksi', 'Production Forest',
                                    ifelse(loss_after$forest_area == 'Hutan Produksi Terbatas', 'Limited Production Forest',
                                           ifelse(loss_after$forest_area == 'Hutan Produksi Konversi', 'Convertible Production Forest',
                                                  ifelse(loss_after$forest_area == 'Hutan Konservasi', "Conservation Forest",
                                                         ifelse(loss_after$forest_area == 'Hutan Lindung', 'Protected Forest',
                                                                ifelse(loss_after$forest_area == 'Areal Penggunaan Lain', 'Non Forest', '')
                                                         )))))

loss_after$sf_type_en <- ifelse(loss_after$sf_type == 'Hutan Adat', 'Customary Forest',
                                ifelse(loss_after$sf_type == 'Hutan Desa', 'Village Forest',
                                       ifelse(loss_after$sf_type == 'Hutan Kemasyarakatan', 'Community Forest',
                                              ifelse(loss_after$sf_type == 'Hutan Tanaman Rakyat', "People's Plantation Forest",
                                                     ifelse(loss_after$sf_type == 'Izin Pemanfaatan Hutan Perhutanan Sosial', 'Perhutani-based Social Forestry',
                                                            ifelse(loss_after$sf_type == 'Pengakuan dan Perlindungan Kemitraan Kehutanan', 'Partnership Forest', '')
                                                     )))))


title_before <- "A boxplot showing the average Forest cover loss\nfrom 2001 - the establishment per schemes"
title_after <- "A boxplot showing the average Forest cover loss\nfrom the establishment per schemes - 2018"
subtitle_before <- "2001 - the establishment per schemes"
subtitle_after <- "the establishment per schemes - 2018"
bottom_title <- 'Average Forest Cover Loss (Ha)'
top_title <- 'A boxplot showing the average Forest cover loss'

# boxplot grouped by social forestry
"
ggplot() +
	geom_boxplot(data = loss_after, aes(x = sf_type_en, y = loss_ha, fill = sf_type_en)) +
	geom_boxplot(data = loss_before, aes(x = sf_type_en, y = loss_ha, fill = sf_type_en)) +
	geom_jitter(width = 0.1, alpha = 0.2) +
	labs(fill = 'Social Forestry (Scheme)', title = 'title') +
	ylab('Average Forest Cover Loss (Ha)') +
	theme_bw(base_size = 11) +
	theme(legend.position = 'none', axis.title.y = element_blank()) +
	coord_flip()
"

boxplot_sf <- function(var, x = var$sf_type_en, y = var$loss_ha, fill = var$sf_type_en, title = '') {
  ggplot() +
  geom_boxplot(data = var, aes(x = x, y = y, fill = fill)) +
  scale_x_discrete(labels = function(x) str_wrap(x, width = 10)) +
  geom_jitter(width = 0.1, alpha = 0.2) +
  labs(title = title) +
  theme_bw(base_size = 11) +
  theme(legend.position = 'none', axis.title.y = element_blank(), axis.title.x = element_blank()) +
  scale_fill_manual(values=c("Customary Forest" = "#ef63ff","Village Forest" = "#4f76f7","Community Forest" = "#52c4c4","People's Plantation Forest" = "#ffc847","Perhutani-based Social Forestry" = "#7cff5e","Partnership Forest" = "#ff5c21")) +
  coord_flip()
}

box_loss_before <- boxplot_sf(loss_before, title = subtitle_before) + ylim(0, 600)
box_loss_after <- boxplot_sf(loss_after, title = subtitle_after) + theme(axis.ticks.y = element_blank(), axis.text.y = element_blank())

## boxplot filtered

boxplot_sf_filtered <- function(var, title = '', f = 'Hutan Lindung') {
  ggplot() +
    geom_boxplot(data = var[var$forest_area %in% f, ], aes(x = sf_type_en, y = loss_ha, fill = sf_type_en)) +
    scale_x_discrete(labels = function(x) str_wrap(x, width = 10)) +
    geom_jitter(width = 0.1, alpha = 0.2) +
    labs(title = title, fill = 'Social Forestry') +
    theme_bw(base_size = 9) +
    theme(legend.position = 'none', axis.title.y = element_blank(), axis.title.x = element_blank()) +
    scale_fill_manual(values=c("Customary Forest" = "#ef63ff","Village Forest" = "#4f76f7","Community Forest" = "#52c4c4","People's Plantation Forest" = "#ffc847","Perhutani-based Social Forestry" = "#7cff5e","Partnership Forest" = "#ff5c21")) +
    coord_flip()
}

box_loss_before_hl <- boxplot_sf_filtered(loss_before, title = subtitle_before, f = 'Hutan Lindung')
box_loss_after_hl <- boxplot_sf_filtered(loss_after, title = subtitle_after, f = 'Hutan Lindung') + scale_y_continuous(position = "top")

box_loss_before_hk <- boxplot_sf_filtered(loss_before, title = subtitle_before, f = 'Hutan Konservasi')
box_loss_after_hk <- boxplot_sf_filtered(loss_after, title = subtitle_after, f = 'Hutan Konservasi')

box_loss_before_apl <- boxplot_sf_filtered(loss_before, title = subtitle_before, f = 'Areal Penggunaan Lain')
box_loss_after_apl <- boxplot_sf_filtered(loss_after, title = subtitle_after, f = 'Areal Penggunaan Lain') + theme(axis.ticks.y = element_blank(), axis.text.y = element_blank())

boxplot_sf_hp <- function(var, title = title_before) {
  var %>%
    filter(forest_area %in% c('Hutan Produksi', 'Hutan Produksi Terbatas', 'Hutan Produksi Konversi')) %>%
    ggplot(aes(x = sf_type_en, y = loss_ha, fill = sf_type_en)) +
    geom_boxplot() +
    geom_jitter(width = 0.1, alpha = 0.2) +
    labs(title = title, fill = "Social Forestry") +
    ylab('Average Forest Cover Loss (Ha)') +
    xlab('Social Forestry Schemes') +
    theme_bw(base_size = 11) +
    theme(legend.position = 'bottom', axis.title.y = element_blank(), axis.ticks.x = element_blank(), axis.text.x = element_blank()) +
    scale_fill_manual(values=c("Customary Forest" = "#ef63ff","Village Forest" = "#4f76f7","Community Forest" = "#52c4c4","People's Plantation Forest" = "#ffc847","Perhutani-based Social Forestry" = "#7cff5e","Partnership Forest" = "#ff5c21")) +
    facet_wrap(~forest_area_en, ncol = 3)
}

box_loss_before_hp <- boxplot_sf_hp(loss_before, title = paste(title_before, 'within Production Forest', sep = " "))
box_loss_after_hp <- boxplot_sf_hp(loss_after, title = paste(title_after, 'within Production Forest', sep = " "))


grid.arrange(box_loss_before, box_loss_after, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within all Forest area'), bottom = bottom_title)
grid.arrange(box_loss_before_hl, box_loss_after_hl, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Protected Forest'), bottom = bottom_title)
grid.arrange(box_loss_before_hk, box_loss_after_hk, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Conservation Forest'), bottom = bottom_title)
grid.arrange(box_loss_before_apl, box_loss_after_apl, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Non Forest'), bottom = bottom_title)
"
#ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_apl.jpg'), plot = grid.arrange(box_loss_before_apl, box_loss_after_apl, nrow = 1, widths = c(5, 4)), width = 9, height = 7, units = 'in', dpi = 300, limitsize = FALSE)
ggsave(paste0(path_plot, 'boxplot_per_scheme_loss.jpg'), plot = grid.arrange(box_loss_before, box_loss_after, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within all Forest area'), bottom = bottom_title), width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)
ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_hl.jpg'), plot = grid.arrange(box_loss_before_hl, box_loss_after_hl, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Protected Forest'), bottom = bottom_title), width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)

ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_hk.jpg'), plot = grid.arrange(box_loss_before_hk, box_loss_after_hk, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Conservation Forest'), bottom = bottom_title), width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)
ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_apl.jpg'), plot = grid.arrange(box_loss_before_apl, box_loss_after_apl, nrow = 1, widths = c(5, 4), top = paste0(top_title, ' within Non Forest'), bottom = bottom_title), width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)

ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_before_hp.jpg'), plot = box_loss_before_hp, width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)
ggsave(paste0(path_plot, 'boxplot_per_scheme_loss_after_hp.jpg'), plot = box_loss_after_hp, width = 8, height = 6, units = 'in', dpi = 300, limitsize = FALSE)
"