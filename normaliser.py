import pandas as pd

class Normaliser:
    def __init__(self):
        pass

    def _convert_to_df(self, data):
        df = pd.DataFrame.from_dict(data)

        return df
    
    def _rename_columns(self, df):
        # df.rename(columns=)
        pass

'''
1) Convert dict to DF
2) Rename columns
3) Reorder columns (if needed)
4) END
'''