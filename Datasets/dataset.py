import pandas as pd
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
pen_based_recognition_of_handwritten_digits = fetch_ucirepo(id=81) 

X = pen_based_recognition_of_handwritten_digits.data.features 
y = pen_based_recognition_of_handwritten_digits.data.targets 
  
dataset = pd.concat([X, y], axis=1) # Combine features and targets into a single DataFrame

dataset.to_csv('pen_based_recognition_of_handwritten_digits.csv', index=False)

print("Dataset saved as 'pen_based_recognition_of_handwritten_digits.csv'.")

# For Readme.md
readme_content = f"# Pen-Based Recognition of Handwritten Digits Dataset\n\n"
readme_content += f"## Metadata\n\n{pen_based_recognition_of_handwritten_digits.metadata}\n\n"

# Write to README.md
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_content)

print("Metadata saved to 'README.md'.")