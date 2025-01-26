library(tidyverse)
library(knitr)
library(kableExtra)  # For nice tables
library(scales)      # For number formatting
library(cowplot)     # For arranging multiple plots

# Helper function for frequency tables
create_freq_table <- function(data, var_name) {
  data %>%
    count(!!sym(var_name), name = "Count") %>%
    drop_na() %>%
    mutate(
      Percentage = Count / sum(Count) * 100,
      Percentage = round(Percentage, 2)
    ) %>%
    kable(format = "html", caption = paste("Distribution of", var_name)) %>%
    kable_styling(bootstrap_options = c("striped", "hover", "condensed"))
}

# Helper function for categorical variables visualization
plot_categorical <- function(data, var_name) {
  ggplot(data, aes(x = !!sym(var_name))) +
    geom_bar() +
    theme_minimal() +
    labs(title = paste("Distribution of", var_name),
         y = "Count") +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

# Helper function for boolean variables
plot_boolean <- function(data, var_name) {
  ggplot(data, aes(x = !!sym(var_name), fill = !!sym(var_name))) +
    geom_bar() +
    scale_fill_manual(values = c("TRUE" = "#619CFF", "FALSE" = "#F8766D")) +
    theme_minimal() +
    labs(title = paste("Distribution of", var_name),
         y = "Count") +
    theme(legend.position = "none")
}
