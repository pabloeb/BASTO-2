import pandas as pd


def flat_datarows(df):
  """ funcion para aplanar los json de tabla datarows """
  flatted_df = pd.json_normalize(df.dataRowData, sep='_')
  flatted_df.columns = ['dataRowData_'+ col for col in flatted_df.columns]
  flatted_df.index = df.index
  res = pd.concat([df,flatted_df], axis=1, join='inner')
  res.drop('dataRowData',axis=1,errors='ignore',inplace=True)
  return res