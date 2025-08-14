# -*- coding: utf-8 -*-
"""

MARIO Quick Start using EXIOBASE v3.9.4

Note: A GHG emission extension is retrieved from IOT_2020 from v3.8.2


Updated on 14/08 by Giulia Moncada

@author: aguilarga
"""

import mario
import pandas as pd

# Uploading Exiobase
## Please download EXIOBASE version from https://zenodo.org/records/14614930

IOT_path = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\IOT_2020_ixi" # Define the desired path to the folder where Exiobase should be downloaded
exiobase = mario.parse_exiobase(
    table = 'IOT',
    unit = 'Monetary',
    path = IOT_path)

# Test balance
exiobase.is_balanced('flows', data_set='baseline', margin=0.05, as_dataframe=False)

#Checking matrices
check = exiobase.matrices['baseline'].keys()

#%%

# Adding Impact account from EXIOBASE to Extensions E
path_extensions = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\Extensions\new_E_accounts(1).xlsx"
#exiobase.get_extensions_excel(matrix='E',path=path_extensions) ##Only use for adding new extensions in E
units = pd.read_excel(path_extensions, sheet_name='units',index_col=[0],header=[0])
exiobase.add_extensions(
   io=path_extensions,
   units=units,
   matrix='E')

#%% Aggregation
path_aggr = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\Aggregations\aggregation_Costa_Rica.xlsx"
#exiobase.get_aggregation_excel(path = path_aggr,) # Use only when it's a new aggregation
exiobase.aggregate(
    io= path_aggr,
   levels = ["Satellite account",
        "Consumption category",
        "Region",
        "Sector"]) # CoreModel.aggregate retrieves the aggregated database based on the Aggregation Excel file

#%%Exporting table
path_table = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\Aggregations\exiobase_simplified.xlsx"
exiobase.to_excel(
    path=path_table,
    flows=True,
    coefficients=True) # CoreModel.to_excel exports the aggregated database


#%% Define the indicators:
    
CO2_all = ['GHG emissions (GWP100) from v3.8.2']



Employment_people = ['Employment people: Low-skilled male', 
'Employment people: Low-skilled female',
'Employment people: Medium-skilled male',
'Employment people: Medium-skilled female',
'Employment people: High-skilled male',
'Employment people: High-skilled female']

Employment_hours = ["Employment hours: High-skilled female",
                   "Employment hours: High-skilled male",
"Employment hours: Low-skilled female",
"Employment hours: Low-skilled male",
"Employment hours: Medium-skilled female",
"Employment hours: Medium-skilled male"]


ValueAdded = ['Taxes less subsidies on products purchased: Total',
'Other net taxes on production',
"Compensation of employees; wages, salaries, & employers' social contributions: Low-skilled",
"Compensation of employees; wages, salaries, & employers' social contributions: Medium-skilled",
"Compensation of employees; wages, salaries, & employers' social contributions: High-skilled",
'Operating surplus: Consumption of fixed capital',
'Operating surplus: Rents on land',
'Operating surplus: Royalties on resources',
'Operating surplus: Remaining net operating surplus']

Nutrients = ["Nutrients"]

Land_use = ["Land use"]

#%%
# Calculation Scenario 1, Costa Rica: Decreasing -40% of LAC Waste, while Increase 40% of Composting of biowaste from LAC 

path_s1 = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\Scenarios\shock_s1_CR.xlsx" 
# exiobase.get_shock_excel(path=path_s1) ## Use only to create new scenario files

exiobase.shock_calc(
    io= path_s1,
    z= True,
    scenario='Scenario 1',
    force_rewrite=True,
    notes=['Decrease of LAC Waste by 40% and increase of composting of biowaste by 40% in LAC'])
 # df.shock_cal calculates the scenarios based on the Shock file data

#%% Intervention CR: Value added by region

V_Scenario_1_CR = exiobase.query(
    matrices= 'V',
    scenarios='Scenario 1',
    ).loc[ValueAdded].sum()

V_delta_s1_CR = exiobase.query(
    matrices='V',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[ValueAdded].sum()

V_delta_s1_CR_region = V_delta_s1_CR.groupby(level= 0).sum().sort_values()
V_delta_s1_CR_tot = V_delta_s1_CR.groupby(level= 0).sum().sum()
V_delta_s1_CR_region.to_excel('V_delta_region_s1_CR.xlsx', index=True)


#%% Intervention CR: GHG by region
GHG_Scenario_1_CR = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[CO2_all].sum()

GHG_delta_s1_CR = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[CO2_all].sum()


GHG_delta_s1_CR_region = GHG_delta_s1_CR.groupby(level= 0).sum().sort_values()
GHG_delta_s1_CR_tot = GHG_delta_s1_CR.groupby(level= 0).sum().sum()
GHG_delta_s1_CR_region.to_excel('GHG_delta_region_s1_CR.xlsx', index=True)

#%% Intervention CR:employment by region
emp_Scenario_1_CR= exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    ).loc[Employment_people].sum()

