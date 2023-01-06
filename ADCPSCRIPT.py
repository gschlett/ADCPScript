import pandas as pd
import os
import glob

# Set WD #
os.chdir('C:/DATA/ADCPTXT/')

## Compiling CSV's into one ## # Data Frame generated
extension = 'txt'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

df = pd.concat([pd.read_csv(f) for f in all_filenames], 
                         keys=[f"{f.split('.')[0]}" for f in all_filenames]) # Adding filenames #

# Keep first row containing the duplicated entry and remove others, also removes no GPS data #
df.drop_duplicates(subset = ['GGA Latitude (491)', 'GGA Longitude (493)'], 
                   keep = 'first', inplace=True)

# Renaming and reordering columns #

df.rename(columns={'Total Width (Ref: GGA) (244)' : 'Distance', 'GGA Latitude (491)': 'Latitude', 
                   'GGA Longitude (493)': 'Longitude', 'River Depth (484)': 'Depth'}, 
          errors="raise", inplace = True) ### Have to put inplace to actually put it in dataframe #

# Removing rows without depth #
df = df[df.Depth > 0]

# Drop the Distance column #
df.drop(columns = 'Distance', inplace = True)

# Writing to csv #
df.to_csv("df.csv", index=True)




