import pandas as pd
import glob
from deepchecks.tabular.checks.integrity.data_duplicates import DataDuplicates
#from deepchecks.base import Dataset, Suite
from datetime import datetime
from deepchecks.checks import DataDuplicates
from deepchecks.tabular.checks.integrity.is_single_value import IsSingleValue
from deepchecks.tabular.checks.integrity.string_length_out_of_bounds import StringLengthOutOfBounds
from deepchecks.checks import MixedDataTypes
from deepchecks.checks import MixedNulls
from deepchecks.checks import SpecialCharacters
from deepchecks.checks import StringMismatch

path = "/home/.../resource/"
filenames = glob.glob(path + "/*.csv") 
for file in filenames: 
    print("\nReading file = ",file)
    data = pd.read_csv(file)
    r = StringMismatch().run(data)
    c  = StringMismatch().add_condition_no_variants() 
    print ((DataDuplicates().run(data), 
            (IsSingleValue().run(pd.DataFrame(data))), 
            (MixedDataTypes().add_condition_rare_type_ratio_not_in_range().run(data)),
            (MixedNulls().run(data)),
            (SpecialCharacters().run(data)),
            (c.conditions_decision(r)), 
            (StringLengthOutOfBounds(min_unique_value_ratio=0.01).run(data)), file), 
            file=open("/home/.../newresults.csv", "a") )
    


