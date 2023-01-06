import pandas as pd
import os
import glob

# Set WD #
os.chdir('C:/DATA/ADCPTXT/')

## Compiling CSV's into one ## # Data Frame generated
extension = 'txt'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames], 
                         keys=[f"{f.split('.')[0]}" for f in all_filenames]) # Adding filenames #

# Exporting CSV #
combined_csv.to_csv("combined_csv.csv", index=False)

## Removing duplicate GPS points, THIS ONE WORKS  ##
df = pd.read_csv('combined_csv.csv', index_col=0)

# Keep first row containing the duplicated entry and remove others, also removes no GPS data #
df.drop_duplicates(subset = ['GGA Latitude (491)', 'GGA Longitude (493)'], 
                   keep = 'first', inplace=True)

# Drop Total Width column #



# Renaming and reordering columns #

df.rename(columns={'Total Width (Ref: GGA) (244)' : 'Distance', 'GGA Latitude (491)': 'Latitude', 
                   'GGA Longitude (493)': 'Longitude', 'River Depth (484)': 'Depth'}, 
          errors="raise", inplace = True) ### Have to put inplace to actually put it in dataframe #

# Removing rows without depth #
df = df[df.Depth > 0]

# Adding in file names as column #




