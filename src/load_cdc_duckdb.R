
library(tidyverse)
library(duckdb)
library(duckplyr)


con <- dbConnect(duckdb(), dbdir = "cdc.duckdb", read_only = FALSE)

duckdb_read_csv(
  con, 
  name="covid19", 
  files="covid19/COVID-19_Case_Surveillance_Public_Use_Data_with_Geography_20241023.csv", 
  header = TRUE,
  nrow.check=10000,
  col.types = c(
    "case_month" = "string",
    "res_state" = "string",
    "state_fips_code" = "string",
    "res_county" = "string",
    "county_fips_code" = "string",
    "age_group" = "string",
    "sex" = "string",
    "race" = "string",
    "ethnicity" = "string",
    "case_positive_specimen_interval" = "string",
    "case_onset_interval" = "string",
    "process" = "string",
    "exposure_yn" = "string",
    "current_status" = "string",
    "symptom_status" = "string",
    "hosp_yn" = "string",
    "icu_yn" = "string",
    "death_yn" = "string",
    "underlying_conditions_yn" = "string"
  )
)
