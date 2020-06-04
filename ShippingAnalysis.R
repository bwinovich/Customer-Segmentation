library(readr)

csh <- read_csv("Company.csv", col_names = TRUE)

str(csh)

library(tidyr)
library(dplyr)

state <- csh %>%
  group_by(ShipToState) %>%
  summarise(taxable_sales = sum(TaxableSalesAmt), non_taxable_sales = sum(NonTaxableSalesAmt), total_sales = (taxable_sales+non_taxable_sales), freight = sum(FreightAmt))

state <- arrange(.data = state, desc(total_sales))
head(state)

freight_index <- state %>%
  group_by(ShipToState) %>%
  summarise(freight_index = (freight / total_sales))

state <- merge(state, freight_index, by = "ShipToState")

state <- arrange(.data = state, desc(freight_index))

topstates <- filter(state, total_sales > 100000)

write.csv(topstates, "ShippingAnalysis.csv",row.names = FALSE)
