
# Appendix A: Overview

This repository contains data and code to evaluate the impacts of two circular economy interventions using a Multi-Regional Environmentally Extended Input-Output Analysis (MR-EEIOA) framework.  

The scope covers key regions including Latin America & Caribbean (LAC), the European Union (EU), China, the United States (US), and the Rest of the World (RoW).

## Modeled Interventions

- **d.3 Uruguay's Plastics Recycling**  
- **b.1 Costa Rica's Increase of Biodegradable Waste from Food**

These interventions are derived from national circular economy strategies and modeled with sectoral and regional aggregations in the EXIOBASE database. The scenarios simulate changes in socio-economic and environmental indicators such as greenhouse gas emissions, nutrient flows, land use, value added, and employment.

**Note:** The numbering and labels of interventions correspond directly to the entries found in the Excel file `LATAM_data_entry_final.xlsx` located in the `01_data` folder.

## Repository Structure

- **01_data**: Contains the Excel data files including `LATAM_data_entry_final.xlsx` that hold sectoral assumptions, intervention numbers, and detailed scenario data.  
- **02_SectoralAggregations**: Sector and region mappings aggregating detailed EXIOBASE data into meaningful groups for analysis.  
- **03_Code**: Main MR-EEIOA modeling code for simulating the circular interventions for Costa Rica (b.1) and Uruguay (d.3).  
- **04_Results**: Model output results organized for visualization and interpretation.
