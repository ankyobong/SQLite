import pdfplumber
import pandas as pd
# pdffile = "Inv_11390_from_KOTRA_Silico_new.pdf"
pdffile = "18.pdf"
with pdfplumber.open(pdffile) as pdf:
    d = pdf.pages
    table = d[0].extract_tables(table_settings={"vertical_strategy": "text",
                                             "horizontal_strategy": "text",
                                             })
    df = pd.DataFrame(table[0])
    print(df)

df.to_csv(pdffile+".txt", sep=',', header=False, index=False)

# f = open(pdffile+".txt", 'w', encoding='utf-8')
# f.write(df)
# f.close()