emp_delta_s1_CR = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Employment_people].sum()

emp_delta_s1_CR_region = emp_delta_s1_CR.groupby(level= 0).sum().sort_values()
emp_delta_s1_CR_tot = emp_delta_s1_CR.groupby(level= 0).sum().sum()
emp_delta_s1_CR_region.to_excel('emp_delta_region_s1_CR.xlsx', index=True)
#%% Intervention CR: Nutrients by region
Nutrients_Scenario_1_CR = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[Nutrients].sum()

Nutrients_delta_s1_CR = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Nutrients].sum()

Nutrients_delta_s1_CR_region = Nutrients_delta_s1_CR.groupby(level= 0).sum().sort_values()
Nutrients_delta_s1_CR_tot = Nutrients_delta_s1_CR.groupby(level= 0).sum().sum()
Nutrients_delta_s1_CR_region.to_excel('Nutrients_delta_region_s1_CR.xlsx', index=True)

#%%Intervention CR: Land use by region

Land_use_Scenario_1_CR = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[Land_use].sum()

Land_use_delta_s1_CR = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Land_use].sum()

Land_use_delta_s1_CR_region = Land_use_delta_s1_CR.groupby(level= 0).sum().sort_values()
Land_use_delta_s1_CR_tot = Land_use_delta_s1_CR.groupby(level= 0).sum().sum()
Land_use_delta_s1_CR_region.to_excel('Land_use_delta_region_s1_CR.xlsx', index=True)
#%%Calculation Scenario 2, Uruguay: Decreasing 27% of landfills for food waste in LAC, while increasing composting waste system in LAC
path_s2 = r"C:\Users\Giulia\MS_Industrial Ecology\Thesis\Scenario Analysis\Scenarios\shock_s2_UY.xlsx"
# exiobase.get_shock_excel(path=path_s2) ## Use only to create new scenario files 
exiobase.shock_calc(
    io= path_s2,
    z= True,
    scenario='Scenario 2',
    force_rewrite=True,
    notes=["Decrease of 27% in waste disposal,and increase of 27% of composting of biowaste"])
#%% Intervention UY: Value added by region

V_Scenario_1_UY = exiobase.query(
    matrices= 'V',
    scenarios='Scenario 1',
    ).loc[ValueAdded].sum()

V_delta_s1_UY = exiobase.query(
    matrices='V',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[ValueAdded].sum()

V_delta_s1_UY_region = V_delta_s1_UY.groupby(level= 0).sum().sort_values()
V_delta_s1_UY_tot = V_delta_s1_UY.groupby(level= 0).sum().sum()
V_delta_s1_UY_region.to_excel('V_delta_region_s1_UY.xlsx', index=True)


#%% Intervention UY: GHG by region
GHG_Scenario_1_UY = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[CO2_all].sum()

GHG_delta_s1_UY = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[CO2_all].sum()

GHG_delta_s1_UY_region = GHG_delta_s1_CR.groupby(level= 0).sum().sort_values()
GHG_delta_s1_UY_tot = GHG_delta_s1_UY.groupby(level= 0).sum().sum()
GHG_delta_s1_UY_region.to_excel('GHG_delta_region_s1_UY.xlsx', index=True)

#%% Intervention CR:employment by region
emp_Scenario_1_UY= exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    ).loc[Employment_people].sum()

emp_delta_s1_UY = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Employment_people].sum()

emp_delta_s1_UY_region = emp_delta_s1_UY.groupby(level= 0).sum().sort_values()
emp_delta_s1_UY_tot = emp_delta_s1_UY.groupby(level= 0).sum().sum()
emp_delta_s1_UY_region.to_excel('emp_delta_region_s1_UY.xlsx', index=True)
#%% Intervention CR: Nutrients by region
Nutrients_Scenario_1_UY = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[Nutrients].sum()

Nutrients_delta_s1_UY = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Nutrients].sum()

Nutrients_delta_s1_UY_region = Nutrients_delta_s1_UY.groupby(level= 0).sum().sort_values()
Nutrients_delta_s1_UY_tot = Nutrients_delta_s1_UY.groupby(level= 0).sum().sum()
Nutrients_delta_s1_UY_region.to_excel('Nutrients_delta_region_s1_UY.xlsx', index=True)

#%%Intervention CR: Land use by region

Land_use_Scenario_1_UY = exiobase.query(
    matrices= 'E',
    scenarios='Scenario 1',
    ).loc[Land_use].sum()

Land_use_delta_s1_UY = exiobase.query(
    matrices='E',
    scenarios='Scenario 1',
    base_scenario='baseline',
    type='absolute',
    ).loc[Land_use].sum()

Land_use_delta_s1_UY_region = Land_use_delta_s1_UY.groupby(level= 0).sum().sort_values()
Land_use_delta_s1_UY_tot = Land_use_delta_s1_UY.groupby(level= 0).sum().sum()
Land_use_delta_s1_UY_region.to_excel('Land_use_delta_region_s1_UY.xlsx', index=True)




