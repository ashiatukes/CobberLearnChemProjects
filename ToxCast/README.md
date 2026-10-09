# ToxCast Estrogen Receptor Project

## Project Goal

The goal of this project is to use ToxCast/Tox21 data to study chemicals that may activate the estrogen receptor. I am focusing on assays that use human systems and looking at different parts of estrogen receptor activity.

The 2013 Zhang et al. study is being used as a model for this project. Their study combined information from multiple estrogen receptor assays to classify chemicals as active or inactive. My goal is to explore newer ToxCast data and determine which assays would be most useful for our dataset.
## Step 1: Exploring the ToxCast Data

I downloaded the assay annotation and assay target mapping files from the EPA ToxCast invitrodb v4.3 database.

I created ExploreToxCast.py to open the assay annotation file in Python and explore what information is available. I looked at the assay names, descriptions, biological targets, human cell systems, time points, and what each assay measures.

This helped me narrow the data down to assays related to estrogen receptor activity instead of using every assay in the database.

## Step 2: Selecting Assays

I decided to focus on human systems and estrogen receptor agonist activity. Instead of using every estrogen receptor assay available, I selected five assays that look at different parts of the estrogen receptor response.

The five assays selected are:

- NVS_NR_hER
- OT_ER_EREGFP_0480
- ATG_ERE_CIS_up
- TOX21_ERa_BLA_Agonist_ratio
- ACEA_ER_80hr

I chose these because together they give us different types of information instead of repeating the same test. They can show whether a chemical interacts with the estrogen receptor and whether that interaction leads to activity or a response in human cells.

The next step is to look at the amount and quality of data available for each assay before deciding if all five should be included in the final dataset.

Step 3: Challenges and Troubleshooting underneath your existing text.
I had many challenges that seemed to be on a loop when it came to commit and push. I had to try multiple avenues that led to multiple dead ends. The only way I was able to get it to work was by draggingthe ToxCast folder from my finder window directly to GitHub. 
