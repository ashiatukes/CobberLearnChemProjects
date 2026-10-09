import pandas as pd
annotations = pd.read_excel("../assay_annotations_invitrodb_v4_3_AUG2025.xlsx")
print(annotations.head())
for column in annotations.columns:
    print(column)
    print(annotations[column].head(20))


